from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():

    title = "<h1>The Zen of Python</h1>"
    content = "<h3>{}</h3>".format(random.choice(app.config['output_lines']))

    return title + content


def get_output_lines(file_name):

    with open(file_name, 'r') as f:
        file_lines = f.readlines()
        output_lines = [line.rstrip("\n") for line in file_lines if line.rstrip("\n")]
        app.config['output_lines'] = output_lines


if __name__ == '__main__':

    get_output_lines('the-zen-of-python.txt')
    app.run("127.0.0.1", port=5000)  # run in the localhost
