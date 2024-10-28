
    ```rust
    fn open_file(path: &str) -> Result<(), String> {
    ```

    ```rust
    let paths = ["$BROWSER", "xdg-open", "gnome-open", "kde-open"];
    let mut tried = Vec::new();
    let mut last_error = None;
    for path in paths {
        let status = Command::new(path)
            .arg(path)
            .status()
            .map_err(|e| e.to_string());
        match status {
            Ok(status) if status.success() => return Ok(()),
            Ok(status) => last_error = Some(format!("{} exited with {}", path, status)),
            Err(e) => last_error = Some(format!("{} failed: {}", path, e)),
        }
        tried.push(path.to_string());
    }
    Err(tried.join(", "))
    }
    ```

    ```rust
    fn main() {
        let path = "/usr/share/doc/rust/README.md";
        match open_file(path) {
            Ok(()) => println!("Opened {}", path),
            Err(e) => eprintln!("Failed to open {}: {}", path, e),
        }
    }
    ```

    ```rust
    fn main() {
        let path = "/usr/share/doc/rust/README.md";
        match open_file(path) {
            Ok(()) => println!("Opened {}", path),
            Err(e) => eprintln!("Failed to open {}: {}", path, e),
        }
    }
    ```

    ```rust
    fn main() {
        let path = "/usr/share/doc/rust/README.md";
        match open_file(path) {
            Ok(()) => println!("Opened {}", path),
            Err(e) => eprintln!("Failed to open {}: {}", path, e),
        }
    }
    ```

    ```rust
    fn main() {
        let path = "/usr/share/doc/rust/README.md";