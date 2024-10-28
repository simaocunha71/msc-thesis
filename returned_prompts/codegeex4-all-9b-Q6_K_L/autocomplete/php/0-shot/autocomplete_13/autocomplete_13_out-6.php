 
	        'password' => password_hash('admin', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);

	    $this->users->create([
	        'acronym' => 'user',
	        'email' => 'user@dbwebb.se',
	        'gravatar' => getGravatar('user@dbwebb.se', 65),
	        'name' => 'User', 
	        'password' => password_hash('user', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);

	    $this->users->create([
	        'acronym' => 'mod',
	        'email' => 'moderator@dbwebb.se',
	        'gravatar' => getGravatar('moderator@dbwebb.se', 65),
	        'name' => 'Moderator', 
	        'password' => password_hash('mod', PASSWORD_DEFAULT),
	        'created' => $now,
	        'active' => true,
	    ]);

	    // Add a couple of topics
	    $this->topics->create([
	        'title' => 'What is your favorite programming language?',
	        'slug' => 'what-is-your-favorite-programming-language',
	        'content' => 'This is a discussion about which programming language is your favorite. What is yours?',
	        'category_id' => 1,
	        'user_id' => 1,
	        'created' => $now,
	        'updated' => $now,
	    ]);

	    $this->topics->create([
	        'title' => 'How do you like this site?',
	        'slug' => 'how-do-you-like-this-site',
	        'content' => 'This is a discussion about how you like this site. What do you think?',
	        'category_id' => 1,
	        'user_id' => 2,
	        'created' => $now,
	        'updated' => $now,
	    ]);

	    $this->topics->create([
	        'title' => 'What is your favorite web framework?',
	        'slug' => 'what-is-your-favorite-web-framework',
	        'content' => 'This is a discussion about which web framework is your favorite. What is yours?',
	        'category_id' => 1,
	        'user_id' => 3,
	        'created' => $now,
	        'updated' => $now,
	    ]);

	    // Add some posts
	    $this->posts->create