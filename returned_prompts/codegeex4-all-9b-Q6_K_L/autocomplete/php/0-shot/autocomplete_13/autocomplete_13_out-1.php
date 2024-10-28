	        'password' => password_hash('admin', PASSWORD_DEFAULT),
	        'created' => $now,
	        'updated' => $now,
	    ]);
	    $this->users->create([
	        'acronym' => 'doe',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'John Doe',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	        'created' => $now,
	        'updated' => $now,
	    ]);
	    $this->users->create([
	        'acronym' => 'user',
	        'email' => 'user@dbwebb.se',
	        'gravatar' => getGravatar('user@dbwebb.se', 65),
	        'name' => 'User',
	        'password' => password_hash('user', PASSWORD_DEFAULT),
	        'created' => $now,
	        'updated' => $now,
	    ]);
