extern crate futures;
extern crate tokio;
extern crate tokio_executor;
extern crate tokio_util;

use std::thread;
use std::sync::mpsc;
use tokio::sync::mpsc;
use tokio_util::compat::TokioCompatExt;

struct QueryClient {
    tx: mpsc::Sender<String>,
}

struct DBSupervisor {
    rx: mpsc::Receiver<String>,
}

struct ThreadPoolExecutor {
    pool: Vec<thread::JoinHandle<()>>,
}

impl ThreadPoolExecutor {
    fn new(size: usize) -> ThreadPoolExecutor {
        let (tx, rx) = mpsc::channel(size);
        let mut pool = Vec::new();
        for _ in 0..size {
            let tx = tx.clone();
            pool.push(thread::spawn(move || {
                let msg = rx.recv().unwrap();
                // Process query here
            }));
        }
        ThreadPoolExecutor { pool: pool }
    }
}

impl DBSupervisor {
    fn new(rx: mpsc::Receiver<String>) -> DBSupervisor {
        DBSupervisor { rx: rx }
    }

    fn start(&self) {
        let msg = self.rx.recv().unwrap();
        // Process query here
    }
}

impl QueryClient {
    fn new(tx: mpsc::Sender<String>) -> QueryClient {
        QueryClient { tx: tx }
    }

    fn send_query(&self, query: &str) {
        self.tx.send(query.to_string()).unwrap();
    }
}

fn main() {
    let (tx, rx) = mpsc::channel(10);
    let pool = ThreadPoolExecutor::new(5);
    let supervisor = DBSupervisor::new(rx);
    let client = QueryClient::new(tx);

    for _ in 0..10 {
       