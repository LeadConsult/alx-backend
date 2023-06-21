import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Event handler when the client connects to the Redis server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler when an error occurs with the Redis client
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
