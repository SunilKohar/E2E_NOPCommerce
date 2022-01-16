Feature: Customer Details entered and saved
  Background:
    Given User Opens the browser, enters the URL

  @Add_user_details
  Scenario: Login and Add a new user
    Given I have user credentials and log in
    And I click on the customer side bar
    And I click on the Add button to add customer details
    Then I verify that the customer has been added successfully
