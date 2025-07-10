# Tic-Tac-Toe

Welcome to the **tic-tac-toe** repository, a Python implementation of the classic Tic-Tac-Toe game with an expert system to challenge human players.

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [How to Play](#how-to-play)
* [Game Rules](#game-rules)
* [Computer Strategy (Expert System)](#computer-strategy-expert-system)
* [Project Structure](#project-structure)
* [Contributing](#contributing)
* [License](#license)

---

## Overview

This project offers a fully playable console-based Tic-Tac-Toe game in Python. You can play:

* **Human vs. Human**
* **Human vs. Computer** (AI)

The computer opponent uses a set of prioritized heuristic rules (an expert system) to determine its moves.

---

## Features

* Display of a 3×3 game board in the console
* Two game modes:

  * Human vs. Human
  * Human vs. Computer (AI)
* Move validation and win/draw detection
* Expert system-based AI with prioritized rules

---

## Requirements

* Python 3.7 or higher

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Vinicius-Mangueira/tic-tac-toe.git
   ```
2. Change into the project directory:

   ```bash
   cd tic-tac-toe
   ```
3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate   # Windows
   ```

---

## How to Play

1. Run the main script:

   ```bash
   python main.py
   ```
2. Select the game mode:

   * Enter **1** for Human vs. Human
   * Enter **2** for Human vs. Computer
3. Choose your symbol (X or O) and make moves by entering a position number (1–9) according to the layout:

   ```plaintext
    1 | 2 | 3
   -----------
    4 | 5 | 6
   -----------
    7 | 8 | 9
   ```
4. Players alternate turns until one aligns three symbols or the board is full (draw).

---

## Game Rules

* Two players take turns marking X or O on empty cells of a 3×3 grid.
* The first player to align three of their symbols horizontally, vertically, or diagonally wins.
* If all cells are filled without a winning alignment, the game ends in a draw.

---

## Computer Strategy (Expert System)

The AI uses the following prioritized heuristic rules. If a rule does not yield a valid move, the next rule is applied.

1. **Win or Block**: If the AI or opponent has two in a row, play the winning move or block the opponent.
2. **Create Fork**: Make a move that creates two simultaneous threats.
3. **Take Center**: If the center cell is empty, take it.
4. **Opposite Corner**: If the opponent is in a corner, play the opposite corner.
5. **Empty Corner**: Play any available corner.
6. **Empty Side**: Play any available side cell.

---

## Project Structure

```
├── main.py      # Entry point and main game loop
├── board.py     # Board representation and display
├── player.py    # Human and AI player classes
├── rules.py     # Heuristic rules for AI decisions
└── utils.py     # Helper functions (validation, win checks)
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: \`git commit -m "Add feature"
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).
