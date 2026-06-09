class PopCatGame {
    constructor() {
        this.clickCount = 0;
        this.timeLeft = 15;
        this.isGameActive = false;
        this.gameTimer = null;

        this.initializeElements();
        this.attachEventListeners();
    }

    initializeElements() {
        this.comboDisplay = document.getElementById('combo');
        this.timerDisplay = document.getElementById('timer');
        this.gameButton = document.getElementById('gameButton');
        this.playAgainBtn = document.getElementById('playAgainBtn');
        this.gameOverScreen = document.getElementById('gameOver');
        this.finalScoreDisplay = document.getElementById('finalScore');
    }

    attachEventListeners() {
        this.playAgainBtn.addEventListener('click', () => this.resetAndStart());
        this.gameButton.addEventListener('click', () => this.handleClick());
    }

    handleClick() {
        // 如果遊戲還沒開始，自動開始
        if (!this.isGameActive) {
            this.startGame();
        }

        if (!this.isGameActive) return;

        this.clickCount++;
        this.updateDisplay();
        this.playClickAnimation();
        this.switchImage();
        
        // 播放音效（如果有）
        this.playSound();
    }

    startGame() {
        this.isGameActive = true;
        this.gameOverScreen.style.display = 'none';
        this.gameButton.disabled = false;

        this.gameTimer = setInterval(() => this.updateTimer(), 1000);
    }

    resetAndStart() {
        this.resetGameState();
        this.startGame();
    }

    resetGameState() {
        this.clickCount = 0;
        this.timeLeft = 15;
        this.isGameActive = false;

        if (this.gameTimer) {
            clearInterval(this.gameTimer);
        }
        this.updateDisplay();
    }

    switchImage() {
        const imgElement = document.getElementById('buttonImage');
        const currentSrc = imgElement.src;

        // 切換到閉嘴圖片
        if (currentSrc.includes('open.png')) {
            imgElement.src = 'assets/images/close.png';
        } else {
            imgElement.src = 'assets/images/open.png';
        }

        // 100ms 後恢復到開嘴圖片
        setTimeout(() => {
            imgElement.src = 'assets/images/open.png';
        }, 100);
    }

    updateTimer() {
        this.timeLeft--;
        this.timerDisplay.textContent = `時間: ${this.timeLeft}秒`;

        if (this.timeLeft <= 0) {
            this.endGame();
        }
    }

    endGame() {
        this.isGameActive = false;
        clearInterval(this.gameTimer);
        this.gameButton.disabled = true;
        this.gameOverScreen.style.display = 'flex';
        this.finalScoreDisplay.textContent = this.clickCount;
    }

    updateDisplay() {
        this.comboDisplay.textContent = this.clickCount;
        this.timerDisplay.textContent = `時間: ${this.timeLeft}秒`;
    }

    playClickAnimation() {
        this.gameButton.style.transform = 'scale(0.9)';
        setTimeout(() => {
            this.gameButton.style.transform = 'scale(1)';
        }, 100);
    }

    playSound() {
        // 預留音效播放函數
        // const audio = new Audio('assets/sounds/pop.mp3');
        // audio.play();
    }
}

// 當頁面加載完成時初始化遊戲
document.addEventListener('DOMContentLoaded', () => {
    new PopCatGame();
});