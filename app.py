# save this as app.py
from flask import Flask,render_template,jsonify
from database import fetch_jobs

app = Flask(__name__)


@app.route("/")
def hello():
    jobs=fetch_jobs()
    return render_template('home.html',jobs=jobs)

@app.route('/api/jobs')
def jobs_list():
    jobs=fetch_jobs()
    return jsonify(jobs)


if __name__=="__main__":
    app.run()