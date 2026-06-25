# First Django Project

A simple web application built with Django. This project focuses on providing a robust framework for developing dynamic web applications with a clear emphasis on the MVT architecture.

## Features

- User management
- Registration and login
- Create, edit, and delete content
- Admin panel for managing users and content

## Installation

1. **Install virtualenv**:
   First, ensure that `virtualenv` is installed. You can install it using:

   ```bash
   pip install virtualenv
   ```

2. **Create a virtual environment**:
   After installing `virtualenv`, create a new virtual environment by running:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   To install necessary dependencies, use the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

5. **Run the development server**:
   After installing the dependencies, run the development server with:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Visit `http://127.0.0.1:8000/` in your web browser to see the website in action.

## Contributing

Feel free to fork the repository and submit a pull request for contributions!

## License

This project is licensed under the MIT License. 
The MIT License is a permissive free software license that allows for reuse within proprietary software, as long as all copies include the original license.