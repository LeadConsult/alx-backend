import redis from 'redis';

const client = redis.createClient();

// Event listener for successful connection to Redis server
client.on('connect', function() {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', function(err) {
  console.log('Redis client not connected to the server: ' + err);
});

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Event listener for receiving messages on subscribed channels
client.on('message', function(channel, message) {
  console.log('Message received on channel ' + channel + ': ' + message);

  // Check if the received message is 'KILL_SERVER'
  if (message === 'KILL_SERVER') {
    // Unsubscribe from the channel
    client.unsubscribe();
    // Quit/close the Redis client connection
    client.quit();
  }
});
