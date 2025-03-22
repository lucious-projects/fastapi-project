from sqlalchemy import Column, Integer, String, ForeignKey, Table # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from .database import Base

workout_routine_association = Table (
    'workout_routine', Base.metadata,
    Column ('workout_id', Integer, ForeignKey ('workouts.id')),
    Column ('routine_id', Integer, ForeignKey ('routines.id'))
)

class User (Base):
    __tablename__ = 'users'
    id = Column (Integer, primary_key=True, index=True)
    username = Column (String, unique=True, index=True)
    email = Column (String, unique=True, index=True)
    password = Column (String)
class Workout(Base):
    _tablename__ = 'workouts'
    id = Column (Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, index=True)
    description = Column(String, index=True)
    user = relationship('User', back_populates='workouts')
    workouts = relationship('Routine', secondary=workout_routine_association, back_populates='routines')

    workouts.routines = relationship('Routine', secondary=workout_routine_association, back_populates='workouts')