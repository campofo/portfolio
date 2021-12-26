from flask import Flask, render_template,request,redirect

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_html(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.csv', mode="a")as database:
        email= data['email']
        subject = data['subject']
        message= data['message']
        file = database.writelines(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong"



