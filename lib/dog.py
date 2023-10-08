from models import Dog

def create_table(base, engine):
    """Creates the Dog table in the database."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Saves a Dog object to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Returns a list of all Dog objects in the database."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Returns the first Dog object with the given name."""
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    """Returns the Dog object with the given ID."""
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    """Returns the first Dog object with the given name and breed."""
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    """Updates the breed of the given Dog object."""
    dog.breed = breed
    session.commit()
