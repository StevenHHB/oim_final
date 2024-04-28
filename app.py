from flask import Flask, render_template, request, redirect, jsonify
from transformers import pipeline
from db import init_db, add_entry, get_entries
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'i_love_oim_and_professor_li'
classifier = pipeline('sentiment-analysis',
                      model='distilbert-base-uncased-finetuned-sst-2-english')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form['text']
        if not text.strip():
            return render_template('index.html', error="Please enter some text.")
        result = classifier(text)[0]
        add_entry(text, result['label'], float(
            result['score']), datetime.now().strftime('%Y-%m-%d'))
        return redirect('/')
    entries = get_entries()
    return render_template('index.html', entries=entries)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/api/events')
def events():
    entries = get_entries()
    events = [{'title': f"{entry['sentiment']} - {entry['score']}",
               'start': entry['date']} for entry in entries]
    return jsonify(events)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
