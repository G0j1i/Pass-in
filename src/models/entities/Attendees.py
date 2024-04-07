from src.models.settings.base import Base
from sqlalchemy import Column, ForeignKey, String, Integer, ForeignKey, DateTime, func

class Attendees(Base): 
    __tablename__ = "attendees"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    event_id = Column(String, ForeignKey("events.id"))
    created_at = Column(DateTime, func.now())
    # attendees_event_id_fkey = Column()
