import { createClient } from 'redis';

const client = createClient();

client.on('err', (err) => console.log('Redis client not connected to the server: ', err.toString()));
client.on('connect', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

client.on('message', (err, msg) => {
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
  console.log(msg);
});
