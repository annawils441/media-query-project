from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')

@app.route('/events')
def events_page():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)