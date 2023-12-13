Welcome to the Restaurant Review System project! This system allows users to leave reviews for restaurants. It's implemented using SQLAlchemy, a powerful and flexible Object Relational Mapper (ORM) for Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone
   cd restaurants

    Create a virtual environment:

    bash
   ```

python -m venv venv

Activate the virtual environment:

    On Windows:

    bash

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install dependencies:

bash

pip install -r requirements.txt

Configure your database connection:

    Open migrations/alembic.ini and set your database connection URL.

Apply migrations:

bash

    alembic upgrade head

Usage

    Run the seeds script to populate the database with sample data:

    bash

    python seeds.py

    Interact with the models using the interactive Python shell or your application code.

Project Structure

Features
Object Relationship Methods
Review Class

    customer(): Returns the Customer instance for this review.
    restaurant(): Returns the Restaurant instance for this review.

Restaurant Class

    reviews(): Returns a collection of all the reviews for the restaurant.
    customers(): Returns a collection of all the customers who reviewed the restaurant.

Customer Class

    reviews(): Returns a collection of all the reviews left by the customer.
    restaurants(): Returns a collection of all the restaurants reviewed by the customer.

Aggregate and Relationship Methods
Customer Class

    full_name(): Returns the full name of the customer, with the first name and the last name concatenated in Western style.
    favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
    add_review(restaurant, rating): Adds a new review for the specified restaurant with the given rating.
    delete_reviews(restaurant): Removes all reviews for a specific restaurant.

Review Class

    full_review(): Returns a formatted string for the review.

Restaurant Class

    fanciest() (class method): Returns one restaurant instance with the highest price.
    all_reviews(): Returns a list of strings with all reviews for the restaurant.

Contributing

Contributions are welcome! Please follow the Contributing Guidelines.
License

This project is licensed under the MIT License.
