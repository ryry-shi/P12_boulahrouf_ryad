from sqlalchemy import URL, create_engine, func
from sqlalchemy import String, Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import enum

Base = declarative_base()

url_object = URL.create(
    "mysql",
    username="root",
    password="password84!",
    host="localhost",
    database="epic",
)

engine = create_engine(url_object)
Session = sessionmaker(bind=engine)
session = Session()

class MyEnum(enum.Enum):
    one = "epic"
    two = "collaborateur"
    three = "management"

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column("name", Enum(MyEnum))

    def __repr__(self) -> str:
        return f" Utilisateurs, ({self.name!r})"
    
class Utilisateurs(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column("user_name", String(30), index=True)
    password = Column(String(30), index=True)
    email = Column("email_address", String(30), index=True)
    affiliation = Column(Integer)
    permission = Column(Integer, ForeignKey("organizations.id"))
    organization = relationship("Organization")
    

    def __repr__(self) -> str:
        return f" Utilisateurs, ({self.nom!r}{self.password!r},{self.email}, {self.affiliation},{self.permission},{self.organization})"

Base.metadata.create_all(bind=engine)
