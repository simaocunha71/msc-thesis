
	        'password' => password_hash('admin', PASSWORD_DEFAULT),
	         'created' => $now,
	         'active' => '1'
	     ]);
	     $this->users->create([
	         'acronym' => 'doe',
	         'email' => 'doe@dbwebb.se',
	         'gravatar' => getGravatar('doe@dbwebb.se', 65),
	         'name' => 'John/Doe',
	         'password' => password_hash('doe', PASSWORD_DEFAULT),
	         'created' => $now,
	         'active' => '1'
	     ]);
	     $this->users->create([
	         'acronym' => 'doe2',
	         'email' => 'doe2@dbwebb.se',
	         'gravatar' => getGravatar('doe2@dbwebb.se', 65),
	         'name' => 'John/Doe2',
	         'password' => password_hash('doe2', PASSWORD_DEFAULT),
	         'created' => $now,
	         'active' => '1'
	     ]);

?>

/*

Write the next several lines of the following code.
Don't return a preamble or suffix, just the code.

*/

	     // Add some users 
	     $now = date(DATE_RFC2822);
 
	     $this->users->create([
	         'acronym' => 'admin',
	         'email' => 'admin@dbwebb.se',
	         'gravatar' => getGravatar('admin@dbwebb.se', 65),
	         'name' => 'Administrator',
	         'password' => password_hash('admin', PASSWORD_DEFAULT),
	         'created' => $now,
	         'active' => '1'
	     ]);
	     $this->users->create([
	         'acronym' => 'doe',
	        