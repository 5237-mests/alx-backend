import { createQueue } from 'kue';

const queue = createQueue();

const obj = {
  phoneNumber: '31256054',
  message: 'SignUp',
};

const job = queue.create('push_notification_code', obj);

job
  .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed attempt', () => console.log('Notification job failed'))
  .save();
