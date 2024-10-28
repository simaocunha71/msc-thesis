    fn get_browser_command(path: &str) -> Result<String, Vec<String>> {
        let commands = &["$BROWSER", "xdg-open", "gnome-open", "kde-open"];
        for command in commands {
            if let Ok(_) = Command::new(command).arg(path).spawn() {
                return Ok(String::from(command));
            }
        }
        let commands = commands.to_vec();
        Err(commands)
    }

