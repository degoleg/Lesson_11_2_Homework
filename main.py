from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route("/")
def index():
    candidates = utils.get_candidates_all()
    return render_template('list.html', candidates=candidates)

@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate(pk)
    return render_template('card.html', candidate=candidate)


if __name__ == '__main__':
    app.run(debug=True)
