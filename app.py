from flask import Flask, render_template, request, jsonify
from gpa import cgpa, sgpa, how_much

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_subjects = int(request.form['numSubjects'])
        grades_credits = []

        for i in range(num_subjects):
            grade = request.form[f'grade{i}']
            credit = int(request.form[f'credit{i}'])
            grades_credits.append([grade, credit])

        # Calculate CGPA
        result1 = cgpa(grades_credits)
        return jsonify(result=f"CALCULATED SGPA = {result1}")

    return render_template('index.html')

@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    num_subjects = int(request.form['numSubjectsMarks'])
    isa1 = []
    isa2 = []
    ass = []
    esa = []
    credits = []

    for i in range(num_subjects):
        isa1.append(int(request.form[f'isa1{i}']))
        isa2.append(int(request.form[f'isa2{i}']))
        ass.append(int(request.form[f'ass{i}']))
        esa.append(int(request.form[f'esa{i}']))
        credits.append(int(request.form[f'credit{i}']))

    marks = [isa1, isa2, ass, esa, credits]
    result2 = sgpa(marks)
    return jsonify(result=f"CALCULATED SGPA = {result2}")

@app.route('/how_much', methods=['POST'])
def how_much_marks():
    num_subjects = int(request.form['numSubjectsHowMuch'])
    isa1 = []
    isa2 = []
    ass = []
    credits = []

    for i in range(num_subjects):
        isa1.append(int(request.form[f'isa1{i}']))
        isa2.append(int(request.form[f'isa2{i}']))
        ass.append(int(request.form[f'ass{i}']))
        credits.append(int(request.form[f'credit{i}']))

    marks = [isa1, isa2, ass, credits]
    result3 = how_much(marks)
    return jsonify(result=f"MARKS NEEDED = {result3}")


