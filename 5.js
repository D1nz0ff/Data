const mineflayer = require('mineflayer');

// Set up bot options
const botOptions = {
  host:  '95.216.92.67',
  port: '25648',
  username: 'Bot'
};

// Create bot instance
const bot = mineflayer.createBot(botOptions);

// Listen for chat events
bot.on('chat', (username, message) => {
  // Check if the message contains "tp to me"
  if (message.toLowerCase().includes('tp to me')) {
    // Get the player object for the user who wrote the message
    const player = bot.players[username];

    // Check if the player object exists
    if (player) {
      // Send the "/tpa" command to the player
      bot.chat(`/tpa ${player.username}`);
    }
  }
});

const express = require('express')
const app = express();
const port = 3000;
app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})
