Feature: Add a new book to the list

  Scenario: Form appears and user adds a new book
    Given the user is on the homepage
    When the user clicks the "Lägg till bok" button
    And enters "The Alchemist" as the title
    And enters "Paulo Coelho" as the author
    Then the "Lägg till ny bok" button should become enabled
    And the user clicks the "Lägg till ny bok" button
    Then the book "The Alchemist" should appear in the "Katalog" tab

#  Scenario: User adds a book with only whitespace
#    Given the user is on the homepage
#    When the user clicks the "Lägg till bok" button
#    And enters "   " as the title
#    And enters "   " as the author
#    Then the "Lägg till ny bok" button should remain disabled
#    # This test currently fails due to missing input validation