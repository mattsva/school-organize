from sqlalchemy import select
from .models import SessionLocal, User, Permission, Course, Subject, StudioTime

def enrich_item(item):
    session = SessionLocal()
    try:
        teacher_uuids = getattr(item, "teacher_uuids", [])
        # Be safe that is it a list... otherwise python hates it!
        if isinstance(teacher_uuids, int):
            teacher_uuids = [teacher_uuids]
        elif teacher_uuids is None:
            teacher_uuids = []

        teachers = []
        for t_uuid in teacher_uuids:
            t = session.get(User, t_uuid)
            if t:
                teachers.append(f"{t.firstname} {t.lastname}")

        return {
            "id": getattr(item, "id", None),
            "name": getattr(item, "name", ""),
            "times": {
                day: {
                    "time": time,
                    "room": getattr(item, "room", ""),
                    "teachers": teachers,
                    "color": getattr(item, "color", "#cccccc")
                }
                for day, time in getattr(item, "times", {}).items()
            }
        }
    finally:
        session.close()


def create_user(firstname, lastname, title):
    session = SessionLocal()
    try:
        user = User(firstname=firstname, lastname=lastname, title=title)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    finally:
        session.close()

def get_user(uuid):
    session = SessionLocal()
    try:
        user = session.get(User, uuid)

        if user is None:
            return {"details": "user not found"}

        return {
            "firstname": user.firstname,
            "lastname": user.lastname,
            "titel": user.title,
            "uuid": user.uuid
        }

    except Exception as e:
        return {"details": "unexpected error", "error": str(e)}

    finally:
        session.close()


def edit_user(uuid, firstname=None, lastname=None, title=None):
    session = SessionLocal()
    try:
        user = session.get(User, uuid)
        if not user:
            return None
        if firstname is not None:
            user.firstname = firstname
        if lastname is not None:
            user.lastname = lastname
        if title is not None:
            user.title = title
        session.commit()
        return user
    finally:
        session.close()

def delete_user(uuid):
    session = SessionLocal()
    try:
        user = session.get(User, uuid)
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True
    finally:
        session.close()

def list_users():
    session = SessionLocal()
    try:
        return session.query(User).all()
    finally:
        session.close()


def create_permission(name):
    session = SessionLocal()
    try:
        perm = session.execute(select(Permission).where(Permission.name==name)).scalar_one_or_none()
        if perm:
            return perm
        perm = Permission(name=name)
        session.add(perm)
        session.commit()
        return perm
    finally:
        session.close()

