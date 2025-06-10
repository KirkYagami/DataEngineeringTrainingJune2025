# Project 3: Task Management CLI Tool 📋

## Overview
Build a comprehensive command-line task management application using Object-Oriented Programming principles and SQLite database integration. Create a professional-grade productivity tool that helps users organize, track, and manage their tasks and projects efficiently.

## Difficulty Level
**Intermediate to Advanced** | **Estimated Time: 14-18 hours**

---

## Problem Statement

Develop a feature-rich task management system that demonstrates advanced Python concepts including OOP design patterns, database operations, and complex data relationships. The application should provide a seamless command-line interface for managing personal and professional tasks.

### Learning Objectives
- Master Object-Oriented Programming (classes, inheritance, encapsulation)
- Implement SQLite database operations with proper schema design
- Build complex command-line interfaces with argument parsing
- Handle data relationships and foreign keys
- Implement search, filtering, and sorting algorithms
- Create data export/import functionality
- Apply software design patterns and best practices

---

## Core Requirements

#### 1. Task Management System
- Create, read, update, and delete tasks with full CRUD operations
- Task properties: title, description, priority, status, due date, created date
- Support for task categories and tags
- Task status tracking (Todo, In Progress, Completed, Cancelled)
- Priority levels (Low, Medium, High, Critical)

#### 2. Project Organization
- Group tasks into projects for better organization
- Project-level statistics and progress tracking
- Assign tasks to specific projects
- Project templates for recurring workflows

#### 3. Advanced Features
- Search and filter tasks by multiple criteria
- Sort tasks by priority, due date, creation date, or status
- Set reminders and due date notifications
- Task dependencies (prerequisite tasks)
- Time tracking for task completion

#### 4. Database Integration
- SQLite database for persistent data storage
- Proper database schema with relationships
- Data integrity constraints and validation
- Database migration and backup functionality

---

## Technical Specifications

### Required Features

#### Core Task Operations (40 points)
- [x] **Task CRUD**: Complete Create, Read, Update, Delete operations
- [x] **Task Properties**: All required fields with proper validation
- [x] **Status Management**: Task lifecycle with status transitions
- [x] **Priority System**: Multi-level priority with visual indicators
- [x] **Due Date Handling**: Date validation and overdue detection
- [x] **Task Categories**: Flexible categorization system

#### Project Management (25 points)
- [x] **Project Creation**: Create and manage multiple projects
- [x] **Task Assignment**: Link tasks to specific projects
- [x] **Project Statistics**: Progress tracking and completion rates
- [x] **Project Views**: Filter tasks by project
- [x] **Project Templates**: Reusable project structures

#### Database & Data Management (20 points)
- [x] **SQLite Integration**: Proper database design and operations
- [x] **Data Relationships**: Foreign keys and referential integrity
- [x] **Search & Filter**: Complex queries with multiple criteria
- [x] **Data Export**: Export tasks to CSV/JSON formats
- [x] **Database Backup**: Backup and restore functionality

#### User Interface & Experience (15 points)
- [x] **CLI Interface**: Intuitive command-line interface
- [x] **Help System**: Comprehensive help and usage information
- [x] **Error Handling**: Graceful error handling and user feedback
- [x] **Data Visualization**: Task statistics and progress displays

### Bonus Features (Extra 30 points)
- [ ] **Task Dependencies**: Prerequisite task relationships
- [ ] **Time Tracking**: Log time spent on tasks
- [ ] **Recurring Tasks**: Automatic task creation on schedules
- [ ] **Task Templates**: Reusable task structures
- [ ] **Collaboration**: Multi-user support with task assignment
- [ ] **API Integration**: Sync with external calendar/task services

---

## Implementation Guidelines

### Object-Oriented Design

