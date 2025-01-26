from flask import Flask, render_template ,jsonify
from sql import getShop

app = Flask(__name__, template_folder='.')  

@app.route("/shop.html")
def shop():
   

   return render_template('assets/shop/shop.html')

@app.route('/data')
def data():
    tov = list(getShop())
    return jsonify(tov)
@app.route("/")  
def web():    
    return render_template('assets/main/главная.html')
if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')  