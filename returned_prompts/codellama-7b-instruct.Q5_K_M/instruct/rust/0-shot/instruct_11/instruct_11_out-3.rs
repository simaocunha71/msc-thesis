    use std::thread::ThreadPoolExecutor;
    use std::sync::Arc;
    use std::chan::{self, Sender, Receiver};

    use db::DBSupervisor;

    fn main() {
        let pool = ThreadPoolExecutor::new(2);
        let db = Arc::new(DBSupervisor::new());
        let (tx, rx) = chan::async();

        pool.execute(move || {
            db.run();
        });

        tx.send(QueryClient::new(rx));
    }