```python
from datetime import datetime, date
import sqlite3
from enum import Enum
from typing import List, Optional
import argparse

class TaskStatus(Enum):
    """Enumeration for task status values"""
    TODO = "Todo"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Priority(Enum):
    """Enumeration for task priority levels"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class Task:
    """Represents a single task with all its properties"""
    
    def __init__(self, title: str, description: str = "", 
                 priority: Priority = Priority.MEDIUM,
                 due_date: Optional[date] = None,
                 project_id: Optional[int] = None):
        self.id = None
        self.title = title
        self.description = description
        self.priority = priority
        self.status = TaskStatus.TODO
        self.due_date = due_date
        self.project_id = project_id
        self.created_date = datetime.now()
        self.completed_date = None
        self.tags = []
    
    def mark_completed(self):
        """Mark task as completed"""
        pass
    
    def is_overdue(self) -> bool:
        """Check if task is overdue"""
        pass
    
    def __str__(self) -> str:
        """String representation of task"""
        pass
    
    def to_dict(self) -> dict:
        """Convert task to dictionary for export"""
        pass

class Project:
    """Represents a project containing multiple tasks"""
    
    def __init__(self, name: str, description: str = ""):
        self.id = None
        self.name = name
        self.description = description
        self.created_date = datetime.now()
        self.tasks = []
    
    def get_completion_rate(self) -> float:
        """Calculate project completion percentage"""
        pass
    
    def get_task_count_by_status(self) -> dict:
        """Get count of tasks by status"""
        pass

class DatabaseManager:
    """Handles all database operations"""
    
    def __init__(self, db_path: str = "tasks.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database schema"""
        pass
    
    def create_task(self, task: Task) -> int:
        """Insert new task into database"""
        pass
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID"""
        pass
    
    def update_task(self, task: Task) -> bool:
        """Update existing task"""
        pass
    
    def delete_task(self, task_id: int) -> bool:
        """Delete task from database"""
        pass
    
    def search_tasks(self, **criteria) -> List[Task]:
        """Search tasks by various criteria"""
        pass
    
    def create_project(self, project: Project) -> int:
        """Create new project"""
        pass
    
    def get_all_projects(self) -> List[Project]:
        """Retrieve all projects"""
        pass

class TaskManager:
    """Main application class orchestrating all operations"""
    
    def __init__(self):
        self.db = DatabaseManager()
    
    def add_task(self, title: str, **kwargs):
        """Add new task with validation"""
        pass
    
    def list_tasks(self, **filters):
        """List tasks with optional filtering"""
        pass
    
    def update_task(self, task_id: int, **updates):
        """Update task properties"""
        pass
    
    def delete_task(self, task_id: int):
        """Delete task with confirmation"""
        pass
    
    def mark_completed(self, task_id: int):
        """Mark task as completed"""
        pass
    
    def show_statistics(self):
        """Display task statistics and insights"""
        pass
    
    def export_tasks(self, format: str = "csv"):
        """Export tasks to file"""
        pass

class CLIInterface:
    """Command-line interface handler"""
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.setup_parser()
    
    def setup_parser(self):
        """Setup argument parser for CLI commands"""
        pass
    
    def run(self):
        """Main CLI execution loop"""
        pass
    
    def display_tasks(self, tasks: List[Task]):
        """Display tasks in formatted table"""
        pass
    
    def display_help(self):
        """Show comprehensive help information"""
        pass

def main():
    """Application entry point"""
    cli = CLIInterface()
    cli.run()

if __name__ == "__main__":
    main()
```

### Database Schema Design

```sql
-- Projects table
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tasks table
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    priority INTEGER NOT NULL DEFAULT 2,
    status TEXT NOT NULL DEFAULT 'Todo',
    due_date DATE,
    project_id INTEGER,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_date TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);

-- Tags table
CREATE TABLE tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Task-Tags junction table (many-to-many relationship)
CREATE TABLE task_tags (
    task_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
);

-- Task dependencies table
CREATE TABLE task_dependencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    depends_on_task_id INTEGER NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks (id) ON DELETE CASCADE,
    FOREIGN KEY (depends_on_task_id) REFERENCES tasks (id) ON DELETE CASCADE
);
```

### Required Files Structure
```
task_manager/
├── task_manager.py        # Main application file
├── models/
│   ├── __init__.py
│   ├── task.py           # Task class definition
│   ├── project.py        # Project class definition
│   └── database.py       # Database manager
├── cli/
│   ├── __init__.py
│   ├── interface.py      # CLI interface handler
│   └── commands.py       # Individual command implementations
├── utils/
│   ├── __init__.py
│   ├── validators.py     # Input validation functions
│   ├── formatters.py     # Output formatting utilities
│   └── exporters.py      # Data export functionality
├── data/
│   ├── tasks.db          # SQLite database file
│   └── backups/          # Database backup files
├── tests/
│   ├── test_models.py    # Unit tests for models
│   ├── test_database.py  # Database operation tests
│   └── test_cli.py       # CLI interface tests
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

---

## Command-Line Interface Design

### Basic Commands
```bash
# Task Management
python task_manager.py add "Complete project proposal" --priority high --due 2024-07-15 --project "Work Tasks"
python task_manager.py list --status todo --priority high
python task_manager.py update 5 --status "in-progress" --description "Updated description"
python task_manager.py complete 5
python task_manager.py delete 5

