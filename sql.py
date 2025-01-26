import sqlite3
import asyncio
import config
class Database:
	def __init__(self, db_name):
		self.connection = sqlite3.connect(db_name)
		self.cursor = self.connection.cursor()
	def add_user(self, user_id):
		with self.connection:
			self.cursor.execute("INSERT INTO `user_data` ('user_id') VALUES (?)", (user_id,))

	def user_exists(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,)).fetchmany(1)
			return bool(len(result))
	def checkRules(self, user_id):
		with self.connection:
			result = self.cursor.execute("SELECT rules FROM user_data WHERE user_id = ?", (user_id,)).fetchmany(1)
			return bool(result[0][0])
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT user_id FROM "user_data"').fetchall()
	def set_rules(self,status,user_id):
		with self.connection:
			return self.cursor.execute("UPDATE user_data SET rules = ? WHERE user_id = ?", (status,user_id))

def getShop():
	connection = sqlite3.connect(config.name)
	cursor = connection.cursor()
	with connection:
		resp = cursor.execute('SELECT * FROM "shop_data"').fetchall()
		cursor.close()
		return resp
def getUserData(user_id):
	connection = sqlite3.connect(config.name)
	cursor = connection.cursor()
	with connection:
		resp = cursor.execute("SELECT * FROM user_data WHERE user_id = ?", (user_id,)).fetchmany(1)
		cursor.close()
		return resp[0]
	
		