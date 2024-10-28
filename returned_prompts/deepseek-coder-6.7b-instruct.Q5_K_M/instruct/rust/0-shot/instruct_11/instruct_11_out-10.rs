use std::thread;
use std::sync::{Arc, Mutex};
use std::sync::mpsc;
use std::error::Error;
use futures::channel::mpsc;

struct ThreadPoolExecutor {
    threads: Vec<thread::Thread>,
}

impl ThreadPoolExecutor {
    fn new(size: usize) -> Self {
        let mut threads = Vec::new();
        for _ in 0..size {
            threads.push(thread::spawn(|| {
                loop {}
            }));
        }
        Self { threads }
    }
}

struct DBSupervisor {
    db: Arc<Mutex<DB>>,
}

impl DBSupervisor {
    fn new(db: Arc<Mutex<DB>>) -> Self {
        Self { db }
    }

    fn process_query(&self, query: Query) -> Result<(), Box<Error>> {
        let mut db = self.db.lock().unwrap();
        db.execute_query(query)?;
        Ok(())
    }
}

struct QueryClient {
    db_supervisor: Arc<DBSupervisor>,
    query_channel: mpsc::Sender<Query>,
}

impl QueryClient {
    fn new(db_supervisor: Arc<DBSupervisor>, query_channel: mpsc::Sender<Query>) -> Self {
        Self { db_supervisor, query_channel }
    }

    fn send_query(&self, query: Query) {
        self.query_channel.send(query).unwrap();
    }
}

fn main() {
    let (query_tx, query_rx) = mpsc::channel();
    let db = Arc::new(Mutex::new(DB::new()));
    let db_supervisor = Arc::new(DBSupervisor::new(db.clone()));
    let thread_pool = ThreadPoolExecutor::new(4);

    for thread in thread_pool.threads.iter() {
        thread.join().unwrap();
    }

    let query_client = Query