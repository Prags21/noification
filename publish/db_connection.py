from mysql.connector.pooling import MySQLConnectionPool
from multiprocessing import Pool

#database configuration
dbconfig = {
  "database": 'notification_db',
  "user":     'root',
  "password":'nishant#3',

  "host":'pragatidbinstance.cwhajy2grhpg.ap-south-1.rds.amazonaws.com'

}
global pool
pool = MySQLConnectionPool(pool_name = "mypool",
                              pool_size = 15,
                              **dbconfig)
