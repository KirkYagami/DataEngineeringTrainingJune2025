# Project 2: Personal Finance Tracker 💰

## Overview
Build a comprehensive personal finance tracking application that allows users to manage their income, expenses, budgets, and generate insightful financial reports with data visualization.

## Difficulty Level
**Intermediate** | **Estimated Time: 12-16 hours**

---

## Problem Statement

Create a command-line personal finance tracker that helps users monitor their financial health through transaction tracking, budget management, and detailed reporting with visual charts.

### Learning Objectives
- Master file I/O operations with CSV files
- Implement data structures for complex data management
- Create data analysis and reporting features
- Generate visualizations using matplotlib/plotly
- Handle date/time operations effectively
- Build a menu-driven application architecture

---

## Core Requirements

#### 1. Transaction Management
- Add income and expense transactions
- Categorize transactions (Food, Transport, Entertainment, Salary, etc.)
- Edit and delete existing transactions
- Import/export transactions from/to CSV files
- Validate transaction data (amounts, dates, categories)

#### 2. Budget Planning
- Set monthly budgets for different categories
- Track budget vs actual spending
- Generate budget alerts and warnings
- Support for multiple budget periods (monthly/yearly)

#### 3. Reporting & Analytics
- Generate monthly and yearly financial reports
- Calculate total income, expenses, and savings
- Category-wise spending analysis
- Trend analysis over time periods
- Export reports to PDF/CSV formats

#### 4. Data Visualization
- Spending by category (pie charts)
- Income vs expenses over time (line graphs)
- Monthly spending trends (bar charts)
- Budget vs actual comparison charts

---

## Technical Specifications

### Required Features

#### Core Functionality (60 points)
- [x] **Transaction CRUD**: Create, Read, Update, Delete transactions
- [x] **Data Persistence**: Save/load data from CSV files
- [x] **Category Management**: Predefined and custom categories
- [x] **Date Handling**: Proper date validation and formatting
- [x] **Amount Validation**: Handle decimal amounts and currency formatting
- [x] **Search & Filter**: Find transactions by date range, category, or amount

#### Budget Management (25 points)
- [x] **Budget Creation**: Set budgets for categories and time periods
- [x] **Budget Tracking**: Compare actual spending vs budgets
- [x] **Alert System**: Warn when approaching or exceeding budgets
- [x] **Budget Reports**: Generate budget performance reports

#### Reporting & Visualization (15 points)
- [x] **Financial Reports**: Monthly/yearly summary reports
- [x] **Data Visualization**: Charts for spending patterns and trends
- [x] **Export Options**: Save reports as CSV or text files
- [x] **Trend Analysis**: Show spending patterns over time

### Bonus Features (Extra 25 points)
- [ ] **Recurring Transactions**: Automatic monthly bills/salary entries
- [ ] **Multiple Accounts**: Support for checking, savings, credit cards
- [ ] **Goal Tracking**: Savings goals with progress monitoring
- [ ] **Data Backup**: Automatic backup and restore functionality
- [ ] **Advanced Analytics**: Forecasting and financial health scores

---

## Implementation Guidelines

### Suggested Program Structure

```python
import csv
import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import os

class Transaction:
    """Represents a single financial transaction"""
    def __init__(self, date, description, amount, category, transaction_type):
        pass

class FinanceTracker:
    """Main finance tracker application"""
    def __init__(self):
        self.transactions = []
        self.budgets = {}
        self.categories = {
            'income': ['Salary', 'Freelance', 'Investment', 'Other Income'],
            'expense': ['Food', 'Transport', 'Entertainment', 'Utilities', 
                       'Healthcare', 'Shopping', 'Other Expense']
        }
    
    # Transaction Management
    def add_transaction(self):
        """Add new income or expense transaction"""
        pass
    
    def view_transactions(self):
        """Display all transactions with filtering options"""
        pass
    
    def edit_transaction(self):
        """Modify existing transaction"""
        pass
    
    def delete_transaction(self):
        """Remove transaction from records"""
        pass
    
    # Data Persistence
    def save_to_csv(self, filename='transactions.csv'):
        """Save transactions to CSV file"""
        pass
    
    def load_from_csv(self, filename='transactions.csv'):
        """Load transactions from CSV file"""
        pass
    
    # Budget Management
    def set_budget(self):
        """Set monthly budget for categories"""
        pass
    
    def check_budget_status(self):
        """Check current budget vs spending"""
        pass
    
    # Reporting
    def generate_monthly_report(self, month, year):
        """Generate detailed monthly financial report"""
        pass
    
    def generate_category_report(self):
        """Show spending breakdown by category"""
        pass
    
    # Visualization
    def plot_spending_by_category(self):
        """Create pie chart of spending by category"""
        pass
    
    def plot_income_vs_expenses(self):
        """Create line chart showing financial trends"""
        pass
    
    def plot_monthly_trends(self):
        """Create bar chart of monthly spending trends"""
        pass

def main():
    """Main application entry point"""
    tracker = FinanceTracker()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            tracker.add_transaction()
        elif choice == '2':
            tracker.view_transactions()
        # ... handle other menu options
        elif choice == '0':
            print("Thank you for using Finance Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    """Display main application menu"""
    pass

if __name__ == "__main__":
    main()
```

### Required Files Structure
```
finance_tracker/
├── finance_tracker.py     # Main application file
├── transaction.py         # Transaction class (optional)
├── data/
│   ├── transactions.csv   # Transaction data
│   ├── budgets.csv       # Budget data
│   └── backup/           # Backup files
├── reports/
│   ├── monthly_reports/  # Generated reports
│   └── charts/           # Generated visualizations
├── requirements.txt      # Required Python packages
└── README.md            # Project documentation
```

---

## Sample Application Flow

```
=== PERSONAL FINANCE TRACKER ===

1. Add Transaction
2. View Transactions
3. Edit Transaction
4. Delete Transaction
5. Set Budget
6. View Budget Status
7. Generate Reports
8. View Charts
9. Import/Export Data
0. Exit

Enter your choice: 1

=== ADD TRANSACTION ===
Transaction Type (income/expense): expense
Date (YYYY-MM-DD) or press Enter for today: 2024-06-10
Description: Grocery shopping
Amount: 75.50
Category:
1. Food
2. Transport
3. Entertainment
4. Utilities
5. Healthcare
6. Shopping
7. Other Expense
Choose category: 1

Transaction added successfully!
Total expenses this month: $523.75
Food budget remaining: $176.25

Press Enter to continue...
```

---

## Data Models

### Transaction CSV Format
```csv
date,description,amount,category,type,id
2024-06-01,Salary,3000.00,Salary,income,1
2024-06-02,Grocery Store,85.50,Food,expense,2
2024-06-03,Gas Station,45.00,Transport,expense,3
2024-06-05,Movie Tickets,24.99,Entertainment,expense,4
```

### Budget CSV Format
```csv
category,monthly_limit,current_spent,month,year
Food,300.00,123.75,6,2024
Transport,200.00,45.00,6,2024
Entertainment,150.00,24.99,6,2024
```

---

## Required Features Detail

### 1. Menu System
Create an intuitive menu-driven interface with clear options:
- Transaction management (add, view, edit, delete)
- Budget management (set, view, check status)
- Reporting (monthly, yearly, category-wise)
- Data visualization (charts and graphs)
- Import/export functionality

### 2. Input Validation
Implement robust validation for:
- Date formats (YYYY-MM-DD)
- Monetary amounts (positive numbers, proper decimal handling)
- Category selection from predefined lists
- Required field validation

### 3. Data Analysis Features
```python
def calculate_monthly_summary(self, month, year):
    """Calculate total income, expenses, and savings for a month"""
    pass

def get_category_totals(self, start_date, end_date):
    """Get spending totals by category for date range"""
    pass

def calculate_average_spending(self, category, months=3):
    """Calculate average spending for a category"""
    pass
```

### 4. Visualization Requirements
- **Pie Chart**: Monthly spending by category
- **Line Chart**: Income vs expenses over time
- **Bar Chart**: Category-wise spending comparison
- **Trend Chart**: 6-month spending trends

---

## Testing Checklist

### Data Management
- [ ] Transactions save and load correctly from CSV
- [ ] Data validation prevents invalid entries
- [ ] Edit and delete operations work properly
- [ ] Large datasets are handled efficiently
- [ ] Backup and restore functionality works

### Budget Features
- [ ] Budget limits are set and stored correctly
- [ ] Budget tracking calculates remaining amounts accurately
- [ ] Alerts trigger when approaching budget limits
- [ ] Multiple budget periods are supported

### Reporting
- [ ] Monthly reports generate accurate summaries
- [ ] Category reports show correct totals
- [ ] Date range filtering works properly
- [ ] Export functionality creates proper files

### Visualization
- [ ] Charts display correct data
- [ ] Multiple chart types are supported
- [ ] Charts save to files properly
- [ ] Visual formatting is professional

---

## Required Python Packages

Create `requirements.txt`:
```
matplotlib>=3.5.0
pandas>=1.3.0
datetime
csv
os
collections
```

Install with: `pip install -r requirements.txt`

---

## Evaluation Criteria

| Criteria | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|----------|---------------|----------|------------------|------------------|
| **Data Management** | Robust CSV handling, perfect data integrity | Good file operations, minor issues | Basic file I/O works | Data loss or corruption issues |
| **User Interface** | Intuitive menu, excellent UX | Clear interface, good flow | Basic but functional | Confusing or frustrating |
| **Budget Features** | Complete budget system with alerts | Budget tracking works well | Basic budget functionality | Missing or broken budget features |
| **Reporting** | Comprehensive reports with insights | Good reporting capabilities | Basic reports generated | Poor or missing reports |
| **Visualization** | Professional charts, multiple types | Good charts, clear data presentation | Basic charts work | Poor or missing visualizations |
| **Code Quality** | Excellent OOP design, clean code | Good structure, readable | Adequate organization | Poor structure, hard to maintain |

---

## Submission Requirements

### What to Submit
1. **Source Code**: All Python files with clear documentation
2. **Sample Data**: transactions.csv with at least 20 sample transactions
3. **Requirements File**: requirements.txt with all dependencies
4. **Documentation**: README.md with:
   - Installation and setup instructions
   - Feature overview and usage guide
   - Sample screenshots of reports and charts
   - Known limitations and future improvements
5. **Demo Files**: Sample generated reports and chart images

### Testing Data
Include sample data covering:
- Multiple months of transactions
- Various categories and amounts
- Both income and expense entries
- Different transaction types

### Code Quality Requirements
- Proper error handling for file operations
- Input validation for all user inputs
- Clear function documentation with docstrings
- Consistent coding style and naming conventions
- Separation of concerns (data, logic, presentation)

---

## Advanced Challenges (Optional)

For students who finish early or want extra challenges:

1. **Web Interface**: Convert to Flask web application
2. **Database Integration**: Use SQLite instead of CSV files
3. **Multi-Currency Support**: Handle different currencies with conversion
4. **Mobile Export**: Generate mobile-friendly reports
5. **API Integration**: Connect to bank APIs for automatic transaction import

---

## Common Pitfalls to Avoid

1. **Date Handling**: Use proper date objects, handle different formats
2. **Float Precision**: Use decimal module for accurate money calculations
3. **File Operations**: Always handle file not found exceptions
4. **Data Validation**: Don't trust user input, validate everything
5. **Memory Management**: Don't load massive CSV files into memory at once

---

## Resources

- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Python DateTime Module](https://docs.python.org/3/library/datetime.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [File I/O Best Practices](https://realpython.com/working-with-files-in-python/)

---

## Academic Integrity
This project builds on concepts from Project 1. While you may discuss approaches with classmates, your implementation must be original. Proper attribution is required for any external code or libraries used.

**Happy coding, and may your finances be ever in your favor! 📊💪**