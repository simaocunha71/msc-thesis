        match Command::new(m).arg(path).status() {
            Ok(_) => return Ok(m),
            Err(_) => methods.push(m),
        }
    }

    return Err(format!("Failed to open {}, tried: {:?}",
                       path.display(), methods));
}

