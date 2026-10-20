# Cars Dealership - Full-Stack Cloud Application

**Repository Name:** `xrwvm-fullstack_developer_capstone`  
**Project Name:** Cars Dealership Full-Stack Cloud Application  
**Author:** Yash Mohite  

---

## Project Overview

The **Cars Dealership** application is a comprehensive full-stack cloud web application developed for a national car retailer in the United States. The platform enables prospective car buyers to browse nationwide dealerships, filter dealerships by state, inspect detailed dealership profiles, view real customer reviews enhanced with sentiment analysis, and submit reviews for vehicles.

---

## Architectural Components

1. **Frontend:**
   - **React.js & HTML5 / CSS3 / Bootstrap 5**: Responsive single-page application (SPA) providing dynamic dealer search, state-level filtering, review submission forms, user registration, and authentication views.
   - **Static Pages**: Informative pages including `About Us` and `Contact Us` served by Django.

2. **Backend Services:**
   - **Django Web Framework**: Handles user session management, authentication (Sign-up, Login, Logout), car make/model inventory models, and acts as an API gateway communicating with downstream microservices.
   - **SQLite Database**: Persists car inventory (Car Make, Car Model, Year, Type).
   - **Django Admin Portal**: Administrative interface for managing makes, models, and registered users.

3. **Microservices:**
   - **Node.js / Express / MongoDB Data Microservice**: Manages dealership listings and user reviews with high scalability.
   - **Flask & NLTK Sentiment Analysis Microservice**: Evaluates user reviews with Natural Language Toolkit (NLTK) SentimentIntensityAnalyzer to classify feedback as positive, negative, or neutral.

4. **CI/CD & Cloud Deployment:**
   - **GitHub Actions**: Continuous Integration pipeline running automated linting, test execution, and container building.
   - **Docker & IBM Cloud Code Engine / Kubernetes**: Microservices containerized with Dockerfiles and deployed to IBM Cloud Code Engine.

---

## Technologies Used

- **Languages:** Python 3.10+, JavaScript (ES6+), HTML5, CSS3, SQL
- **Frameworks & Libraries:** Django 4+, React 18, Express.js 4, Flask 2, NLTK, Bootstrap 5
- **Databases:** MongoDB, SQLite3
- **Containerization & Cloud:** Docker, Docker Compose, IBM Cloud Code Engine, Kubernetes
- **DevOps:** GitHub Actions, Git
