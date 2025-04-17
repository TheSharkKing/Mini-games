class Platform {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    draw(context) {
        context.fillStyle = '#8B4513';
        context.fillRect(this.x, this.y, this.width, this.height);
        
        // Add platform detail
        context.fillStyle = '#654321';
        for (let i = 0; i < this.width; i += 30) {
            context.fillRect(this.x + i, this.y + 5, 20, 2);
        }
    }

    isColliding(player) {
        return player.x < this.x + this.width &&
               player.x + player.width > this.x &&
               player.y < this.y + this.height &&
               player.y + player.height > this.y;
    }
}

class Obstacle {
    constructor(x, y, width, height, speed) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.speed = speed;
        this.originalX = x;
    }

    update() {
        this.x += this.speed;
        
        // Reverse direction when reaching boundaries
        if (Math.abs(this.x - this.originalX) > 100) {
            this.speed = -this.speed;
        }
    }

    draw(context) {
        context.fillStyle = '#FF0000';
        context.fillRect(this.x, this.y, this.width, this.height);
        
        // Add spikes
        context.beginPath();
        context.moveTo(this.x, this.y + this.height);
        context.lineTo(this.x + this.width/2, this.y);
        context.lineTo(this.x + this.width, this.y + this.height);
        context.fillStyle = '#8B0000';
        context.fill();
    }

    isColliding(player) {
        return player.x < this.x + this.width &&
               player.x + player.width > this.x &&
               player.y < this.y + this.height &&
               player.y + player.height > this.y;
    }
}