# save this as app.py
from flask import Flask,render_template,jsonify,request
from database import fetch_jobs,fetch_job

app = Flask(__name__)


@app.route("/")
def home():
    jobs=fetch_jobs()
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')
def jobs_list():
    jobs=fetch_jobs()
    return jsonify(jobs)

@app.route('/job/<id>')
def get_job_detail(id):
    job=fetch_job(id)
    return render_template('job_detail.html',job=job)

@app.route('/job/<id>/apply',methods=['post'])
def submit_details(id):
    data=request.form
    job=fetch_job(id)
    return render_template('submitted.html',job=job,application=data)


if __name__=="__main__":
    app.run()