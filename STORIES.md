## [U1] As a user, I want to be able to add a new book
**So that** I can build my personal reading list.

### Acceptance Criteria:
- [A1.1] A form with fields for title and author is displayed.
- [A1.2] The "Lägg till ny bok" button remains disabled until both fields are filled.
- [A1.3] When I click "Lägg till ny bok", the book appears in the "Mina böcker" tab
- [A1.4] (Edge-case) A book added with only whitespace is still added

---
## [U2] As a user, I want to be able to favorite a book
**So that** I can easily find it later.

### Acceptance Criteria:
- [A2.1] A heart icon becomes visible only when hovering over a book in the catalog.
- [A2.2] Clicking the heart icon marks the book as a favorite (the icon stays visible and turns red).
- [A2.3] The book appears in the "Mina böcker" tab after being marked as a favorite.

---
## [U3] As a user, I want to be able to remove a book from my favorites
**So that** I can manage my list as my preference change.

### Acceptance Criteria:
- [A3.1] Clicking the red heart again removes the book from favorites.
- [A3.2] The heart icon returns to default (non-red).
- [A3.3] The book no longer appears under "Mina böcker".

---
## [U4] As a user, I want to navigate between the tabs
**So that** I can access catalog, favorites, and add a new book easily.

### Acceptance Criteria:
- [A4.1] All three tab buttons are visible.
- [A4.2] Clicking a tab shows relevant content.
- [A4.3] The active tab is visually highlighted or disables its own button.