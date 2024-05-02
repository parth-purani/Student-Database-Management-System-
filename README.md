# 🎓 Python Student Database Management System

This Python script acts as a comprehensive student database management system tailored for educational settings. It utilizes a command-line interface to facilitate various operations such as adding, editing, and removing student records, as well as managing course enrollments. All data is persistently stored in "studentsDatabase.dat".

## 🛠 Key Functionalities

### Adding New Student Record (`add` function)
- **Input Prompts**: Collects student ID, name, semester, email, and course codes.
- **Validation**: Ensures formats for course codes, semester, and uniqueness of student IDs are correct.
- **Data Writing**: Adds new records to both the database and the data file.

### Editing Existing Student Record (`edit` function)
- **Record Retrieval**: Locates the desired student record.
- **Field Editing**: Permits modifications to the semester or email fields.
- **Update**: Reflects changes in both the database and the data file.

### Dropping a Course (`drop` function)
- **Course Selection**: Identifies the course to be dropped from a student’s record.
- **Validation**: Checks if the course is listed under the student.
- **Database Update**: Removes the course and updates the file.

### Retrieving Information About a Student (`info` function)
- **Information Display**: Shows detailed information about a student, including enrolled courses.

### Removing a Student Record (`remove` function)
- **Record Deletion**: Completely erases a student's record post-confirmation.
- **File Update**: Ensures the data file is updated accordingly.

## 🖥️ Usage

Run the script within a Python environment. It operates continuously, allowing for multiple interactions until the user exits. Each function is crafted to validate user inputs rigorously before any modifications to the data are executed.

## 🏫 Ideal for Educational Projects

This system is perfect for educational projects focusing on:
- File handling
- Data manipulation
- User interface design within a command-line context

It provides a hands-on application for managing a simple database, demonstrating the foundational elements of data management and software design.

---

**Embark on managing educational data effectively with this robust Python script, tailored to enhance learning and application of database management principles!**
