        match Command::new(*m).arg(path).status() {
            Ok(_) => return Ok(*m),
            Err(_) => methods.push(*m),
        }
    }

    // trying xdg-open, gnome-open or kde-open
    for m in methods.iter() {
        match Command::new(*m).arg(path).status() {
            Ok(_) => return Ok(*m),
            Err(_) => (),
        }
    }

    return Err("No browser found");