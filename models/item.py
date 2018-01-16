from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

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