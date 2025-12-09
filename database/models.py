from sqlalchemy import Column, Integer, String, JSON, Table, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///school.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    users = relationship("User", secondary="user_permissions", back_populates="permissions")

user_permissions = Table(
    "user_permissions",
    Base.metadata,
    Column("user_uuid", Integer, ForeignKey("users.uuid"), primary_key=True),
    Column("perm_id", Integer, ForeignKey("permissions.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    uuid = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String)
    lastname = Column(String)
    title = Column(String)
    grades = Column(JSON, default={})
    absence = Column(JSON, default={})
    timetable = Column(JSON, default={})

    permissions = relationship("Permission", secondary=user_permissions, back_populates="users")
    courses = relationship("Course", secondary="user_courses", back_populates="users")
    subjects = relationship("Subject", secondary="user_subjects", back_populates="users")
    studiots = relationship("StudioTime", secondary="user_studiotimes", back_populates="users")

user_courses = Table(
    "user_courses",
    Base.metadata,
    Column("user_uuid", Integer, ForeignKey("users.uuid"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True)
)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    teacher_uuids = Column(JSON, default=[])
    times = Column(JSON, default={})
    color = Column(String, default="#cccccc")
    room = Column(String, default="")

    users = relationship("User", secondary=user_courses, back_populates="courses")

user_subjects = Table(
    "user_subjects",
    Base.metadata,
    Column("user_uuid", Integer, ForeignKey("users.uuid"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subjects.id"), primary_key=True)
)

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    teacher_uuids = Column(JSON, default=[])
    times = Column(JSON, default={})
    color = Column(String, default="#bdb2ff")
    room = Column(String, default="")

    users = relationship("User", secondary=user_subjects, back_populates="subjects")

user_studiotimes = Table(
    "user_studiotimes",
    Base.metadata,
    Column("user_uuid", Integer, ForeignKey("users.uuid"), primary_key=True),
    Column("studiotime_id", Integer, ForeignKey("studiotimes.id"), primary_key=True)
)

class StudioTime(Base):
    __tablename__ = "studiotimes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    teacher_uuids = Column(JSON, default=[])
    times = Column(JSON, default={})
    color = Column(String, default="#ffadad")
    room = Column(String, default="")

    users = relationship("User", secondary=user_studiotimes, back_populates="studiots")

def init_db():
    Base.metadata.create_all(engine)
