    use std::thread;
    use std::sync::Arc;
    use std::sync::mpsc;
    use std::thread::ThreadPoolExecutor;

    struct QueryClient {
        // ...
    }

    struct DBSupervisor {
        // ...
    }

    fn main() {
        let pool = ThreadPoolExecutor::new(8);
        let (tx, rx) = mpsc::channel();

        let db_supervisor = Arc::new(DBSupervisor::new());
        pool.execute(move || {
            db_supervisor.run();
        });

        let query_client = QueryClient::new(tx);
        query_client.run();
    }
