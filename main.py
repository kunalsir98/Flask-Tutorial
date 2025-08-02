from flask import Flask,render_template

app= Flask(__name__)

## Let us define the routes here 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aboutus')
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(host='127.0.0.1',port=5000)