#!/usr/bin/node
import { createClient } from 'redis';

const client = createClient();

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

// older version of redis
client.on("connect", () => {
	console.log("Redis client connected to the server");
})

// (async () => {
// 	await client.connect();
// 	console.log("Redis client connected to the server");
// })();