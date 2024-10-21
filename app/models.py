from . import db
from datetime import datetime
class Student(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    rollno = db.Column (db.String(20),unique = True, nullable =False)
    name = db.Column (db.String(100),nullable=False)
    feesamount = db.Column (db.Float,nullable=False)
    dated = db.Column(db.DateTime, default = datetime.utcnow)
    paymentmode = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f'<Student {self.name}>'
