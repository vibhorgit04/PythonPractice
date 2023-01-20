import requests
from behave import *

import DbHelper
from data import payload
from utilities.RequestHelper import RequestHelper
from utilities.helper import getProperties
from utilities.resources import AddUser
from CommonMethod.BookApi import BookApi
from Logs import logsfile

log = logsfile.get_logs()


# @given(u'User is on add user module')
# def step_impl(context):
#     context.url = getProperties.getappurll + AddUser.AddUser
#     context.headers = getProperties.getheaders
#
#
# @when(u'User enters {name} and {job} details')
# def step_impl(context, name, job):
#     context.payload = payload.AddUser(name, job)
#
#
# @when(u'User execute POST operation')
# def step_impl(context):
#     context.response = RequestHelper().post(wc_endpoint=context.url, params=context.payload, expected_status_code=201)
#
#
# @then(u'User is created with success code')
# def step_impl(context):
#     # print(context.response.json())
#     # statuscode = context.response.status_code
#     # assert statuscode == 201,"Resource couldn't be created"
#     pass
#
#
# @then(u'{name} and {job} are displayed accordingly')
# def step_impl(context, name, job):
#     assert context.response['name'] == name
#     assert context.response['job'] == job

@given(u'User is on Get user module')
def step_impl(context):
    context.url = getProperties.getappurll + AddUser.GetUser
    context.headers = getProperties.getheaders


@when(u'User execute GET operation')
def step_impl(context):
    context.response = RequestHelper().get(wc_endpoint=context.url, params=context.headers, expected_status_code=200)
    print(context.response)

@then(u'User is retrieved with {name} and {surname}')
def step_impl(context,name,surname):
 assert context.response['data']['first_name'] == name
 assert context.response['data']['last_name'] == surname

@given(u'the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getProperties.getappurl + AddUser.AddBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = payload.addBookPayload(isbn,aisle)
    print(context.url)


@when(u'we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = RequestHelper().post(wc_endpoint=context.url, params=context.payload, expected_status_code=200)
    #context.response = requests.post(context.url, json=context.payload , headers=context.headers)
    print(context.response)

@then(u'book is successfully added')
def step_impl(context):
 #   print(context.response.json())
   # response_json = context.response.json()
    context.bookId = context.response['ID']
    course_name = 'Selenium'
    print(context.bookId)
    assert context.response["Msg"] == "successfully added"
    tp = BookApi().get_Book_detail(course_name)
    assert tp, f'Course not found in database. Course name : {course_name}'
    print(tp)
    log.info("Calling Delete API to delete further")