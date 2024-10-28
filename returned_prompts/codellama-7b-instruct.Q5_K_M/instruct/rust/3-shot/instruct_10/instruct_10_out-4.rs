
    use std::process::Command;
    use std::process::Output;
    use std::str::from_utf8;
    use std::io::{self, Write};
    use std::path::Path;

    pub fn open_with(path: &str) -> Result<(), String> {
        let browser = env::var("BROWSER").unwrap_or("xdg-open".to_string());
        let path = Path::new(path);

        if let Ok(output) = Command::new(browser).arg(path).output() {
            return Ok(());
        }

        if let Ok(output) = Command::new("xdg-open").arg(path).output() {
            return Ok(());
        }

        if let Ok(output) = Command::new("gnome-open").arg(path).output() {
            return Ok(());
        }

        if let Ok(output) = Command::new("kde-open").arg(path).output() {
            return Ok(());
        }

        Err(format!("Failed to open {}. Tried: {:?}", path.display(), [browser, "xdg-open", "gnome-open", "kde-open"]))
    }

