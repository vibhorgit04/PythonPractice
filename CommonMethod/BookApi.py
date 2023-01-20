
import DbHelper

class BookApi(object):
    def __init__(self):
        self.db_heler = DbHelper.DBHelpers()

    def get_Book_detail(self,author_name):
        sql = "SELECT * FROM  Books WHERE BookName = '{}';".format(author_name)
        return  self.db_heler.execute_select(sql)



