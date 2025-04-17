const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const WIDTH = 800;
const HEIGHT = 400;

canvas.width = WIDTH;
canvas.height = HEIGHT;

let player = {
    x: 50,
    y: HEIGHT - 110,
    width: 40,
    height: 60,
    speed: 5,
    velocityY: 0,
    jump: -15,
    onGround: false
};

const gravity = 0.8;

const platforms = [
    { x: 0, y: HEIGHT - 50, width: WIDTH, height: 50 }, // Ground
    { x: 200, y: 300, width: 100, height: 20 },
    { x: 400, y: 250, width: 100, height: 20 },
    { x: 600, y: 200, width: 100, height: 20 }
];

function drawPlayer() {
    ctx.fillStyle = 'red';
    ctx.fillRect(player.x, player.y, player.width, player.height);
}

function drawPlatforms() {
    ctx.fillStyle = 'blue';
    platforms.forEach(platform => {
        ctx.fillRect(platform.x, platform.y, platform.width, platform.height);
    });
}

function update() {
    player.velocityY += gravity;
    player.y += player.velocityY;

    player.onGround = false;

    platforms.forEach(platform => {
        if (player.x < platform.x + platform.width &&
            player.x + player.width > platform.x &&
            player.y + player.height < platform.y + platform.height &&
            player.y + player.height + player.velocityY >= platform.y) {
            player.y = platform.y - player.height;
            player.velocityY = 0;
            player.onGround = true;
        }
    });

    if (player.y > HEIGHT) {
        console.log("You died!");
        resetGame();
    }
}

function resetGame() {
    player.x = 50;
    player.y = HEIGHT - 110;
    player.velocityY = 0;
}

function gameLoop() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    drawPlatforms();
    drawPlayer();
    update();
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft') {
        player.x -= player.speed;
    }
    if (event.key === 'ArrowRight') {
        player.x += player.speed;
    }
    if (event.key === ' ' && player.onGround) {
        player.velocityY = player.jump;
        player.onGround = false;
    }
});

gameLoop();