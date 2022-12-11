from app.extensions import mysql


class Users:
    def __init__(self):
        self.mysql = mysql

    @property
    def get_users(self):
        cur = self.mysql.get_db().cursor()
        cur.execute('SELECT user FROM mysql.user;')
        res = cur.fetchall()
        return [i[0] for i in res]
