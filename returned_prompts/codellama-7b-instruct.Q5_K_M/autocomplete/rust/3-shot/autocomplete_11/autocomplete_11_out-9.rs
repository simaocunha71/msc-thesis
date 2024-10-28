
    executor.spawn(db_actor);

    let tmp_handle = handle.clone();
    let mem_actor = MEMSupervisor::new(handle.clone(), move |sender, receiver| {
        MEMDBActor::create_and_monitor(sender, receiver, get_mem(), &tmp_handle)
    });

    executor.spawn(mem_actor);

    let mut rx = executor.run();

    while let Some(message) = rx.recv().unwrap() {
        println!("{:?}", message);
    }
