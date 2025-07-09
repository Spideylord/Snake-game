# Snake Game (Terminal-Based)

A classic Snake game implemented in Python, designed to run in the terminal using the `pandas`, `time`, and `random` libraries. The game involves a snake that grows by eating food, with the goal of achieving the highest score possible without colliding with the walls or itself. The high score is saved in a `data.txt` file for persistence.

## Project Structure

The project is organized into the following files:

- **main.py**: Contains the main game loop, handling initialization, user input, and game updates in the terminal.
- **snake.py**: Defines the `Snake` class, managing the snake's movement, growth, and collision detection.
- **food.py**: Implements the `Food` class, responsible for generating food at random positions on the grid.
- **scoreboard.py**: Manages the `Scoreboard` class, which tracks and displays the current score and high score.
- **data.txt**: Stores the high score persistently between game sessions.

## Prerequisites

To run the game, you need Python installed along with the following libraries:

- `pandas`
- `time` (standard library)
- `random` (standard library)

Install `pandas` using pip:

```bash
pip install pandas
```

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd snake-game
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Gameplay

- Use the arrow keys or WASD (W: up, A: left, S: down, D: right) to control the snake's direction (depending on terminal input handling).
- The snake grows longer each time it eats food.
- Avoid colliding with the walls or the snake's own body.
- The game displays the current score and high score in the terminal.
- The high score is saved to `data.txt` and persists across sessions.
- The game board is rendered in the terminal using ASCII characters, with `pandas` used for managing game data (e.g., grid or score tracking).

## File Descriptions

- **main.py**: Initializes the game, handles the terminal-based game loop, and coordinates interactions between the snake, food, and scoreboard.
- **snake.py**: Defines the `Snake` class, which manages the snake's position, movement, and collision logic.
- **food.py**: Implements the `Food` class, which places food at random grid positions for the snake to eat.
- **scoreboard.py**: Manages the `Scoreboard` class, which tracks the player's score and reads/writes the high score to `data.txt` using `pandas` for data handling.
- **data.txt**: A text file used to store the high score.

## Notes

- The game uses `pandas` for managing game data, such as the game grid or score tracking, ensuring efficient data manipulation.
- The terminal-based interface relies on ASCII characters to represent the snake, food, and game boundaries.
- Ensure your terminal supports real-time input and output for the best experience (some terminals may require additional configuration).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
