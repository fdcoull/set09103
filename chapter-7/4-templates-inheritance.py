from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inherits/')
def inherits():
    return render_template('4-templates-inheritance-base.html')

@app.route('/inherits/one')
def inherits_one():
        return render_template('4-templates-inheritance-content.html')

if __name__ == ("__main__"):
    app.run(host='0.0.0.0', debug=True)
