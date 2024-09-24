#!/usr/bin/node
const kue = require("kue");
const queue = kue.createQueue();
const blacklisted = ['415351878', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
	const totalFrames = 100;  // Total number of frames to convert
	let framesProcessed = 0;  // Initialize progress
	job.progress(framesProcessed, totalFrames);

	if (blacklisted.includes(phoneNumber)) {
		return done(`Phone number ${phoneNumber} is blacklisted`);
	}

	framesProcessed = 50;
	job.progress(framesProcessed, totalFrames);
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
	done();
}

// Process jobs in the queue 'push_notification_code_2' with a concurrency of 2 jobs
queue.process('push_notification_code_2', 2, (job, done) => {
	// Extract phoneNumber and message from the job's data
	const { phoneNumber, message } = job.data;

	// Call the sendNotification function to handle the job
	sendNotification(phoneNumber, message, job, done);
});