#!/usr/bin/node
import { createClient, print } from 'redis';
// import { promisify } from 'util';

const client = createClient();

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

// older version of redis
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

client.subscribe("holberton school channel", (err) => {
	if (err) {
		console.log(err);
	}
})

client.on('message', (_, message) => {
	if (message === 'KILL_SERVER') {
		client.unsubscribe("holberton school channel");
		client.quit();
	}
	if (message) {
		console.log(message);
	}
})
