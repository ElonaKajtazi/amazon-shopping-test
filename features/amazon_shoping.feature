Feature: Amazon Shopping

  Scenario: Search for a product, add to basket, and update quantity
    Given I am on the Amazon home page
    When I search for "laptop"
    And I select the first product
    And I add the product to the basket
    Then the basket count should be "1"
    When I go to the basket
    And I update the quantity to "3"
    Then the basket count should now be "3"
