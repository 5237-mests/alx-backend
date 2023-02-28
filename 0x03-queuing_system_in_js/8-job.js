// eslint-disable-next-line no-unused-vars
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobsO of jobs) {
    const job = queue.create('push_notification_code_3', jobsO);
    job
      .on('enqueue', () => console.log(`Notification job created: ${job.id}`))
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed attempt', (err) => console.log(`Notification job ${job.id} failed: ${err}`))
      .on('progress', (p) => console.log(`Notification job ${job.id}${p}% complete`))
      .save();
  }
}

module.exports = createPushNotificationsJobs;
