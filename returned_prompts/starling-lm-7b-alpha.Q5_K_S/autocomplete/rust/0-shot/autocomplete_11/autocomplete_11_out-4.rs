
    let handle = handle.clone();
    let db_actor_handle = db_actor.start().unwrap();

    let tmp_handle = handle.clone();
    let db_actor = DBSupervisor::new(handle.clone(), move |sender, receiver| {
        DBActor::create_and_monitor(sender, receiver, get_db(), &tmp_handle)
    });

    executor.execute(db_actor);


    fn create_and_monitor(sender: Sender<Command>, receiver: Receiver<Response>) -> Result<()> {
        let mut db_actor = DB::new();
        let _ = db_actor.connect();

        while let Ok(command) = receiver.try_recv() {
            match command {
                Command::Ping => {
                    sender.send(Response::Pong)?;
                }
            }
        }
        Ok(())
    }


    struct DBActor {
        sender: Sender<Command>,
        receiver: Receiver<Response>,
        db: Arc<Mutex<DB>>,
    }

    impl DBActor {
        pub fn new(sender: Sender<Command>, receiver: Receiver<Response>, db: Arc<Mutex<DB>>) -> Self {
            DBActor {
                sender, receiver, db
            }
        }

        fn create_and_monitor(sender: Sender<Command>, receiver: Receiver<Response>, db: Arc<Mutex<DB>>, tmp_handle: &Handle) {
            let mut db_actor = DBActor::new(sender, receiver, db);
            let handle = tmp_handle.clone();
            executor.spawn(async move {
                while let Ok(response) = receiver.recv().await {
                    let handle = handle.clone();
                    let db_actor = db_actor.clone();
                    executor.execute(async move {
                        match response {
                            Response::Pong => {
                                db_actor.send(Command::Ping)?;
                            }
                        }
                    })
                }
            });
        }
    }


    struct