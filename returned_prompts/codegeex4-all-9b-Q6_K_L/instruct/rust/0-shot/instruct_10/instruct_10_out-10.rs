fn open_file_with_browser(path: &str) -> Result<String, String> {
    let commands = ["$BROWSER", "xdg-open", "gnome-open", "kde-open"];

    for cmd in commands {
        let output = Command::new(cmd)
            .arg(path)
            .output()
            .map_err(|e| format!("Failed to run command: {}", e))?;

        if output.status.success() {
            return Ok(String::from(cmd));
        }
    }

    Err(format!("Failed to open file with any of the following commands: {:?}", commands))
}

