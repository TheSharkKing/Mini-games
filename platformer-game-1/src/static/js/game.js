// src/static/js/game.js

const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let player;
let platforms = [];
let gravity = 0.5;
let keys = {};

function init() {
    player = new Player(50, canvas.height - 60);
    platforms.push(new Platform(0, canvas.height - 20, canvas.width, 20));
    requestAnimationFrame(gameLoop);
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

function update() {
    player.update();
    platforms.forEach(platform => platform.update());
    handleCollisions();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    player.draw(ctx);
    platforms.forEach(platform => platform.draw(ctx));
}

function handleCollisions() {
    platforms.forEach(platform => {
        if (player.y + player.height >= platform.y && player.y + player.height <= platform.y + platform.height &&
            player.x + player.width >= platform.x && player.x <= platform.x + platform.width) {
            player.y = platform.y - player.height;
            player.velocityY = 0;
            player.isJumping = false;
        }
    });
}

window.addEventListener('keydown', (e) => {
    keys[e.code] = true;
});

window.addEventListener('keyup', (e) => {
    keys[e.code] = false;
});

init();