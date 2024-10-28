use std::sync::mpsc::{channel, Sender};
use std::thread::{self, Thread};
use super::*;

pub struct DBSupervisor {
    thread_pool: ThreadPoolExecutor,
    database: Mutex<Database>,
}

impl DBSupervisor {
    pub fn new(thread_count: usize) -> Self {
        DBSupervisor {
            thread_pool: ThreadPoolExecutor::new(thread_count),
            database: Mutex::new(Database::new()),
        }
    }

    pub fn spawn<F, T>(&self, f: F) -> Thread
    where
        F: FnOnce() -> T,
        T: Send + 'static,
    {
        self.thread_pool.spawn(f)
    }
}

impl Supervisor for DBSupervisor {
    type QueryClient = QueryClient;
    type Database = Database;

    fn spawn_database(&self) -> Database {
        self.spawn(move || {
            let mut database = self.database.lock().unwrap();
            database.listen();
        })
    }

    fn spawn_client(&self, sender: Sender<Query>) -> QueryClient {
        self.spawn(move || {
            let mut client = QueryClient::new(sender);
            client.listen();
            client
        })
    }
}

pub struct QueryClient {
    sender: Sender<Query>,
}

impl QueryClient {
    pub fn new(sender: Sender<Query>) -> Self {
        QueryClient { sender }
    }

    pub fn listen(&mut self) {
        loop {
            let query = receiver::async::<Query>::new(self.sender.clone());
            query.listen();
        }
    }
}

pub struct Query {
    pub query: String,
}

pub struct Database {
    pub queue: ReceiveQueue<Query>,
}

impl Database {
    pub fn new() -> Self {
        Database {
            queue: ReceiveQueue::new(),
        }
    }

    pub fn listen(&mut self) {
        loop {
            let query = self.queue.recv