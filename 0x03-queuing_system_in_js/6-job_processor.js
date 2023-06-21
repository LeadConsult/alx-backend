#!/usr/bin/yarn dev

import { createQueue } from 'kue';

// Create a new instance of the Kue queue
const queue = createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => {
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  );
};

// Process jobs with the name 'push_notification_code'
queue.process('push_notification_code', (job, done) => {
  // Extract phoneNumber and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with the extracted data
  sendNotification(phoneNumber, message);

  // Call the done() function to indicate that the job processing is complete
  done();
});
