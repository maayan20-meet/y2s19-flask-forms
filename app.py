from databases import *
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template('add.html')

	else:
		add_student(request.form['student_name'], int(request.form['student_year']), False)
		return redirect(url_for('home'))

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete(student_id):
	delete_student_id(student_id)
	return render_template('home.html', students=query_all())

@app.route('/edit', methods=['GET', 'POST'])
def edit_entry():
	if request.method == 'GET':
		return render_template('edit.html')

	else:
		update_lab_status(int(request.form['student_id']), True)
		return redirect(url_for('display_student', student_id=request.form['student_id']))

if __name__ == '__main__':
    app.run(debug=True)
