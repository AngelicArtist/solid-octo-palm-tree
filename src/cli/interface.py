import mysql.connector
# The display_menu function displays the main menu of the program.
def display_menu():
    print("Welcome to the Movie Database!")
    print("1. Add a Movie")
    print("2. List Movies")
    print("3. Increment Watch Count")
    print("4. Book Tickets")
    print("5. Exit")
# The get_user_choice function prompts the user to enter their choice and returns it.
def get_user_choice():
    choice = input("Please enter your choice: ")
    return choice
# The add_movie_interface function prompts the user to enter the movie title and the number of tickets available, and adds the movie to the database.
def add_movie_interface(conn):
    title = input("Enter movie title: ")
    tickets = int(input("Enter number of tickets available: "))
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO movies (title, tickets_available) VALUES (%s, %s)", (title, tickets))
        conn.commit()
        print("Movie added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
# The list_movies_interface function lists all the movies in the database along with the number of tickets available.
def list_movies_interface(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT title, tickets_available FROM movies")
    for (title, tickets_available) in cursor:
        print(f"{title}: {tickets_available} tickets available")
    cursor.close()
# The increment_watch_count_interface function prompts the user to enter the movie title and increments the number of tickets available for that movie.
def increment_watch_count_interface(conn):
    title = input("Enter movie title: ")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE movies SET tickets_available = tickets_available + 1 WHERE title = %s", (title,))
        conn.commit()
        print("Tickets incremented successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()

def book_tickets_interface(conn):
    title = input("Enter movie title: ")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE movies SET tickets_available = tickets_available - 1 WHERE title = %s AND tickets_available > 0", (title,))
        if cursor.rowcount == 0:
            print("No tickets available or movie not found.")
        else:
            conn.commit()
            print("Ticket booked successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
# The start_interface function is the main entry point for the text-based interface. It displays the main menu and calls the appropriate functions based on the user's choice.
def start_interface(conn):
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            add_movie_interface(conn)
        elif choice == '2':
            list_movies_interface(conn)
        elif choice == '3':
            increment_watch_count_interface(conn)
        elif choice == '4':
            book_tickets_interface(conn)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='********',
        database='app'
    )
    start_interface(conn)