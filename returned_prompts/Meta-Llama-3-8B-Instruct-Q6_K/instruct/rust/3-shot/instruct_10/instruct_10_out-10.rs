fn get_default_command(path: &str) -> Result<String, String> {
    let mut commands = vec!["$BROWSER", "xdg-open", "gnome-open", "kde-open"];

    for command in &commands {
        if let Ok(output) = Command::new(command).arg(path).output() {
            if output.status.success() {
                return Ok(command.to_string());
            }
        }
    }

    let failed_commands = commands.join(", ");
    Err(format!("Failed to open with: {}", failed_commands))
}
