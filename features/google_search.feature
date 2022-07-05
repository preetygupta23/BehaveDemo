Feature: Search Feature
  Scenario: Validating the search feature
    Given I navigate to google.com
    When I validate the page title
    Then I enter the text Hello Selenium
    And I click on search button