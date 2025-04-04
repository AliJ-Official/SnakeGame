<p align="center" style="font-size:100px;">
  <strong> Snake Game 🎮</strong>
</p>

A classic Snake game built using Python and Pygame. This game features exciting gameplay with special mango food, sound effects, and increasing difficulty as you progress.

---

## Features ✨

- **Classic Gameplay**: Control the snake to eat apples and grow in size.
- **Special Mango Food**: Occasionally, a mango appears for 5 seconds. Eating it adds 3 points to your score and increases the snake's length.
- **Dynamic Difficulty**: The snake's speed increases every 5 points, making the game more challenging.
- **Immersive Sound Effects**: Background music and sound effects for eating food and game over.
- **Top Score Tracking**: Displays the current score and the top score.

---

## Installation 🛠️

Follow these steps to set up and run the game:

### 1. Clone the Repository
Clone the repository using the following command:
```bash
git clone https://github.com/AliJ-Official/SnakeGame.git
```

If you don't have Git installed, you can download the ZIP file from this [link](https://codeload.github.com/AliJ-Official/SnakeGame/zip/refs/heads/main) and extract it.

### 2. Create a Virtual Environment (Recommended)
Create a virtual environment to isolate dependencies:
```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment using the following command:
- On Windows:
  ```bash
  .venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

### 4. Install Dependencies
Install the required dependencies using pip:
```bash
pip install pygame
```

### 5. Run the Game
Run the game using the following command:
```bash
python SnakeGame.py
```

### 6. Deactivate the Virtual Environment (Optional)
To deactivate the virtual environment, use:
```bash
deactivate
```

Alternatively, you can run the game without activating the virtual environment:
```bash
.venv\Scripts\python.exe SnakeGame.py
```

---

## Game Rules 🕹️

1. Do not go outside the snake's boundaries.
2. Avoid colliding with the snake's own body.
3. Every 5 points, the snake's speed increases.
4. Mangoes are special food that appear for 5 seconds. Eating them adds 3 points to your score and increases the snake's length.

---
## Dependencies 📦

This project requires Python and the following Python package:
- **`pygame==2.6.1`**



---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the game! 🎉
