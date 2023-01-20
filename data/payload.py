def AddUser(name, job):
    body = {
        "name": name,
        "job": job
    }
    return body

def addBookPayload(isbn,aisle):
    body = {

        "name": "Learn Python Automation with BDD",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Vibhor GL"
    }
    return body
