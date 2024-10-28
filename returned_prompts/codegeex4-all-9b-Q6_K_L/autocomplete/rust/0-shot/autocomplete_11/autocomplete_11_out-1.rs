    let tmp_handle = handle.clone();
    let db_actor = DBSupervisor::new(handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &tmp_handle)
    });

    let tmp_handle = handle.clone();
    let tx_actor = TxSupervisor::new(handle.clone(), move |sender, receiver| {
        TxActor::create_and_monitor(sender, receiver, get_db(), &tmp_handle)
    });

