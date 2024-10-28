
	        'password' => bcrypt('secret'),
	        'remember_token' => str_random(10),
	        'created_at' => $now,
	        'updated_at' => $now,
	    ]);

	    $this->users->create([
	        'acronym' => 'user1',
	        'email' => 'user1@dbwebb.se',
	        'gravatar' => getGravatar('user1@dbwebb.se', 65),
	        'name' => 'User 1',
	        'password' => bcrypt('secret'),
	        'remember_token' => str_random(10),
	        'created_at' => $now,
	        'updated_at' => $now,
	    ]);

	    // Create some roles
	    $this->roles->create([
	        'name' => 'admin',
	        'display_name' => 'Admin',
	        'description' => 'Super user',
	        'created_at' => $now,
	        'updated_at' => $now,
	    ]);

	    $this->roles->create([
	        'name' => 'user',
	        'display_name' => 'Regular user',
	        'description' => 'Regular user',
	        'created_at' => $now,
	        'updated_at' => $now,
	    ]);

	    // Assign roles to users
	    $this->users->assignRole('admin');
	    $this->users->assignRole('user');
	    $this->users->assignRole('admin', 'user1');

	    // Create some permissions
	    $this->permissions->create([
	        'name' => 'view-dashboard',
	        'display_name' => 'View Dashboard',
	        'description' => 'View Dashboard',
	        'created_at' => $now,
	        'updated_at' => $now,
	    ]);

	    $this->permissions->create([
	        'name' => 'manage-dashboard',