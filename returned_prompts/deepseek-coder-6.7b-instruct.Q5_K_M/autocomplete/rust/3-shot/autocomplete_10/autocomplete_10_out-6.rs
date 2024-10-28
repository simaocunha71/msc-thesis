        match Command::new(m).arg(path).status() 
             {
                 Ok(_) => return Ok(m),
                 Err(_) => methods.push(m),
             }
     }
    
     // If none of the methods worked, return an error
