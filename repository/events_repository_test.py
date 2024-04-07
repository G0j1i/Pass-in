import sys
sys.path.append("C:\\Users\\Goji\\VScode\\NLWUnite")
import pytest
from src.models.settings.connection import db_connection_handler
from src.models.repository.events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New database registry")
def test_insert_event():
    event = {
        "uuid": "uuid-yo",
        "title": "title here",
        "slug": "slug-here",
        "maximum_attendees": "20"
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

def test_get_event_by_id():
    event_id = "uuid-yo"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
