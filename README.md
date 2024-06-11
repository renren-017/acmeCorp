# Acme Corp API Development Task 🚀

## Introduction 📘

This documentation details the backend development task assigned by Acme Corp, a rapidly growing startup specializing in innovative supply chain management software. The task involves developing a series of API endpoints for product management in a web application.

## Setup and Installation 🛠️

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:renren-017/acmeCorp.git

2. Install dependencies via Docker Compose:
    ```bash
    docker-compose build

3. Start the Docker services running!:
    ```bash
    docker-compose up -d

## How to Test the APIs 🔍
    docker-compose exec web python manage.py test


## Q & A

### Q1: What technologies were used for the project development?
**A1:** This project was developed using Django REST Framework for the backend along with drf-yasg for generating OpenAPI documentation. For the admin interface, Jazzmin Admin Panels were utilized. The entire project deployment including the database, Redis handling, and the web server was containerized using Docker.

### Q2: How do you ensure robust and effective responses in the API?
**A2:** Caching was specifically implemented to enhance the responsiveness and efficiency of the product list views. This approach helps in serving repeated requests faster by reducing database load.

### Q3: What method of authentication is used in this project?
**A3:** For security measures, JWT (JSON Web Token) authentication was employed to secure the API endpoints and ensure that only authenticated users can access certain functionalities.

### Q4: What additional models were created to enhance the functionality of the API?
**A4:** To address the complexity and requirements of the project, models such as Location, Manufacturer, Category, and Currency Rate were created. These models help in organizing the data effectively and provide a more feasible structure to the API.

### Q5: What features support the ease of use of the API?
**A5:** The API is designed to support filtering, searching, and ordering backends. These features make it user-friendly by allowing users to easily navigate through and interact with the API data.

### Q6: How is the product filtering by price managed considering different currencies?
**A6:** To handle product filtering by price across different currencies, a `price_sort` field is maintained which always stores the product price in USD. This standardization allows for consistent and reliable ordering and filtering by price irrespective of the original currency of a product.



## Screenshots 📸

![Image of Open Api Main Page](screenshots%2FScreenshot%202024-06-11%20at%2013.56.46.png)

![Catogories List API](screenshots%2FScreenshot%202024-06-11%20at%2013.57.07.png)

![Manufacturers List API](screenshots%2FScreenshot%202024-06-11%20at%2013.57.20.png)

![Manufacturer Details API](screenshots%2FScreenshot%202024-06-11%20at%2013.57.46.png)

![Products List API](screenshots%2FScreenshot%202024-06-11%20at%2013.57.59.png)

![Products List API Results](screenshots%2FScreenshot%202024-06-11%20at%2013.58.21.png)

![Authentication via JWT API](screenshots%2FScreenshot%202024-06-11%20at%2013.58.43.png)

![Admin panel main page](screenshots%2FScreenshot%202024-06-11%20at%2014.10.37.png)

![Admin panel products list](screenshots%2FScreenshot%202024-06-11%20at%2014.11.17.png)

![Admin panel products filtering results](screenshots%2FScreenshot%202024-06-11%20at%2014.10.30.png)

## Video Description of Work 🎥

Access only for AIU
[https://drive.google.com/drive/u/1/folders/1ZozxEzt4BXG2Suo224fgj-bqg0ejxzXq](https://drive.google.com/drive/u/1/folders/1ZozxEzt4BXG2Suo224fgj-bqg0ejxzXq)