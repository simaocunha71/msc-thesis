    let _ = db_actor.run();
    let mut db_actor_clone = db_actor.clone();
    executor.execute(move || db_actor_clone.run());
    let _ = executor.shutdown();
}
