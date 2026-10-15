from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CSE30040 - Cloud Computing and DevOps</h1>
    <h2>Experiment 5: CI/CD with Jenkins</h2>
    <p>Flask application deployed using Docker on AWS EC2.</p>
    <p>Status: Running successfully!</p>
    <p>Version: 1</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