# Project Management
python task_manager.py project create "Personal Goals" --description "My 2024 objectives"
python task_manager.py project list
python task_manager.py project show "Personal Goals"
python task_manager.py project stats "Personal Goals"

# Search and Filter
python task_manager.py search --keyword "proposal" --tag "important"
python task_manager.py list --overdue
python task_manager.py list --project "Work Tasks" --status todo

# Statistics and Reports
python task_manager.py stats
python task_manager.py report --monthly
python task_manager.py export --format csv --output tasks_backup.csv
```

### Interactive Mode
```bash
python task_manager.py interactive

=== TASK MANAGER ===
1. Add Task
2. List Tasks
3. Update Task
4. Complete Task
5. Delete Task
6. Manage Projects
7. Search Tasks
8. View Statistics
9. Export Data
0. Exit

Enter your choice: 1

=== ADD NEW TASK ===
Title: Complete project documentation
Description: Write comprehensive docs for the new feature
Priority (low/medium/high/critical): high
Due date (YYYY-MM-DD) or press Enter: 2024-07-20
Project (or press Enter for none): Documentation Project
Tags (comma-separated): documentation, urgent, deadline

Task created successfully! ID: 15
```

---

## Advanced Features Implementation

### 1. Search and Filter System
```python
class TaskSearcher:
    """Advanced search functionality for tasks"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def search(self, **criteria) -> List[Task]:
        """Multi-criteria search with AND/OR logic"""
        query_parts = []
        params = []
        
        if 'keyword' in criteria:
            query_parts.append("(title LIKE ? OR description LIKE ?)")
            keyword = f"%{criteria['keyword']}%"
            params.extend([keyword, keyword])
        
        if 'status' in criteria:
            query_parts.append("status = ?")
            params.append(criteria['status'])
        
        if 'priority' in criteria:
            query_parts.append("priority = ?")
            params.append(criteria['priority'])
        
        if 'overdue' in criteria and criteria['overdue']:
            query_parts.append("due_date < date('now') AND status != 'Completed'")
        
        # Build and execute query
        base_query = "SELECT * FROM tasks"
        if query_parts:
            base_query += " WHERE " + " AND ".join(query_parts)
        
        return self.db.execute_search(base_query, params)
```

### 2. Task Statistics and Analytics
```python
class TaskAnalytics:
    """Generate insights and statistics from task data"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
    
    def get_completion_stats(self) -> dict:
        """Calculate completion statistics"""
        pass
    
    def get_productivity_trends(self, days: int = 30) -> dict:
        """Analyze productivity trends over time"""
        pass
    
    def get_priority_distribution(self) -> dict:
        """Get distribution of tasks by priority"""
        pass
    
    def generate_weekly_report(self) -> str:
        """Generate formatted weekly productivity report"""
        pass
```

### 3. Data Export and Import
```python
class DataExporter:
    """Handle data export in various formats"""
    
    def export_to_csv(self, tasks: List[Task], filename: str):
        """Export tasks to CSV format"""
        pass
    
    def export_to_json(self, tasks: List[Task], filename: str):
        """Export tasks to JSON format"""
        pass
    
    def export_project_report(self, project_id: int, filename: str):
        """Export comprehensive project report"""
        pass
    
    def import_from_csv(self, filename: str) -> int:
        """Import tasks from CSV file"""
        pass
```

---

## Testing Framework

### Unit Testing Structure
```python
import unittest
from unittest.mock import Mock, patch
from models.task import Task, TaskStatus, Priority
from models.database import DatabaseManager

class TestTask(unittest.TestCase):
    """Test Task class functionality"""
    
    def setUp(self):
        self.task = Task("Test Task", "Test Description")
    
    def test_task_creation(self):
        """Test task initialization"""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.status, TaskStatus.TODO)
    
    def test_mark_completed(self):
        """Test task completion"""
        self.task.mark_completed()
        self.assertEqual(self.task.status, TaskStatus.COMPLETED)
        self.assertIsNotNone(self.task.completed_date)
    
    def test_overdue_detection(self):
        """Test overdue task detection"""
        # Test with past due date
        past_date = date.today() - timedelta(days=1)
        self.task.due_date = past_date
        self.assertTrue(self.task.is_overdue())

