
        if let Ok(name) = env::var(m) {
            match Command::new(name).arg(path).status() {
                Ok(_) => return Ok(m),
                Err(_) => methods.push(m),
            }
        }
    }

    for m in ["open"].iter() {
        if let Ok(name) = env::var(m) {
            match Command::new(name).arg(path).status() {
                Ok(_) => return Ok(m),
                Err(_) => methods.push(m),
            }
        }
    }

    if !methods.is_empty() {
        Err(
            format!(
                "unable to open {}. tried with: {}",
                path.display(),
                methods.join(", ")
            )
        )
    } else {
        Err(format!("unable to open {}. no method found", path.display()))
    }
