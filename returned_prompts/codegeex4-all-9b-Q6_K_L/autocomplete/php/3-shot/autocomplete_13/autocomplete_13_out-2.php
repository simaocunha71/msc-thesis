	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'doe',
	        'email' => 'john@doe.com',
	        'gravatar' => getGravatar('john@doe.com', 65),
	        'name' => 'John Doe',
	        'password' => password_hash('doepass', PASSWORD_BCRYPT),
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'jane',
	        'email' => 'jane@doe.com',
	        'gravatar' => getGravatar('jane@doe.com', 65),
	        'name' => 'Jane Doe',
	        'password' => password_hash('doepass', PASSWORD_BCRYPT),
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'manager',
	        'email' => 'manager@dbwebb.se',
	        'gravatar' => getGravatar('manager@dbwebb.se', 65),
	        'name' => 'Manager',
	        'password' => password_hash('managerpass', PASSWORD_BCRYPT),
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);

