from flask import Flask, render_template  
  
app = Flask(__name__, template_folder='.')  
  
@app.route("/")  
def web():  
    return render_template('WebApp.html')  
  
if __name__ == "__deploy__":  
    app.run(debug=True, host="0.0.0.0", port='80')  