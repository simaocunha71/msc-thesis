 
	        'password' => password_hash('password', PASSWORD_DEFAULT),
	        'role' => 'admin',
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'johan',
	        'email' => 'johan@dbwebb.se',
	        'gravatar' => getGravatar('johan@dbwebb.se', 65),
	        'name' => 'Johan', 
	        'password' => password_hash('password', PASSWORD_DEFAULT),
	        'role' => 'user',
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'emil',
	        'email' => 'emil@dbwebb.se',
	        'gravatar' => getGravatar('emil@dbwebb.se', 65),
	        'name' => 'Emil', 
	        'password' => password_hash('password', PASSWORD_DEFAULT),
	        'role' => 'user',
	        'created_at' => $now,
	        'updated_at' => $now
	    ]);
 
	    $this->users->create([
	        'acronym' => 'anna',
	        'email' => 'anna@dbwebb.se',
	        'gravatar' => getGravatar('anna@dbwebb.se', 65),
	        'name' => 'Anna', 
	        'password' => password_hash('password', PASSWORD_DEFAULT),
	        'role' => 'user',
	        'created_at' => $now,
	        'updated_at' => $now
	    ]); 














// Add some courses 
$this->courses->create([
    'name' => 'PHP och MySQL',
    'description' => 'En kurs om PHP och MySQL',
    'created_at' => $now,
    'updated_at' => $now
]);

$this->courses->create([
    'name' => 'Webbutveckling',
    'description' => 'En kurs om webbutveckling',
    'created_at' => $now,
    'updated_at' => $now
]);

$this->courses->create([
    'name' => 'Database',
    'description' => 'En kurs om databaser',
    'created_at' => $now,
    'updated_at' => $now
]);

$this->courses->create([
