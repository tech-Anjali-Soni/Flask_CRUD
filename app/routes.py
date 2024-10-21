from flask import Blueprint, render_template, redirect, url_for,request,flash              
from .models import Student
from .forms import  StudentForm, SearchForm
from . import db
from fpdf import FPDF
main = Blueprint('main',__name__)
@main.route('/')
def index():
    form  = SearchForm()
    students = Student.query.all()
    return render_template('index.html',students=students, form=form)
@main.route('/add',methods=['GET','POST'])
def add_student():
    form = StudentForm()
    if  form.validate_on_submit():
        new_student = Student(rollno=form.rollno.data,
            name = form.name.data, feesamount=form.feesamount.data,
            paymentmode = form.paymentmode.data)
        db.session.add(new_student)
        db.session.commit()
        flash("Student added successfully!", "success")
        return redirect(url_for('main.index'))
    return render_template('add_update.html',form=form,title="Add Student")

@main.route('/update/<int:id>',methods =  ['GET','POST'])
def update_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if  form.validate_on_submit():
        student.rollno = form.rollno.data
        student.name = form.name.data
        student.feesamount = form.feesamount.data
        student.paymentmode = form.paymentmode.data
        db.session.commit()
        flash("Student updated successfully!","success")
        return redirect(url_for('main.index'))
    return render_template('add_update.html',form=form,title="Update Student")
@main.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted successfully!","danger")
    return redirect(url_for("main.index"))
@main.route('/search',methods=["POST"])
def search_student():
    form = SearchForm()
    search_term = form.search.data
    students = Student.query.filter((Student.rollno.contains(search_term))|(Student.name.contains(search_term))). all()
    return render_template('index.html', students=students, form=form)
@main.route('/export')
def export_to_pdf():
    students = Student.query.all()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt='Student Records', ln=True, align="C")
    for student in students:
        pdf.cell(200, 10, txt = f"{student.rollno} - {student.name} - {student.feesamount} - {student.paymentmode}", ln=True)
        pdf_file = "students_report.pdf"
        pdf.output(pdf_file)
        return redirect(url_for('main.index'))