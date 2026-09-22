# School
An Object-Oriented School Management System in Python demonstrating Inheritance, Polymorphism, Encapsulation via Properties, and Object Relationships (Aggregation).

# 🏫 School Management System (Python OOP)

A modular Python program that simulates a basic **School Management System**. This project showcases advanced Object-Oriented Programming (OOP) design patterns, focusing on class hierarchies, attribute privacy, polymorphism, and relationship modeling between domain entities.

---

## ✨ Features

- **Base Person Class**: Unified base representation for shared user attributes (`name`, `email`) and methods (`introduce`).
- **Student & Teacher Entities**: Extended inherited classes with role-specific logic, course enrollment, and subject tracking.
- **Course & Student Relationships**: Dynamic registration linking teachers, courses, and student rosters with duplicate prevention.
- **Encapsulated Grades**: Controlled access to student grades using Python `@property` getters and setters with range validation (`0` - `100`).
- **Static Counter Metrics**: Real-time tracking of generated instances (`total_students`, `total_courses`) using class attributes.

---

## 🛠️ Concepts Demonstrated

| Concept | Implementation in Code |
| :--- | :--- |
| **Inheritance** | `Student` and `Teacher` inherit from the `Person` base class. |
| **Polymorphism** | Overriding `introduce()` method across different child classes. |
| **Encapsulation** | Private attribute `__grade` with validation via `@property` and `@grade.setter`. |
| **Aggregation / Relationships** | `Course` holds references to `Teacher` and `Student` objects. |
| **Class Attributes** | Static counters tracking total `Course` and `Student` instances. |

---

## 🚀 How to Run

1. **Prerequisites**: Ensure Python 3.x is installed.
2. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME
