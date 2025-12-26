# Medicine Alternative Finder

A backend-focused web application that identifies alternative medicines with the same salt composition and compares their prices to support cost-aware healthcare decisions.

---

## Problem Statement

Many medicines available in the market have equivalent alternatives with identical salt compositions but significantly different prices.  
Patients often lack visibility into these alternatives, which can lead to unnecessary healthcare expenses.

This project aims to bridge that gap by programmatically identifying equivalent medicines and presenting structured price comparisons.

---

## Solution Overview

The application allows users to search for a medicine by name.  
It automatically extracts the salt composition and retrieves all medicines sharing the same composition from a large dataset.

The results are analyzed and presented with clear pricing insights.

---

## Key Features

- Case-insensitive medicine search
- Automatic salt composition detection
- Identification of all equivalent medicines
- Price analysis including:
  - Minimum price
  - Maximum price
  - Average price
- Highlighting of cheapest and most expensive options
- Sorted display of affordable alternatives
- Efficient handling of a large dataset (220k+ records)

---

## Technical Approach

- Normalize medicine names for reliable searching
- Extract salt composition from the selected medicine
- Filter the dataset to identify matching compositions
- Perform price aggregation and comparison
- Render results using server-side templates

The focus is on backend logic, data correctness, and clarity of implementation.

---

## Tech Stack

### Backend
- Python
- Flask
- Pandas

### Frontend
- HTML (Jinja2 Templates)
- CSS

### Data
- CSV-based medicine dataset (220k+ records)

### Tools
- Git & GitHub
- Visual Studio Code

---

## Project Structure
```
medicine-project/
├── flaskcode.py
├── backend.py
├── pharmacy.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── .gitignore
```

---

## How to Run Locally

1. Clone the repository  
   git clone https://github.com/your-username/medicine-project.git  

2. Navigate to the project directory  
   cd medicine-project  

3. Install the required dependencies  
   pip install flask pandas  

4. Run the Flask application  
   python flaskcode.py  

5. Open the application in your browser  
   http://127.0.0.1:5000

## Limitations
- Dataset is static and CSV-based
- No authentication or user accounts
- UI is minimal and focused on functionality

---

## Future Improvements
•	Database integration for better scalability

•	API-based architecture

•	Improved search tolerance for misspellings

•	Enhanced UI/UX

•	Cloud deployment



