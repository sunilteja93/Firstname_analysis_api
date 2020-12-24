import re
import random
import mysql.connector as mysql
from datetime import datetime

class Utils():
	
	## Nickname generator
	def nickname(self, name):
		first_letter = name[0][0]
		three_letters = name[1][0:3]
		number = '{:03d}'.format(random.randrange (1,999))
		nickname = "".join([first_letter, three_letters, str(number)])
		
		## Return nickname
		print(nickname)
		return nickname

	## Random traits selector from Mysql table	
	def random_traits(self):
		try:	
			db = mysql.connect(
			host = "50.62.209.2",
			user = "user_analysis",
			passwd = "7gz0I%5j",
			database = "firstname_analysis"
			)
			cursor = db.cursor()

			## executing the statement using 'execute()' method
			sql = "SELECT trait_summary,id FROM personality_traits_tb WHERE last_fetched_timestamp < DATE_SUB(NOW(),INTERVAL 1 MINUTE) ORDER BY RAND() LIMIT 1"
			cursor.execute(sql)

			row = cursor.fetchone()
			self.update_last_fetched_timestamp(row[1])		
			## Return random row data
			print(row)
			return row
		except Exception as e:
			print(e)
			
	## To update the last fetched timestamp 	
	def update_last_fetched_timestamp(self, id):
		try:
			db = mysql.connect(
			host = "50.62.209.2",
			user = "user_analysis",
			passwd = "7gz0I%5j",
			database = "firstname_analysis"
			)
			cursor = db.cursor()

			## executing the statement using 'execute()' method
			now = datetime.now();
			sql = "UPDATE personality_traits_tb SET last_fetched_timestamp=%s WHERE id=%s"
			cursor.execute(sql, (now, int(id)))
			db.commit()	
		except Exception as e:
			print(e)	
		#finally:
		#	cursor.close()
		
	## Insert user_log	
	def insert_user_log(self, firstname, month, day, summary, trait_id):
		try:
			db = mysql.connect(
			host = "50.62.209.2",
			user = "user_analysis",
			passwd = "7gz0I%5j",
			database = "firstname_analysis"
			)
			cursor = db.cursor()

			## executing the statement using 'execute()' method
			sql = "INSERT INTO user_log_tb (username, month, day, trait_summary, trait_id) VALUES(%s, %s, %s, %s, %s)"
			cursor.execute(sql, (firstname,int(month),day, summary, trait_id))
			db.commit()	
		except Exception as e:
			print(e)
		#finally:
		#	cursor.close()			
	
	## Check if the data exists
	def check_data_exists(self, firstname, month, day):
		try:
			db = mysql.connect(
			host = "50.62.209.2",
			user = "user_analysis",
			passwd = "7gz0I%5j",
			database = "firstname_analysis"
			)
			cursor = db.cursor()

			## executing the statement using 'execute()' method
			sql = "SELECT trait_summary,id FROM user_log_tb where username=%s and month =%s and day=%s"
			cursor.execute(sql, (firstname,int(month),day))

			## 'fetchall()' method fetches all the rows from the last executed statement
			row = cursor.fetchone() ## it returns the random selected data
			
			if row == None:
				print("There are no results for this query")
			else:
				self.update_last_fetched_timestamp(row[1])

			## printing random row data
			print(row)
			return row[0]	
		except Exception as e:
			print(e)			

	## Zodiac sign generator
	def zodiac_sign(self, day, month):
	   # checks month and date within the valid range
	   # of a specified zodiac	
		if month == '12':
			astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
		elif month == '01' or month == '1':
			astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
		elif month == '02' or month == '2':
			astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
		elif month == '03' or month == '3':
			astro_sign = 'Pisces' if (day < 21) else 'Aries'
		elif month == '04' or month == '4':
			astro_sign = 'Aries' if (day < 20) else 'Taurus'
		elif month == '05' or month == '5':
			astro_sign = 'Taurus' if (day < 21) else 'Gemini'
		elif month == '06' or month == '6':
			astro_sign = 'Gemini' if (day < 21) else 'Cancer'
		elif month == '07' or month == '7':
			astro_sign = 'Cancer' if (day < 23) else 'Leo'
		elif month == '08' or month == '8':
			astro_sign = 'Leo' if (day < 23) else 'Virgo'
		elif month == '09' or month == '9':
			astro_sign = 'Virgo' if (day < 23) else 'Libra'
		elif month == '10':
			astro_sign = 'Libra' if (day < 23) else 'Scorpio'
		elif month == '11':
			astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
		return astro_sign
	
	## Function to generate the complete report [Consolidated data]
	def nameanalysis_report(self, dob, firstname):
		if not dob or not dob.strip() or len(dob.split('/')) < 2:
			return "Invalid dob"
		self.arr = dob.split('/')
		month = self.arr[1] 
		day = int(self.arr[0])
		if re.match("^[0-9 ]+$", firstname) or not firstname or not firstname.strip():
			return "Invalid firstname"
		if not re.match("^(1[0-2]|[1-9]|0[1-9])$", month) or day > 31:
			return "Invalid dob"	
		result = self.check_data_exists(firstname, month, day)
		
		## Result none condition
		if result == None:
			zodiac_sign_generator = self.zodiac_sign(day, month)
			random_traits_generator = self.random_traits()
			
			# Convert list to string
			str = ""
			res_traits = str.join(random_traits_generator[0])
			nickname_generator = self.nickname(firstname)
			trait_id = random_traits_generator[1]
			summary = "Hi " + firstname + "," + "Your zodiac sign is: " + zodiac_sign_generator + " and your nickname is: "+ nickname_generator + " Your prediction is :" + res_traits
			self.insert_user_log(firstname, month, day, summary, trait_id)
			return summary
		else:
			return result
