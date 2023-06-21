import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

// Event listener for successful connection to Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the 'holberton school channel'
client.subscribe('holberton school channel');

// Event listener for receiving messages on subscribed channels
client.on('message', (channel, message) => {
  console.log(message);
  // Check if the received message is 'KILL_SERVER'
  if (message === 'KILL_SERVER') {
    // Unsubscribe from the channel
    client.unsubscribe();
    // Quit/close the Redis client connection
    client.quit();
  }
});

// Asynchronous function to publish messages after a specified time delay
async function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    // Publish the message to the 'holberton school channel'
    client.publish('holberton school channel', message);
  }, time);
}

// Schedule the publication of messages at different time intervals
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
