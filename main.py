from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


api = Api()
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db.init_app(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    videos = db.Column(db.Integer, nullable=False)

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

with app.app_context():
    db.create_all()


class Main(Resource):
    def get(self, id):
        course = db.get_or_404(Course, id)
        return course

    def delete(self, id):
        #course = db.get_or_404(Course, id)
        #db.session.delete(course)
        #db.session.commit()
        #return
        pass


    def put(self, id):
       pass


class MainList(Resource):
    def post(self):
        course = Course(
            name=request.form["name"],
            videos=request.form["videos"],
        )
        db.session.add(course)
        db.session.commit()
        course = db.session.query(Course)
        course = [x.as_dict for x in course.all()]
        return course

    def get(self):
        courses = db.session.query(Course)
        courses = [x.as_dict for x in courses.all()]
        return courses


api.add_resource(Main, "/api/courses/<int:id>")
api.add_resource(MainList, "/api/courses/")
api.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, port=3000, host="127.0.0.1")