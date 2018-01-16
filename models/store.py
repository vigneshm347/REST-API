from db import db
class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('ItemModel', lazy = 'dynamic')
    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        # filter_by(filter1, filter2...filtern n)
        # it returns the data from database as an
        # ItemModel object. So it contains the object property
        # basically self.name, self.price
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):

        #code to insert a record basically an object
        #into the SQLLite database using SQLAlchemy
        #session here is the instance(object). We can add multiple
        #objects at once. When we retreive a record from the
        #database and then add it again. SQLAlchemy would update
        #the record instead of creating new one.

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        #deletes an object from the database

        db.session.delete(self)
        db.session.commit()