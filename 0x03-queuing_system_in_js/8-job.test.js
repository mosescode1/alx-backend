const createPushNotificationsJobs = require('./8-job.js'); // The function to be tested
const kue = require("kue");
const queue = kue.createQueue();
// Mocha hook to enter Kue's test mode before running tests
const chai = require('chai');
const expect = chai.expect;
const should = chai.should();

before(function () {
	queue.testMode.enter();
});

// Clear the queue after each test to ensure a clean slate
afterEach(function () {
	queue.testMode.clear();
});

// Exit Kue's test mode after all tests are done
after(function () {
	queue.testMode.exit();
});

// Main test suite
describe('createPushNotificationsJobs', function () {

	const list = [
		{
			phoneNumber: '4153518780',
			message: 'This is the code 1234 to verify your account'
		},
		{
			phoneNumber: '4153518789',
			message: 'This is the code 2345 to verify your account'
		}
	];

	// Test case to check if an error is thrown when `jobs` is not an array
	it("should display an error message if jobs is not an array", function (done) {
		try {
			createPushNotificationsJobs("", queue); // should throw error
		} catch (error) {
			const message = error.message;
			message.should.equal('Jobs is not an array');
			done();
		}
	});


	it('should create two new jobs with correct data', function (done) {
		const jobs = [
			{ phoneNumber: '4153518780', message: 'This is the code 1234' },
			{ phoneNumber: '4153518781', message: 'This is the code 5678' }
		];

		createPushNotificationsJobs(jobs, queue);

		expect(queue.testMode.jobs.length).to.equal(2); // Ensure two jobs were added
		expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]); // Check job 1 data
		expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]); // Check job 2 data
		done();
	});
});