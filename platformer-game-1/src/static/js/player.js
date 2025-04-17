class Player {
    constructor(x, y) {
        this.x = x; // Player's x position
        this.y = y; // Player's y position
        this.width = 50; // Player's width
        this.height = 50; // Player's height
        this.gravity = 1; // Gravity effect
        this.velocityY = 0; // Vertical velocity
        this.isJumping = false; // Jumping state
    }

    move(left, right) {
        if (left) {
            this.x -= 5; // Move left
        }
        if (right) {
            this.x += 5; // Move right
        }
    }

    jump() {
        if (!this.isJumping) {
            this.velocityY = -15; // Initial jump velocity
            this.isJumping = true; // Set jumping state
        }
    }

    update() {
        this.y += this.velocityY; // Update vertical position
        this.velocityY += this.gravity; // Apply gravity

        // Simple ground collision detection
        if (this.y >= canvas.height - this.height) {
            this.y = canvas.height - this.height; // Reset to ground level
            this.isJumping = false; // Reset jumping state
            this.velocityY = 0; // Reset vertical velocity
        }
    }

    draw(context) {
        context.fillStyle = 'blue'; // Player color
        context.fillRect(this.x, this.y, this.width, this.height); // Draw player
    }
}

export default Player;