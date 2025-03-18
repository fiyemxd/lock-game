# Lock Game - Console-Based Strategy Game

This project is a console-based strategy game where two players compete to lock and remove each other's stones from the playing field. The game is played on a square grid, and players take turns moving their stones to lock the opponent's stones. The game ends when one player has fewer than two stones remaining.

## Features

- **Player Representation**: Each player chooses a unique character to represent their stones on the board.
- **Customizable Board Size**: The game supports board sizes ranging from 4x4 to 8x8.
- **Turn-Based Gameplay**: Players take turns moving their stones to lock and remove the opponent's stones.
- **Locking Mechanism**: Stones are locked and removed when they are surrounded by the opponent's stones in a straight line (horizontally or vertically).
- **Win Condition**: The game ends when one player has fewer than two stones remaining.
- **Play Again Option**: After the game ends, players can choose to play again or exit.

## How to Play

### 1. Run the Game
```bash
python project2.py
```

### 2. Enter Player Representations
Each player will be prompted to enter a unique character to represent their stones on the board.

### 3. Set the Board Size
Enter the size of the playing field (between 4 and 8).

### 4. Gameplay
- The game will display the initial state of the board with each player's stones placed on opposite sides.
- Players take turns entering the position of their stone and the target position to move it.
- Stones can only move straight (horizontally or vertically) and cannot jump over other stones.
- If a stone is locked (surrounded by the opponent's stones), it will be removed from the board.

### 5. Winning the Game
- The game ends when one player has fewer than two stones remaining.
- The player with the most stones remaining wins.

### 6. Play Again
After the game ends, players can choose to play again or exit.

## Game Rules
- **Movement**: Stones can only move straight (horizontally or vertically) and cannot jump over other stones.
- **Locking Stones**: A stone is locked and removed if it is surrounded by the opponent's stones in a straight line (horizontally or vertically).
- **Win Condition**: The game ends when one player has fewer than two stones remaining.

## Example Gameplay
1. Player 1 chooses `X` and Player 2 chooses `O` as their representations.
2. The board size is set to 6x6.
3. Players take turns moving their stones to lock and remove the opponent's stones.
4. The game ends when one player has fewer than two stones remaining.

## Repository Structure
- **`project2.py`**: The main Python script containing the game logic.
- **`README.md`**: This file, providing an overview of the game and instructions on how to play.

## Requirements
- Python 3.x

## How to Run
Clone the repository or download the `project2.py` file.
Run the script using Python:
```bash
python project2.py
```

## Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

