        match Command::new(m).arg(path).status() {
            Ok(_) => return Ok(m),
            Err(_) => methods.push(m),
        }
    }

    for m in ["open", "explorer"].iter() {
        match Command::new(m).arg(path).status() {
            Ok(_) => return Ok(m),
            Err(_) => methods.push(m),
        }
    }

    Err(methods.join(" "))
