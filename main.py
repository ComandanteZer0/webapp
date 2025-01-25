from flask import Flask, render_template  
from config import url
app = Flask(__name__,template_folder='.')  
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/")  
def web():  

    return render_template(url)  
  
if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')  