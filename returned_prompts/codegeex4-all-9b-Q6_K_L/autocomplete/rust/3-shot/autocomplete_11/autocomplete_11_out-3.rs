    let db_handle = db_actor.handle();

    let tmp_handle = handle.clone();
    let state_actor = StateSupervisor::new(handle.clone(), move |sender, receiver| {
        StateActor::create_and_monitor(sender, receiver, db_handle.clone())
    });

Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

    let tx_actor = TxSupervisor::new(handle.clone(), move |sender, receiver| {
        TxActor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

    let tx_handle = tx_actor.handle();

    let tmp_handle = handle.clone();
    let tx2_actor = Tx2Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx2Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx2_handle = tx2_actor.handle();

    let tmp_handle = handle.clone();
    let tx3_actor = Tx3Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx3Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx3_handle = tx3_actor.handle();

    let tmp_handle = handle.clone();
    let tx4_actor = Tx4Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx4Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx4_handle = tx4_actor.handle();

    let tmp_handle = handle.clone();
    let tx5_actor = Tx5Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx5Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx5_handle = tx5_actor.handle();

    let tmp_handle = handle.clone();
    let tx6_actor = Tx6Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx6Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx6_handle = tx6_actor.handle();

    let tmp_handle = handle.clone();
    let tx7_actor = Tx7Supervisor::new(handle.clone(), move |sender, receiver| {
        Tx7Actor::create_and_monitor(sender, receiver, db_handle.clone(), &tmp_handle)
    });

let tx7_handle