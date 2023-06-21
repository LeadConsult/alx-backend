#!/usr/bin/yarn dev

import { createQueue } from 'kue';

// Create new instance of the Kue queue with the name 'push_notification_code'
const queue = createQueue({ name: 'push_notification_code' });

// Create a job named 'push_notification_code' with specific data
const job = queue.create('push_notification_code', {
  phoneNumber: '07046296761',
  message: 'Msg: Account registered',
});

// Event listeners for job events
job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });

// Save the job to the queue
job.save();
