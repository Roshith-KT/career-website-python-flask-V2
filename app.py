# save this as app.py
from flask import Flask,render_template,jsonify

app = Flask(__name__)

jobs=[
        {
            'id':1,
            'role':'DataScientist',
            'location':'Bengaluru,India',
            'Salary':'Rs. 15,00,000'
        },
        {
            'id':2,
            'role':'Data Analyst',
            'location':'Remote',
            'Salary':'Rs. 10,00,000'
        },
        {
            'id':3,
            'role':'Python Back-end Engineer',
            'location':'Bengaluru,India',
            'Salary':'Rs. 15,00,000'
        },
        {
            'id':4,
            'role':'Front-end Developer',
            'location':'Bengaluru,India',
            'Salary':'Rs. 15,00,000'
        },
    ]

@app.route("/")
def hello():
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')
def jobs_list():
    return jsonify(jobs)


if __name__=="__main__":
    app.run()