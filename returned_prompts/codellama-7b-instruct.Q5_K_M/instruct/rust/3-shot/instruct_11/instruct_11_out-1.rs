
use std::thread::ThreadPoolExecutor;
use std::sync::mpsc::{Sender, channel};
use std::sync::Arc;

fn main() {
    let (tx, rx): (Sender<_>, _) = channel();
    let thread_pool = ThreadPoolExecutor::new(4);
    let db = DBSupervisor::new(tx);
    let client = QueryClient::new(rx, db);
    thread_pool.spawn(client);
}
