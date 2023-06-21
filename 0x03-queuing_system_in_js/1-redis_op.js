import redis from 'redis';

// Import the Redis package

const client = redis.createClient();

// Create a Redis client

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler when the client connects to the Redis server

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Event handler when an error occurs with the Redis client

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Function to set a new school name and value in Redis

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

// Function to display the value of a school name stored in Redis

displaySchoolValue('Holberton');

// Call the displaySchoolValue function with 'Holberton' as the school name

setNewSchool('HolbertonSanFrancisco', '100');

// Call the setNewSchool function to set a new school name
// 'HolbertonSanFrancisco' with the value '100' in Redis

displaySchoolValue('HolbertonSanFrancisco');

// Call the displaySchoolValue function with 'HolbertonSanFrancisco'
//  as the school name
