function createUser($userData) {
    $db = new PDO('mysql:host=localhost;dbname=users', 'user', 'password');
    $query = "INSERT INTO users (username, email, password, creation_date, activation_date, gravatar_url) VALUES (:username, :email, :password, NOW(), NOW(), :gravatar_url)";
    $stmt = $db->prepare($query);
    $stmt->execute([
        ':username' => $userData['username'],
        ':email' => $userData['email'],
        ':password' => password_hash($userData['password'], PASSWORD_DEFAULT),
        ':gravatar_url' => getGravatar($userData['email']),
    ]);
    $id = $db->lastInsertId();
    $user = new User();
    $user->id = $id;
    $user->username = $userData['username'];
    $user->email = $userData['email'];
    $user->password = $userData['password'];
    $user->creation_date = date('Y-m-d H:i:s', strtotime($userData['creation_date']));
    $user->activation_date = date('Y-m-d H:i:s', strtotime($userData['activation_date']));
    $user->gravatar_url = $userData['gravatar_url'];
    return $user;
}