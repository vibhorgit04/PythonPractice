import mysql.connector

from utilities.helper import getProperties
from Logs import logsfile

log = logsfile.get_logs()


class DBHelpers(object):

    def __init__(self):
        # creds_helper = CredentialsHelper()
        # creds = creds_helper.get_db_credentials()
        self.host = getProperties.getDbHostname
        self.db_user = getProperties.getDbUser
        self.db_password = getProperties.getDbPass
        self.db_name = getProperties.getDbName

    def create_connection(self):

        self.conn = mysql.connector.connect(host=self.host, user=self.db_user, password=self.db_password,database = self.db_name)
        if self.conn.is_connected():
            log.info("Connection is successful")
        else:
            log.info("Connection is Unsuccessful")



    def execute_select(self,sql):
        try:
            self.create_connection()
            cur = self.conn.cursor()
            cur.execute(sql)
            rs_dict = cur.fetchall()
            print(rs_dict)
            cur.close()
        except Exception as e:
            log.error("Failed running sql {}. Error: {}".format(sql, str(e)))
        finally:
            self.conn.close()

        return rs_dict


    def execute_sql(self):
        pass

if __name__ == "__main__":
    obj = DBHelpers()
    obj.execute_select()