def assign_permission(user_uuid, perm_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        perm = session.execute(select(Permission).where(Permission.name==perm_name)).scalar_one_or_none()
        if not user or not perm:
            return False
        if perm not in user.permissions:
            user.permissions.append(perm)
            session.commit()
        return True
    finally:
        session.close()

def remove_permission(user_uuid, perm_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        perm = session.execute(select(Permission).where(Permission.name==perm_name)).scalar_one_or_none()
        if not user or not perm:
            return False
        if perm in user.permissions:
            user.permissions.remove(perm)
            session.commit()
        return True
    finally:
        session.close()

def list_permissions(user_uuid=None):
    session = SessionLocal()
    try:
        if user_uuid:
            user = session.get(User, user_uuid)
            return user.permissions if user else []
        return session.query(Permission).all()
    finally:
        session.close()

def create_course(name, teacher_uuids=None, times={}, color="#a0c4ff", room=""):
    teacher_uuids = teacher_uuids or []
    session = SessionLocal()
    try:
        course = session.execute(select(Course).where(Course.name==name)).scalar_one_or_none()
        if course:
            return course
        course = Course(name=name, teacher_uuids=teacher_uuids, times=times, color=color, room=room)
        session.add(course)
        session.commit()
        return course
    finally:
        session.close()

def edit_course(name, new_name=None, teacher_uuids=None, times=None, color=None, room=None):
    session = SessionLocal()
    try:
        course = session.execute(select(Course).where(Course.name==name)).scalar_one_or_none()
        if not course:
            return None
        if new_name:
            course.name = new_name
        if teacher_uuids is not None:
            course.teacher_uuids = teacher_uuids
        if times is not None:
            course.times = times
        if color is not None:
            course.color = color
        if room is not None:
            course.room = room
        session.commit()
        return course
    finally:
        session.close()

def delete_course(name):
    session = SessionLocal()
    try:
        course = session.execute(select(Course).where(Course.name==name)).scalar_one_or_none()
        if not course:
            return False
        session.delete(course)
        session.commit()
        return True
    finally:
        session.close()

def list_courses():
    session = SessionLocal()
    try:
        courses = session.query(Course).all()
        return [enrich_item(c) for c in courses]
    finally:
        session.close()

def book_course(user_uuid, course_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        course = session.execute(select(Course).where(Course.name==course_name)).scalar_one_or_none()
        if not user or not course:
            return False
        if course not in getattr(user, "courses", []):
            user.courses.append(course)
            session.commit()
        return enrich_item(course)
    finally:
        session.close()

def unbook_course(user_uuid, course_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        course = session.execute(select(Course).where(Course.name==course_name)).scalar_one_or_none()
        if not user or not course or course not in getattr(user, "courses", []):
            return False
        user.courses.remove(course)
        session.commit()
        return True
    finally:
        session.close()

def create_subject(name, teacher_uuids=None, times={}, color="#bdb2ff", room=""):
    teacher_uuids = teacher_uuids or []
    session = SessionLocal()
    try:
        subj = session.execute(select(Subject).where(Subject.name==name)).scalar_one_or_none()
        if subj:
            return subj
        subj = Subject(name=name, teacher_uuids=teacher_uuids, times=times, color=color, room=room)
        session.add(subj)
        session.commit()
        return subj
    finally:
        session.close()

def edit_subject(name, new_name=None, teacher_uuids=None, times=None, color=None, room=None):
    session = SessionLocal()
    try:
        subj = session.execute(select(Subject).where(Subject.name==name)).scalar_one_or_none()
        if not subj:
            return None
        if new_name:
            subj.name = new_name
        if teacher_uuids is not None:
            subj.teacher_uuids = teacher_uuids
        if times is not None:
            subj.times = times
        if color is not None:
            subj.color = color
        if room is not None:
            subj.room = room
        session.commit()
        return subj
    finally:
        session.close()

def delete_subject(name):
    session = SessionLocal()
    try:
        subj = session.execute(select(Subject).where(Subject.name==name)).scalar_one_or_none()
        if not subj:
            return False
        session.delete(subj)
        session.commit()
        return True
    finally:
        session.close()

def list_subjects():
    session = SessionLocal()
    try:
        subjects = session.query(Subject).all()
        return [enrich_item(s) for s in subjects]
    finally:
        session.close()

def book_subject(user_uuid, subject_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        subj = session.execute(select(Subject).where(Subject.name==subject_name)).scalar_one_or_none()
        if not user or not subj:
            return False
        if subj not in getattr(user, "subjects", []):
            user.subjects.append(subj)
            session.commit()
        return enrich_item(subj)
    finally:
        session.close()

def unbook_subject(user_uuid, subject_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        subj = session.execute(select(Subject).where(Subject.name==subject_name)).scalar_one_or_none()
        if not user or not subj or subj not in getattr(user, "subjects", []):
            return False
        user.subjects.remove(subj)
        session.commit()
        return True
    finally:
        session.close()

def create_studiotime(name, teacher_uuids=None, times={}, color="#ffadad", room=""):
    teacher_uuids = teacher_uuids or []
    session = SessionLocal()
    try:
        st = session.execute(select(StudioTime).where(StudioTime.name==name)).scalar_one_or_none()
        if st:
            return st
        st = StudioTime(name=name, teacher_uuids=teacher_uuids, times=times, color=color, room=room)
        session.add(st)
        session.commit()
        return st
    finally:
        session.close()

def list_studiotimes():
    session = SessionLocal()
    try:
        sts = session.query(StudioTime).all()
        return [enrich_item(st) for st in sts]
    finally:
        session.close()

def book_studiotime(user_uuid, studiostime_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        st = session.execute(select(StudioTime).where(StudioTime.name==studiostime_name)).scalar_one_or_none()
        if not user or not st:
            return False
        if st not in getattr(user, "studiots", []):
            user.studiots.append(st)
            session.commit()
        return enrich_item(st)
    finally:
        session.close()

def unbook_studiotime(user_uuid, studiostime_name):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        st = session.execute(select(StudioTime).where(StudioTime.name==studiostime_name)).scalar_one_or_none()
        if not user or not st or st not in getattr(user, "studiots", []):
            return False
        user.studiots.remove(st)
        session.commit()
        return True
    finally:
        session.close()

def set_grade(user_uuid, subject_name, grade):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        if not user:
            return False
        user.grades[subject_name] = grade
        session.commit()
        return True
    finally:
        session.close()

def add_absence(user_uuid, date, status):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        if not user:
            return False
        user.absence[date] = status
        session.commit()
        return True
    finally:
        session.close()

def build_timetable(user_uuid):
    session = SessionLocal()
    try:
        user = session.get(User, user_uuid)
        if not user:
            return {}

        timetable = {}

        def add_to_timetable(item, item_type):
            enriched = enrich_item(item)
            for day, info in enriched["times"].items():
                if day not in timetable:
                    timetable[day] = []
                timetable[day].append({
                    "name": enriched["name"],
                    "type": item_type,
                    "time": info["time"],
                    "room": info.get("room", ""),
                    "teachers": info.get("teachers", []),
                    "color": info.get("color", "#cccccc")
                })

        for c in user.courses:
            add_to_timetable(c, "course")

        for s in user.subjects:
            add_to_timetable(s, "subject")

        for st in user.studiots:
            add_to_timetable(st, "studiotime")

        user.timetable = timetable
        session.commit()

        return timetable
    finally:
        session.close()
