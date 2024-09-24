const createPushNotificationsJobs = (jobs, queue) => {
	if (!Array.isArray(jobs)) {
		throw new Error('Jobs is not an array');
	}

	jobs.forEach(el => {
		const job = queue.create('push_notification_code_3', {
			phoneNumber: el.phoneNumber,
			message: el.message,
		}).save(err => {
			if (!err) {
				console.log(`Notification job created: ${job.id || 'N/A (test mode)'}`);
			}
		});

		job.on('complete', () => {
			console.log(`Notification job ${job.id || 'N/A (test mode)'} completed`);
		});

		job.on('failed', (err) => {
			console.log(`Notification job ${job.id || 'N/A (test mode)'} failed: ${err}`);
		});

		job.on('progress', (progress) => {
			console.log(`Notification job ${job.id || 'N/A (test mode)'} ${progress}% complete`);
		});
	});
};

module.exports = createPushNotificationsJobs;
