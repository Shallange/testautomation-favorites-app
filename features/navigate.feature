Feature: Navigating between tabs

  Scenario Outline: User clicks on a tab and sees correct content
    Given the user is on the homepage
    When the user clicks the "<tab>" tab
    Then the content for "<tab>" should be shown

    Examples:
      | tab          |
      | Katalog      |
      | Mina böcker  |
      | Lägg till bok|