---

# MVT Test Project

This project is a dynamic web application built with Django, demonstrating key features like a robust backend, dynamic content management, and a functional contact form.

---

## Features

* **Django MVT Architecture:** The backend of this website is developed using Django's Model-View-Template (MVT) architectural pattern, ensuring a clear separation of concerns for data handling, business logic, and presentation.
* **Dynamic Content Management:** All content on the website is fully dynamic. This means you can easily update and manage all website content directly from the Django administration panel without needing to write or modify any code.
* **Contact Us Form:** The website includes a "Contact Us" form, allowing users to send messages directly. Submissions from this form are automatically sent to the administrator's email address, ensuring prompt communication.
* **Responsive Design:** The project utilizes a responsive design, ensuring an optimal viewing experience across various devices, from desktops to mobile phones. (This was inferred based on typical web development practices and the general expectation for modern websites.)
* **Database Integration:** The project uses Django's ORM (Object-Relational Mapping) to interact with a database, making data management efficient and straightforward. (This is a core aspect of Django's MVT.)

---

## Technologies Used

* **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
* **HTML, CSS, JavaScript:** For the front-end structure, styling, and interactivity.
* **SQLite (Default Django Database):** For database management during development. (You can specify if you're using a different database like PostgreSQL or MySQL if applicable).

---

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, follow these steps.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HuseynliIlqar/mvt-test.git
    cd mvt-test
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt` after installing your project's dependencies).

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin panel access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your admin user credentials.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    The application will be accessible at `http://127.0.0.1:8000/`. You can access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.

---

## Contributing

If you'd like to contribute to this project, please feel free to fork the repository and submit pull requests.

---

## License

This project is open source and available under the [License Name] license. (Replace `[License Name]` with your chosen license, e.g., MIT, Apache 2.0).

---
