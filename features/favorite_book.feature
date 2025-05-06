Feature: Favorite a book from the catalog

  Scenario: User favorites a book and it appears in the favorites tab
    Given the user is on the homepage
    When the user hovers over the book "Min katt är min chef"
    And the user clicks the heart icon for the book "Min katt är min chef"
    Then the book "Min katt är min chef" should appear in the "Mina böcker" tab

  Scenario: User removes a book from favorites
    Given the user is on the homepage
    When the user hovers over the book "Min katt är min chef"
    And the user clicks the heart icon for the book "Min katt är min chef"
    Then the book "Min katt är min chef" should appear in the "Mina böcker" tab
    When the user returns to the "Katalog" tab
    And the user clicks the heart icon for the book "Min katt är min chef" again
    Then the book "Min katt är min chef" should no longer appear in the "Mina böcker" tab
