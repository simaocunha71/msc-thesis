```rust
    let db_actor = DBSupervisor::new(handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &tmp_handle)
    });

    let tmp_handle = handle.clone();
    let task_scheduler = TaskScheduler::new(handle.clone(), move |sender, receiver| {
        TaskSchedulerActor::create_and_monitor(sender, receiver, &tmp_handle)
    });

    let tmp_handle = handle.clone();
    let worker = Worker::new(handle.clone(), move |sender, receiver| {
        WorkerActor::create_and_monitor(sender, receiver, &tmp_handle)
    });

    let tmp_handle = handle.clone();
    let monitor = Monitor::new(handle.clone(), move |sender, receiver| {
        MonitorActor::create_and_monitor(sender, receiver, &tmp_handle)
    });
```