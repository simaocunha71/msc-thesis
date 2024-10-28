    let tmp_handle = handle.clone();
    let db_actor = DBSupervisor::new(handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &tmp_handle)
    });

    let mut workers = HashMap::new();
    for i in 0..num_workers {
        let tmp_handle = handle.clone();
        let worker_actor = WorkerSupervisor::new(handle.clone(), move |sender, receiver| {
            WorkerActor::create_and_monitor(sender, receiver, tmp_handle.clone())
        });
        workers.insert(i, worker_actor);
    }

    let mut workers_vec = Vec::new();
    for worker in workers.values() {
        workers_vec.push(worker.clone());
    }

