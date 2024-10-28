use std::process::Command;
use std::io::Error;
use std::env;

fn find_opener(path: &str) -> Result<String, Vec<Error>> {
    let commands = vec![
        "$BROWSER",
        "xdg-open",
        "gnome-open",
        "kde-open",
    ];

    for command in commands.iter() {
        let output = Command::new(command)
            .arg(path)
            .output()
            .map_err(|error| vec![error])?;
        
        if output.status.success() {
            return Ok(command.to_string());
        }
    }

    Err(commands.into_iter().map(|_| Error::new(std::io::ErrorKind::NotFound, "command not found")).collect())
}

