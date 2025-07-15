from flask import Flask, render_template, request, redirect, url_for
from assessment import assess_student
from questions import reasoning_questions, psychometry_questions

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        name = request.form['name']
        reasoning_score = 0
        psychometry_score = 0
        for i, q in enumerate(reasoning_questions):
            ans = request.form.get(f'reasoning_{i}', '').strip().lower()
            if ans == str(q['answer']).lower():
                reasoning_score += 1
        for i, q in enumerate(psychometry_questions):
            ans = request.form.get(f'psychometry_{i}', '').strip().lower()
            if ans == str(q['answer']).lower():
                psychometry_score += 1
        result = assess_student(reasoning_score, psychometry_score, len(reasoning_questions), len(psychometry_questions))
        students.append({'name': name, 'reasoning': result['reasoning'], 'psychometry': result['psychometry']})
        return redirect(url_for('dashboard'))
    return render_template('quiz.html', reasoning_questions=reasoning_questions, psychometry_questions=psychometry_questions)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
