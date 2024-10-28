	        'password' => password_hash('password', PASSWORD_DEFAULT),
	        'created_at' => $now,
	        'updated_at' => $now,
	        'role' => 'admin',
	    ]);

	    $this->users->create([
	        'acronym' => 'user',
	        'email' => 'user@dbwebb.se',
	        'gravatar' => getGravatar('user@dbwebb.se', 65),
	        'name' => 'User',
'password' => password_hash('password', PASSWORD_DEFAULT),
	        'created_at' => $now,
	        'updated_at' => $now,
	        'role' => 'user',
	    ]);