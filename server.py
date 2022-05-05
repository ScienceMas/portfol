from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email} , {subject} , {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database, delimiter=',',
                              quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email, subject, message])


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':

        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thank.html')
    else:
        return 'somthing went wrong.try again'
