import redis from 'redis';

const client = redis.createClient();

// Store values in the hash set "HolbertonSchools"
client.hset("HolbertonSchools", "Portland", 50, redis.print);
client.hset("HolbertonSchools", "Seattle", 80, redis.print);
client.hset("HolbertonSchools", "New York", 20, redis.print);
client.hset("HolbertonSchools", "Bogota", 20, redis.print);
client.hset("HolbertonSchools", "Cali", 40, redis.print);
client.hset("HolbertonSchools", "Paris", 2, redis.print);

// Retrieve all values from the hash set "HolbertonSchools"
client.hgetall("HolbertonSchools", function(err, reply) {
  console.log(reply);
});
