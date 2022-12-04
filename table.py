from dao.model.user import User
from setup_db import db

db.create_all()

user_danil = User(id=1, username="Danil", password="qwer12345", email="wafawrasg@mail.ru",
                  surname="Balakirev", role="admin", favorite_genre="comedy")

user_ivan = User(id=2, username="Ivan", password="12345qwert", email="zxvsdbdf@mail.ru",
                 surname="Rengar", role="user", favorite_genre="comedy")

db.session.add(user_danil)
db.session.add(user_ivan)

db.session.commit()
