        if let Ok(name) = env::var(m) {
            match Command::new(name).arg(path).status() {
                Ok(_) => return Ok(m),
                Err(_) => methods.push(m),
            }
        }
    }

    if methods.is_empty() {
        return Err("No associated program found".into());
    }

    let method = methods.choose(&mut rng).unwrap();
    Ok(method)
}

