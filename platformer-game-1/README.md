# Platformer Game

## Overview
This project is a platformer game built using HTML, JavaScript, and Python with Flask. The game features a player character that can jump and navigate through various platforms while avoiding obstacles.

## Project Structure
```
platformer-game
├── src
│   ├── app.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       ├── game.js
│   │       ├── player.js
│   │       └── platform.js
│   └── templates
│       └── index.html
├── tests
│   └── test_app.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd platformer-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```
   python src/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to play the game.

## Game Features
- Smooth player movement and jumping mechanics.
- Various platforms to navigate.
- Obstacles that challenge the player.
- Responsive design for different screen sizes.

## Contributing
Feel free to submit issues or pull requests to improve the game!