
	        'password' => password_hash('admin', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => 1,
	        'deleted' => 0,
	    ]);
 

/*

Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

*/

	    // Add a user 
	    $now = date(DATE_RFC2822);
 
	    $this->users->create([
	        'acronym' => 'doe',
	        'email' => 'doe@dbwebb.se',
	        'gravatar' => getGravatar('doe@dbwebb.se', 65),
	        'name' => 'John/Jane Doe',
	        'password' => password_hash('doe', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => 1,
	        'deleted' => 0,
	    ]);
 

/*

Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

*/

	    // Add a user 
	    $now = date(DATE_RFC2822);
 
	    $this->users->create([
	        'acronym' => 'john',
	        'email' => 'john@dbwebb.se',
	        'gravatar' => getGravatar('john@dbwebb.se', 65),
	        'name' => 'John Doe',
	        'password' => password_hash('john', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => 1,
	        'deleted' => 0,
	    ]);
 

/*

Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

*/

	    // Add a user 
	    $now = date(DATE_R