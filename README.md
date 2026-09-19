# 🏥 Hospital Resource Intelligence

An end-to-end **hospital resource analytics and booking platform** that combines an interactive **Power BI dashboard** with a **Streamlit web application** to help users understand hospital resource availability and book available beds or ambulances.

The project integrates data analytics, database management, visualization, and web application development into a single platform.

---

## 📌 Problem Statement

Finding and comparing hospital resources can be difficult because information such as:

- Available beds
- ICU availability
- Doctor availability
- Ambulance availability
- Operation theatre availability
- Treatment costs
- Discounts

is often scattered across different sources.

Patients and their attendants may have difficulty identifying hospitals with suitable resources, while hospital resource information can be difficult to analyze in a centralized manner.

This project addresses this problem by creating a centralized platform where hospital resource data can be **stored, analyzed, visualized, and accessed through a simple web interface**.

---

## 🎯 What Does This Project Solve?

The Hospital Resource Intelligence platform solves two major problems:

### 1. Hospital Resource Visibility

The Power BI dashboard provides an interactive overview of hospital resources and allows users to compare hospitals and cities based on factors such as:

- Total hospitals
- Available beds
- ICU beds
- Doctors on duty
- Available ambulances
- Operation theatres
- Treatment costs
- Discounts
- Ambulance availability
- Doctor availability
- OT availability

Users can interact with the dashboard using filters such as **city and hospital-related attributes** to explore the available data.

### 2. Resource Booking

The Streamlit application provides a simple booking interface through which users can:

- Select a city
- Select a hospital
- Choose a resource type
- Check available beds
- Book beds
- Check available ambulances
- Book an ambulance
- Receive a booking ID after successful booking

The database is updated after a successful booking so that resource availability reflects the booking.

---

# 💡 How the Project Solves the Problem

The project follows an end-to-end architecture:


Hospital Data
     │
     ▼
   MySQL
     │
     ├──────────────────┐
     │                  │
     ▼                  ▼
 Power BI            Streamlit
 Dashboard           Application
     │                  │
     ▼                  ▼
Resource Analysis   Resource Booking
     │                  │
     └──────────┬───────┘
                ▼
        Updated MySQL Data

Data Storage

Hospital information and resource information are stored in a structured MySQL database.

The database contains tables for resources such as:

Hospitals
Departments
Doctors
Beds
ICUs
Ambulances
Emergency resources
Operation theatres
Bookings


Data Analytics

Power BI connects to the hospital data and transforms it into interactive dashboards and visualizations.

This allows users to understand resource availability and compare hospitals and cities.

Web Application

The Streamlit application provides a user-friendly interface for interacting with the database.

When a user books a resource, the application updates the corresponding database records.



🎯 Target Audience

The project is designed primarily for:

👨‍👩‍👧 Patients & Attendants

Users who want to explore hospital resources and check the availability of beds or ambulances before making a booking.

🏥 Hospital & Healthcare Staff

The dashboard can help healthcare staff or administrators understand resource distribution and availability across hospitals.

📊 Data Analysts

The Power BI dashboard provides a practical environment for analyzing healthcare resource data and identifying patterns across hospitals and cities.

🎓 Students & Researchers

The project demonstrates how data analytics, databases, visualization, and web applications can be combined to build a real-world data-driven system.


🛠️ Tech Stack
Programming Language
Python

Used for:

Application development
Database interaction
Backend logic
Resource booking operations
Web Application
Streamlit

Used to build the interactive web application.

The application contains:

Dashboard page
Booking page
Bed booking interface
Ambulance booking interface
Database
MySQL

Used as the central relational database for storing:

Hospital information
Department information
Doctor availability
Bed information
ICU information
Ambulance information
Emergency resources
Operation theatres
Booking records
Data Visualization
Microsoft Power BI

Used to build the interactive hospital resource intelligence dashboard.

The dashboard provides KPIs and visualizations for:

Hospital availability
Bed availability
ICU availability
Doctor availability
Ambulance availability
OT availability
Treatment costs
Discounts
City-wise comparisons
Deployment
GitHub

Used for:

Source code management
Version control
Project hosting
Streamlit Community Cloud

Used to deploy the Streamlit application and make it accessible through the web.

Aiven

Used to host the MySQL database remotely so that the deployed Streamlit application can access the database instead of relying on a local MySQL server


🌟 Key Features
📊 Interactive Power BI hospital analytics dashboard
🏥 Hospital-wise and city-wise resource analysis
🛏️ Bed availability tracking
🚑 Ambulance availability tracking
👨‍⚕️ Doctor availability analysis
🏥 ICU availability analysis
🏗️ Operation theatre availability
💰 Treatment cost and discount analysis
📝 Bed booking system
🚑 Ambulance booking system
🔄 Database updates after bookings
🆔 Automatic booking ID generation
☁️ Cloud deployment
🔐 Secure database credentials using Streamlit Secrets


Future Improvements

Potential future improvements include:

🔐 User authentication and login
💳 Online payment integration
❌ Booking cancellation
📧 Booking confirmation notifications
🤖 AI-powered hospital/resource assistant
📍 Location-based hospital recommendations
📱 Improved mobile responsiveness
📈 Advanced predictive analytics for resource demand
👨‍💼 Separate hospital-admin dashboard
📊 More advanced resource forecasting


🔗 **Live Demo**

https://hospital-resource-intelligence-bhwrms6wkjirznongmwnko.streamlit.app/Booking
