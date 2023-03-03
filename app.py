from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'SDE',
  'location': 'Japan',
  'salary': 1000
}, {
  'id': 2,
  'title': 'PM',
  'location': 'India',
  'salary': 5000
}, {
  'id': 3,
  'title': 'Data-Analyst',
  'location': 'China',
  'salary': 8000
}]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS)
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
