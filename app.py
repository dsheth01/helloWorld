from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Dev Sheth! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite_course')
def favorite_course():
    print('Subject: ' + request.args.get('subject'))
    print('Course Number: ' + request.args.get('course_number'))
    return render_template('favorite_course.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()


'''     print('First Name entered: ' + request.args.get('first_name'))
        print('Last Name entered: ' + request.args.get('last_name'))
        print('Email entered: ' + request.args.get('email'))
        print('Phone Number entered: ' + request.args.get('phone'))

        if request.get.form('agree_check'):
            print('Agree to be contacted entered' + request.args.get('phone'))'''