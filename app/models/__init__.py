from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager
db = SQLAlchemy()

class Model(db.Model):
    __abstract__ = True
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    """ Method to insert or update model"""
    def save(self):
        if self.id is None:
            db.session.add(self)
        else:
            db.session.merge(self)

        db.session.commit()
        db.session.flush()

    """ Method delete model """

    def delete(self) -> bool:
        try:
            if self.id is not None:
                db.session().delete(self)
                db.session().commit()

            return True

        except Exception as exception:
            return False

    def fill(self, attrs: dict):
        for item in attrs.keys():
            setattr(self, item, attrs[item])



@contextmanager
def transaction():
    session = db.session()
    try:
        yield session
        session.flush()
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()