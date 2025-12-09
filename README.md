# School-Organize
***Version: 09th December 2025 — First Version***
**School-Organize** is an open-source project for managing students, teachers, courses, timetables, and attendance in schools. It can be run locally or as a web application using FastAPI.

## Author

**Mattsva**  
GitHub: [https://github.com/mattsva/school-organize](https://github.com/mattsva/school-organize)

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  
Full license: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

You are free to copy, adapt, and redistribute this project **for non-commercial purposes**, provided you credit **Mattsva** as the original author.

**No Warranty / Liability:**  
This software is provided "as-is", without any warranty. The author is not responsible for any damages, errors, or losses resulting from using this software.

## Features

- Manage **users** (students, teachers)
- Create and edit **courses, subjects, and studio times**
- Assign **permissions**
- Book system for students
- Automatic **timetable generation** per user
- Track **grades and absences**

## Installation# School-Organize

**School-Organize** is an open-source project for managing students, teachers, courses, timetables, and attendance in schools. It can be run locally or as a web application using FastAPI.

## Author

**Mattsva**  
GitHub: [https://github.com/mattsva/school-organize](https://github.com/mattsva/school-organize)

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  
Full license: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

You are free to copy, adapt, and redistribute this project **for non-commercial purposes**, provided you credit **Mattsva** as the original author.

**No Warranty / Liability:**  
This software is provided "as-is", without any warranty. The author is not responsible for any damages, errors, or losses resulting from using this software.

## Features

- Manage **users** (students, teachers)
- Create and edit **courses, subjects, and studio times**
- Assign **permissions**
- Book system for students
- Automatic **timetable generation** per user
- Track **grades and absences**

## Installation

This project uses **Python 3.13** and **Pipenv** for dependency management.

```bash
# Clone the repository
git clone https://github.com/mattsva/school-organize.git
cd school-organize

# Install Pipenv if not already installed
pip install --user pipenv

# Create virtual environment and install dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Optional: Run the FastAPI server
uvicorn api.main:app --reload


This project uses **Python 3.13** and **Pipenv** for dependency management.

```bash
# Clone the repository
git clone https://github.com/mattsva/school-organize.git
cd school-organize

# Install Pipenv if not already installed
pip install --user pipenv

# Create virtual environment and install dependencies
pipenv install

# Activate the virtual environment
pipenv shell

# Optional: Run the FastAPI server
uvicorn api.main:app --reload
