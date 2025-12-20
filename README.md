# Medicine Alternative Finder

A web application that helps users find alternative medicines with the same salt composition and compare their prices to make informed and cost-effective healthcare decisions.

---

## Overview

The Medicine Alternative Finder allows users to search for a medicine by name and retrieves all other medicines with the same salt composition. It provides a detailed price comparison, highlighting budget-friendly and premium options.

This project focuses on real-world healthcare utility and efficient data processing on a large dataset.

---

## Features

- Case-insensitive medicine search  
- Automatic salt composition detection  
- Identification of all equivalent medicines  
- Price analysis including minimum, maximum, and average price  
- Highlights the cheapest and most expensive options  
- Displays affordable alternatives sorted by price  
- Efficient handling of a large dataset (220k+ records)

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
- CSV-based medicine dataset  

### Tools
- Git and GitHub  
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


