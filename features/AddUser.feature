Feature: General GET and POST functional test

# @AddUser
#  Scenario Outline: Add a new user with name and job details
#    Given User is on add user module
#    When User enters <name> and <job> details
#    And User execute POST operation
#    Then User is created with success code
#    And <name> and <job> are displayed accordingly
#    Examples: POST details
#      | name   | job  |
#      | Vibhor | SDET |
#      | Vibhor | CEO  |
  @GetUser
  Scenario Outline: Get the existing user with name and surname details
    Given User is on Get user module
    When User execute GET operation
    Then User is retrieved with <name> and <surname>
    Examples: GET details
      | name   | surname  |
      | Janet | Weaver |



  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
      Examples:
        |isbn  |  aisle |
        | kjf842v| 28618   |