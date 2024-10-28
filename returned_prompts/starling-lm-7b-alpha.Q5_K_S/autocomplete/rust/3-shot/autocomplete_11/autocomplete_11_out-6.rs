    let db_handle = handle.clone();
    let db_actor = DBSupervisor::new(db_handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &db_handle)
    });
    let db_handle = handle.clone();
    let db_actor = DBSupervisor::new(db_handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &db_handle)
    });
    let db_handle = handle.clone();
    let db_actor = DBSupervisor::new(db_handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &db_handle)
    });

