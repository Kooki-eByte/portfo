from flask import Flask, render_template, send_from_directory, request, url_for, redirect
import csv


app = Flask(__name__)


@app.route('/')
def my_home_page():
	return render_template('index.html')


# @app.route('/index.html')
# def my_home_page2():
# 	return render_template('index.html')


# @app.route('/works.html')
# def my_works_page():
# 	return render_template('works.html')


# @app.route('/about.html')
# def about_me_page():
# 	return render_template('about.html')


# @app.route('/contact.html')
# def contact_page():
# 	return render_template('contact.html')

# This is the dynamic version of getting html files so we don't have to keep copy and pasting this code above.
@app.route('/<get_html>')
def portfolio_page(get_html):
	return render_template(get_html)


def write_to_file(data):
	with open('database.txt', mode='a') as db:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = db.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	with open('database.csv', mode='a', newline='') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not send to database...'
	else:
		return 'Something went wrong...'


