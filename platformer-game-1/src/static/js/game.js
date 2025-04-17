// src/static/js/game.js

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let player;
let platforms = [];
let obstacles = [];
let score = 0;
let gameOver = false;

function init() {
    player = new Player(50, canvas.height - 100);
    
    // Create ground platform
    platforms.push(new Platform(0, canvas.height - 20, canvas.width, 20));
    
    // Add more platforms
    platforms.push(new Platform(300, 400, 200, 20));
    platforms.push(new Platform(100, 300, 200, 20));
    platforms.push(new Platform(500, 200, 200, 20));
    
    // Add obstacles
    createObstacles();
    
    requestAnimationFrame(gameLoop);
}

function createObstacles() {
    obstacles.push(new Obstacle(400, 370, 30, 30, 2)); // Moving obstacle
    obstacles.push(new Obstacle(600, 170, 30, 30, -2)); // Moving obstacle
    obstacles.push(new Obstacle(200, 270, 30, 30, 1.5)); // Moving obstacle
}

function gameLoop() {
    if (!gameOver) {
        update();
        draw();
        requestAnimationFrame(gameLoop);
    }
}

function update() {
    // Handle player movement
    if (keys['ArrowLeft']) player.move(true, false);
    if (keys['ArrowRight']) player.move(false, true);
    if (keys['Space']) player.jump();
    
    player.update();
    
    // Update obstacles
    obstacles.forEach(obstacle => obstacle.update());
    
    handleCollisions();
}

function draw() {
    // Clear canvas
    ctx.fillStyle = '#87CEEB'; // Sky blue background
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    // Draw score
    ctx.fillStyle = 'black';
    ctx.font = '24px Arial';
    ctx.fillText(`Score: ${score}`, 10, 30);
    
    // Draw game elements
    platforms.forEach(platform => platform.draw(ctx));
    obstacles.forEach(obstacle => obstacle.draw(ctx));
    player.draw(ctx);
    
    if (gameOver) {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'white';
        ctx.font = '48px Arial';
        ctx.fillText('Game Over!', canvas.width/2 - 100, canvas.height/2);
    }
}

function handleCollisions() {
    // Platform collisions
    let onPlatform = false;
    platforms.forEach(platform => {
        if (platform.isColliding(player)) {
            if (player.velocityY > 0) {
                player.y = platform.y - player.height;
                player.velocityY = 0;
                player.isJumping = false;
                onPlatform = true;
            }
        }
    });
    
    if (!onPlatform && !player.isJumping) {
        player.isJumping = true;
    }
    
    // Obstacle collisions
    obstacles.forEach(obstacle => {
        if (obstacle.isColliding(player)) {
            gameOver = true;
        }
    });
}

let keys = {};
window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
});

window.addEventListener('keyup', (e) => {
    keys[e.code] = false;
});

init();