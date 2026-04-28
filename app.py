from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  # change if needed
    database="hospital_db"
)

cursor = conn.cursor()

# HOME PAGE
@app.route('/')
def home():
    return render_template("index.html")

# ADD PATIENT
@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    disease = request.form['disease']

    cursor.execute(
        "INSERT INTO patients (name, age, disease) VALUES (%s, %s, %s)",
        (name, age, disease)
    )
    conn.commit()

    return redirect('/patients')

# VIEW PATIENTS
@app.route('/patients')
def view_patients():
    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()
    return render_template("patients.html", patients=data)

# RUN
if __name__ == "__main__":
    app.run(debug=True)