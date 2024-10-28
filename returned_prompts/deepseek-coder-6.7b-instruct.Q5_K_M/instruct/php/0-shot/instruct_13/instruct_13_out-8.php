```php
    function createUser($userData) {
        $createdAt = date('Y-m-d H:i:s');
        $activatedAt = $createdAt; // for now
        $hashedPassword = password_hash($userData['password'], PASSWORD_DEFAULT);

        // Connect to the database
        $db = new PDO('mysql:host=localhost;dbname=test', 'username', 'password');

        // Prepare the SQL statement
        $stmt = $db->prepare("INSERT INTO users (username, email, password, created_at, activated_at) VALUES (:username, :email, :password, :created_at, :activated_at)");

        // Execute the SQL statement
        $stmt->execute([
            'username' => $userData['username'],
            'email' => $userData['email'],
            'password' => $hashedPassword,
            'created_at' => $createdAt,
            'activated_at' => $activatedAt
        ]);

        // Get the ID of the last inserted user
        $userId = $db->lastInsertId();

        // Get the Gravatar image
        $default = "mm"; // default image if Gravatar does not exist
        $size = 50; // size in pixels
        $grav_url = "https://www.gravatar.com/avatar/" . md5(strtolower(trim($userData['email']))) . "?d=" . urlencode($default) . "&s=" . $size;

        // Store the Gravatar image in the database
        $stmt = $db->prepare("UPDATE users SET avatar = :avatar WHERE id = :id");
        $stmt->execute(['avatar' => $grav_url, 'id' => $userId]);

        // Fetch the created user
        $stmt = $db->prepare("SELECT * FROM users WHERE id = :id");
        $stmt->execute(['id' => $userId]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        return $user;
    }
```
