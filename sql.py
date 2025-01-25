import sqlite3
import asyncio
import json

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
	def get_users(self):
		with self.connection:
			return self.cursor.execute('SELECT user_id FROM "user_data"').fetchall()
		