class TestDatabaseManager(unittest.TestCase):
    """Test database operations"""
    
    def setUp(self):
        self.db = DatabaseManager(":memory:")  # Use in-memory database for testing
    
    def test_create_task(self):
        """Test task creation in database"""
        task = Task("Test Task")
        task_id = self.db.create_task(task)
        self.assertIsNotNone(task_id)
        
        retrieved_task = self.db.get_task(task_id)
        self.assertEqual(retrieved_task.title, "Test Task")

if __name__ == "__main__":
    unittest.main()
```

---

## Performance Requirements

### Database Optimization
- Implement proper indexing for frequently queried columns
- Use prepared statements for repeated queries
- Implement connection pooling for better performance
- Handle large datasets with pagination

### Memory Management
- Lazy loading for large task lists
- Efficient data structures for in-memory operations
- Proper resource cleanup and garbage collection

---

## Evaluation Criteria

| Criteria | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|----------|---------------|----------|------------------|------------------|
| **OOP Design** | Excellent class design, proper inheritance, encapsulation | Good OOP principles, minor issues | Basic OOP implementation | Poor or missing OOP concepts |
| **Database Integration** | Robust SQLite operations, proper schema, data integrity | Good database usage, minor issues | Basic database functionality | Poor database implementation |
| **CLI Interface** | Professional CLI, excellent UX, comprehensive commands | Good interface, clear commands | Basic CLI functionality | Poor or confusing interface |
| **Search & Filter** | Advanced search capabilities, multiple criteria | Good search functionality | Basic search implemented | Limited or broken search |
| **Code Architecture** | Excellent separation of concerns, modular design | Good structure, well-organized | Adequate organization | Poor structure, tightly coupled |
| **Error Handling** | Comprehensive error handling, graceful failures | Good error management | Basic error handling | Poor or missing error handling |
| **Documentation** | Excellent docs, clear examples, comprehensive | Good documentation | Basic documentation | Poor or missing docs |

---

## Submission Requirements

### What to Submit
1. **Complete Source Code**: All Python files with proper documentation
2. **Database Schema**: SQL file with table creation scripts
3. **Sample Data**: Pre-populated database with sample tasks and projects
4. **Test Suite**: Unit tests covering core functionality
5. **Documentation Package**:
   - README.md with installation and usage instructions
   - API documentation for classes and methods
   - User manual with command examples
   - Design document explaining architecture choices

### Demonstration Requirements
Your submission should include:
- At least 25 sample tasks across different projects
- Multiple projects with varying completion states
- Examples of all task statuses and priority levels
- Demonstration of search and filter capabilities
- Sample exported data files

### Code Quality Standards
- Proper PEP 8 style compliance
- Comprehensive docstrings for all classes and methods
- Type hints for function parameters and return values
- Meaningful variable and function names
- Proper error handling and logging
- Modular design with clear separation of concerns

---

## Advanced Extensions (Graduate Level)

For students seeking additional challenge:

1. **Web API**: Create REST API endpoints using Flask/FastAPI
2. **Plugin System**: Implement plugin architecture for extensibility
3. **Real-time Sync**: Implement real-time synchronization across devices
4. **Performance Optimization**: Add caching, indexing, and query optimization
5. **Advanced Analytics**: Machine learning for task completion prediction
6. **Integration**: Connect with external services (Google Calendar, Slack, etc.)

---

## Common Implementation Challenges

### 1. Database Design
- Properly handle foreign key relationships
- Implement cascading deletes correctly
- Design efficient indexes for search operations

### 2. Date Handling
- Handle timezone differences properly
- Validate date inputs and ranges
- Calculate overdue tasks accurately

### 3. CLI Interface
- Implement proper argument parsing
- Handle edge cases in user input
- Provide helpful error messages

### 4. Data Integrity
- Validate all user inputs
- Handle database connection failures
- Implement proper transaction management

---

## Resources

- [SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Argparse Tutorial](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Unit Testing Framework](https://docs.python.org/3/library/unittest.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

---

## Academic Integrity

This project requires original implementation of OOP concepts and database operations. While you may reference documentation and tutorials, your class designs and implementations must be your own work. Proper citation is required for any external code or design patterns used.

**Build something amazing that showcases your growing Python expertise! 🚀✨**