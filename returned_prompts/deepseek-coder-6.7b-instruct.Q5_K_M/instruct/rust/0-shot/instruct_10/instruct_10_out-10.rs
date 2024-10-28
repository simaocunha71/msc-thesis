    use std::process::Command;
    use std::io::Error;
    use std::io::ErrorKind;
    use std::path::Path;
    use std::fs::canonicalize;
    use std::env;

    pub fn get_opener(path: &Path) -> Result<String, Vec<String>> {
        let mut commands = vec![
            "BROWSER",
            "xdg-open",
            "gnome-open",
            "kde-open",
        ];
        for command in commands.iter() {
            let mut cmd = match Command::new(command) {
                Ok(cmd) => cmd.arg(path),
                Err(_) => continue,
            };
            match cmd.output() {
                Ok(_) => {
                    let canonical_path = match canonicalize(path) {
                        Ok(p) => p.display().to_string(),
                        Err(_) => path.display().to_string(),
                    };
                    return Ok(canonical_path);
                }
                Err(_) => continue,
            }
        }
        return Err(commands);
    }

