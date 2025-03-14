# Movie Database Project

This project is a simple movie database application that uses PostgreSQL to store and manage movie records. It provides a text-based interface for users to interact with the database, allowing them to add movies, update ticket counts, book tickets, and retrieve movie records.

## Project Structure

```
movie-database-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── db
│   │   ├── __init__.py  # Initializes the database module
│   │   └── models.py    # Defines the database schema and interaction functions
│   ├── cli
│   │   ├── __init__.py  # Initializes the command-line interface module
│   │   └── interface.py  # Implements the text-based interface for user interaction
├── requirements.txt      # Lists the project dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd movie-database-project
   ```

2. **Install dependencies**:
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**:
   Ensure you have PostgreSQL installed and running. Create a database for the project and update the database connection settings in the `src/db/models.py` file.

4. **Run the application**:
   Start the application by running:
   ```
   python src/main.py
   ```

## Usage Examples

- To add a new movie, follow the prompts in the interface.
- You can increment watch counts and book tickets through the provided options.
- List all movies to see the current records in the database.

## Additional Information

This project is designed for educational purposes and can be extended with more features such as user authentication, advanced search capabilities, and a graphical user interface. Contributions and improvements are welcome!