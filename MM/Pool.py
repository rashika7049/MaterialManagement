import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host='localhost',port=3306,user="root",password="1234",db="mm")
    cmd=db.cursor()
    return (db,cmd)