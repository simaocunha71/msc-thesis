
    Hint: You may need to use the `Arc` and `Mutex` from the `std::sync` module in Rust.
*/

use std::sync::{Arc, Mutex};
use chan::async::*;
use std::thread::Thread;
use std::sync::mpsc;

struct DBSupervisor {
    db: Arc<Mutex<String>>,
}

struct QueryClient {
    tx: Sender<String>,
}

struct ThreadPoolExecutor {
    threads: Vec<Thread>,
}

impl DBSupervisor {
    fn new() -> DBSupervisor {
        DBSupervisor {
            db: Arc::new(Mutex::new(String::new())),
        }
    }

    fn process_query(&self, query: String) -> String {
        let mut db = self.db.lock().unwrap();
        db.push_str(&query);
        db.clone()
    }
}

impl QueryClient {
    fn new(db_supervisor: &DBSupervisor) -> QueryClient {
        let (tx, _) = mpsc::channel();
        Thread::spawn(move || {
            let query = tx.recv().unwrap();
            db_supervisor.process_query(query);
        });
        QueryClient { tx: tx }
    }

    fn send_query(&self, query: String) {
        self.tx.send(query).unwrap();
    }
}

impl ThreadPoolExecutor {
    fn new(size: usize) -> ThreadPoolExecutor {
        let (tx, rx) = mpsc::channel();
        let db_supervisor = Arc::new(DBSupervisor::new());
        let mut threads = Vec::new();
        for _ in 0..size {
            threads.push(Thread::spawn(move || {
                let query = rx.recv().unwrap();
                let _ = QueryClient::new(&db_supervisor);
                db_supervisor.process_query(query);
            }));
        }
        ThreadPoolExecutor { threads