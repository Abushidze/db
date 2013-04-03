__author__ = 'Хрюнделя'
import cx_Oracle
con = cx_Oracle.connect('test/test@127.0.0.1')
print(con.version)
con.close()