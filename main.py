from flask import Flask, render_template  
  
app = Flask(__name__, template_folder='.')  
  
@app.route("/")  
def web():  
    return render_template('WebApp.html')  
  
if __name__ == "__main__":  
    app.run(debug=True, host="127.0.0.1", port='80')  