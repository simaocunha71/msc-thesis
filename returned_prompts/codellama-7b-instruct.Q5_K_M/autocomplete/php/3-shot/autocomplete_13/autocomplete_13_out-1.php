	        'password' => password_hash('admin', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);
	    $this->users->create([
	        'acronym' => 'doe',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'John',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);
	    $this->users->create([
	        'acronym' => 'doejane',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'Jane',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);
	    $this->users->create([
	        'acronym' => 'doe2',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'John Doe',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);
	    $this->users->create([
	        'acronym' => 'doe3',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'John Doe',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	