from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)




@app.route('/')
def index():
    task_list = Task.query.all()
    print(task_list)
    return render_template('base.html')


if __name__ == '__main__':
     db.create_all()

     new_Task = Task(title="task 1", complete=False)
     db.session.add(new_Task)
     db.session.commit()
     app.run(debug=True)
