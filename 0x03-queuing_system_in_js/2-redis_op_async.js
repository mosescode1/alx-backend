#!/usr/bin/node
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on("error", (err) => {
	console.log(`Redis client not connected to the server: ${err.message}`);
});

// older version of redis
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

// making client.get into a promise
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
	try {
		const value = await getAsync(schoolName);
		console.log(value);
	} catch (err) {
		console.error('Error getting value:', err);
	}

}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');