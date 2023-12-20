from models_users import Utilisateurs
from sqlalchemy import URL, create_engine, func
from sqlalchemy import String, Column, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

url_object = URL.create(
    "mysql",
    username="root",
    password="password84!",  # plain (unescaped) text
    host="localhost",
    database="epic",
)
engine = create_engine(url_object)

Session = sessionmaker(bind=engine)
session = Session()


class Epic_Client(Base):
    __tablename__ = "epic_client"

    id = Column(Integer, primary_key=True)
    nom = Column(String(30), unique=True, index=True)
    email = Column(String(30), unique=True, index=True)
    telephone = Column(String(30), unique=True, index=True)
    entreprise = Column(String(30))
    creation = Column(DateTime(timezone=True))
    maj_contact = Column(DateTime(timezone=True))
    contact = Column(String(30))

    def __repr__(self) -> str:
        return f"('Client D'Epic {self.nom!r}{self.email!r}{self.telephone!r}{self.entreprise!r}{self.creation!r}{self.maj_contact!r}{self.contact!r}')"


class Contrat(Base):
    __tablename__ = "contrat_user"

    id = Column(Integer, primary_key=True)
    information_id = Column(Integer, ForeignKey("epic_client.id"))
    contact = Column(String(30), index=True)
    prix = Column(Integer)
    rest_prix = Column(Integer)
    creation = Column(DateTime(timezone=True))
    status = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"(Contrat {self.information_id!r} {self.contact!r} {self.prix!r} {self.rest_prix!r} {self.creation!r} {self.status!r})"


class Evenement(Base):
    __tablename__ = "evenement_user"

    event_id = Column(Integer, primary_key=True, index=True)
    contrat_id = Column(Integer, ForeignKey("contrat_user.id"))
    client_name = Column(String(30), ForeignKey("epic_client.nom"))
    client_contact = Column(ForeignKey("epic_client.email"))
    event_start = Column(DateTime(timezone=True))
    event_end = Column(DateTime(timezone=True))
    support_contact = Column(String(30), ForeignKey(Utilisateurs.nom))
    location = Column(String(30), unique=True)
    attendes = Column(Integer)
    NOTES = Column(String(30), unique=True)

    def __repr__(self) -> str:
        return f" Evenement {self.client_name},{self.client_contact},{self.location},{self.event_start!r},{self.event_end!r}"



Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

