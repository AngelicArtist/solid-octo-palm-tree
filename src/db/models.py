from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, Sequence('movie_id_seq'), primary_key=True)
    title = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(50))
    tickets_sold = Column(Integer, default=0)

def get_session(database_url):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def add_movie(session, title, director, year, genre):
    new_movie = Movie(title=title, director=director, year=year, genre=genre)
    session.add(new_movie)
    session.commit()

def update_tickets(session, movie_id, count):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie:
        movie.tickets_sold += count
        session.commit()

def get_movies(session):
    return session.query(Movie).all()

def initialize_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) UNIQUE,
            tickets_available INT
        )
    """)
    conn.commit()
    cursor.close()