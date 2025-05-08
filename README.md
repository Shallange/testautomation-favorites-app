# Favorites app – Test Automation
---
##  Table of Contents

- [Overview](#favorites-app)
- [What has been tested](#what-has-been-tested)
- [Getting Started](#getting-started)
  - [1. Clone the repo](#1-clone-the-repo)
  - [2. Set up a virtual enviorment](#2-set-up-a-virtual-enviorment)
  - [3. Install dependencies](#3-install-dependencies)
  - [4. Run the tests](#4-run-the-tests)
---
*“Läslistan” is a web application where users can build a personal reading list by selecting favorites from a book catalog or adding new books. The client is an organization aiming to promote reading among children and young people.*

Website under test:
https://tap-ht24-testverktyg.github.io/exam-template/


# What has been tested:
- **Adding a new book with a title and author:**
  - The submit button is only enabled when both fields are filled
  - The new book appears in the "Katalog" tab
  - (**Edge case**) Adding a book with only whitespace **should not** be allowed, but currently is.
  The submit button becomes enabled, which it shouldn't. (**Note:** This scenario fails, revealing a missing input validation issue in the application.)
<br>

- **Favoriting a book by clicking the heart icon on hover:**
  - The heart icon becomes visible on hover
  - The favorited book appears in the "Mina böcker" tab

<br>


- **Unfavoriting a book:**
  - Clicking the red heart removes it from favorites
  - Book disappears from the **"Mina böcker"** tab

<br>

- **Navigating between tabs:**
  - All three tabs (**Katalog**, **Mina böcker**, **Lägg till bok**) are clickable
  - Each tab displays the correct content
  - The current tab is visually active (disabled state)

---

## Getting Started

Follow these steps to run the tests locally:

### 1. Clone the repo

```bash
git clone https://github.com/Shallange/testautomation-favorites-app.git
cd testautomation-favorites-app
```

### 2. Set up a virtual enviorment

- *Windows*

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- *MacOS/Linux*

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3 Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4 Run the tests

```bash 
behave
```