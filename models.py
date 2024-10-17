from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Модель спортсмена
class Athlete(Base):
    __tablename__ = 'athletes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(Enum('male', 'female', name='gender_type'))
    country = Column(String)
    birthdate = Column(Date)

    participations = relationship('Participation', back_populates='athlete')

# Модель Олимпийских игр
class OlympicGame(Base):
    __tablename__ = 'olympic_games'

    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    season = Column(Enum('summer', 'winter', name='season_type'))
    country = Column(String)
    city = Column(String)

    events = relationship('Event', back_populates='olympic_game')

# Модель события
class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    sport_name = Column(String)
    event_name = Column(String)
    venue = Column(String)
    event_date = Column(Date)

    olympic_game_id = Column(Integer, ForeignKey('olympic_games.id'))
    olympic_game = relationship('OlympicGame', back_populates='events')

    participations = relationship('Participation', back_populates='event')

# Модель участия
class Participation(Base):
    __tablename__ = 'participations'

    id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.id'))
    event_id = Column(Integer, ForeignKey('events.id'))
    rank = Column(Integer)  # 1 - Gold, 2 - Silver, 3 - Bronze
    team_event = Column(Integer)  # 0 - Individual, 1 - Team

    athlete = relationship('Athlete', back_populates='participations')
    event = relationship('Event', back_populates='participations')