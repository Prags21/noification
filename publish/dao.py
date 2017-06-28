import mysql.connector
#from multiprocessing import Pool
#from mysql.connector.pooling import MySQLConnectionPool
import db_connection
#from mysql.connector import connect
import os
import json
mobile=[]

def fetch(p_id):
	#getting a connection from connection pool
        conn = db_connection.pool.get_connection()
	cursor = conn.cursor()
	"""
	con1=db_connection.pool.get_connection()
	cursor1 = con1.cursor()
	query1 = ("SELECT name FROM agents where id=1")
	cursor1.execute(query1)
	for (name) in cursor1:
		print(name)
	cursor1.close()
	con1.close()
	"""
	query = ("SELECT mob_no FROM agents where parent_id=%s")
	cursor.execute(query,(p_id,))
	result = cursor.fetchall()
	print(result)
	cursor.close()
	conn.close()
	return result