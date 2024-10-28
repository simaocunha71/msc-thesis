
    Example:

    ```
    fn find_command(path: &str) -> String {
        // your code here
    }
    ```

    An example usage would be:

    ```
    assert_eq_str(find_command("/path/to/file"), "xdg-open");
    ```
}

fn find_command(path: &str) -> String {
    let commands = vec![
        "$BROWSER",
        "xdg-open",
        "gnome-open",
        "kde-open",
    ];

    for command in commands.iter() {
        if command_exists(command) {
            return command.to_string();
        }
    }

    format_error_message(commands.clone())
}

fn command_exists(command: &str) -> bool {
    match std::process::Command::new(command)
        .arg(TEST_FILE_PATH)
        .output()
    {
        Ok(_) => true,
        Err(_) => false,
    }
}

fn format_error_message(commands: Vec<&str>) -> String {
    commands.into_iter()
        .map(|&command| format_error_message_single(command))
        .collect()
}

fn format_error_message_single(command: &str) -> String {
    format_error_message_single_command(command).to_string()
}

fn format_error_message_single_command(command: &str) -> &'static str {
    "Command not found: {}", command
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_command() {
        assert_eq_str(find_command(TEST_FILE_PATH), "xdg-open");
    }

    #[test]
    fn test_command_exists() {
        assert_eq(command_exists("xdg-open"), true);
    }

    #[test]
    fn test_format_error_message() {
