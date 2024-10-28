    fn open_file(path: &str) -> Result<String, String> {
        let mut commands = vec!["$BROWSER", "xdg-open", "gnome-open", "kde-open"];
        for command in commands {
            if let Ok(_) = execute_command(command, path) {
                return Ok(command.to_string());
            }
        }
        Err(commands.join(" or "))
    }

    fn execute_command(command: &str, path: &str) -> Result<(), String> {
        use std::process::Command;
        let output = Command::new(command)
            .arg(path)
            .output()
            .map_err(|e| format!("Failed to execute command: {}", e))?;
        if !output.status.success() {
            Err(format!("Command '{}' failed with status {}", command, output.status))
        } else {
            Ok(())
        }
    }