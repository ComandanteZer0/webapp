from __future__ import print_function # In python 2.7
from flask import Flask, render_template ,jsonify,request
from sql import getShop,getUserData
import logging
import sys
app = Flask(__name__, template_folder='.')  

@app.route("/shop.html")
def shop():
   return render_template('assets/shop/shop.html')
@app.route('/profile/<username>')
def show_user_profile(username):
  app.logger.warning(username)
  data = getUserData(username)
  
  print(username, file=sys.stderr)
  return render_template('assets/profile/profile.html',user_id=data[0],balance=data[2],name=data[6])

@app.route('/data')
def data():
    tov = list(getShop())
    return jsonify(tov)
@app.route('/shop', methods=['POST'])
def login_post():
    data = request.json
    print(data, file=sys.stderr)

    return jsonify({
        'status': 'SUCCESS',
        'data': data,
    })
@app.route("/")  
def web():    
    
    return render_template('assets/main/главная.html')
if __name__ == "__main__":  
    app.run(debug=True, host="0.0.0.0", port='80')  