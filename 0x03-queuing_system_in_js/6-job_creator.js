#!/usr/bin/node
const kue = require("kue");

const queue = kue.createQueue();

const jobData = {
	phoneNumber: "09065428105",
	message: "This is a kue message",
}

const job = queue.create("push_notification_code", jobData)
	.save(err => {
		if (!err) console.log(`Notification job created: ${job.id}`);
	});

job.on("complete", () => {
	console.log('Notification job completed');
})

job.on("failed", err => {
	console.log(`Notification job failed: ${err}`);
});

job.on("error", err => {
	if (err) console.log("Notification job failed");
})



