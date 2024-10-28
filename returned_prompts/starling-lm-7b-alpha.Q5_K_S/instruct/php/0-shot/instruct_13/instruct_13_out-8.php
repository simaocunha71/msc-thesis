function createUser($userData) {
    $user = new User($userData['username'], $userData['email'], $userData['gravatar'], $userData['password'], $userData['fullname']);
    $user->save();
    return $user;
}

function User($username, $email, $gravatar, $password, $fullname) {
    $this->username = $username;
    $this->email = $email;
    $this->gravatar = $gravatar;
    $this->password = password_hash($password, PASSWORD_DEFAULT);
    $this->fullname = $fullname;
    $this->creation_date = date('Y-m-d H:i:s');
    $this->activation_date = date('Y-m-d H:i:s');
}

function User::save() {
    $query = "INSERT INTO users (username, email, gravatar, password, fullname, creation_date, activation_date) VALUES (?, ?, ?, ?, ?, ?, ?)";
    $stmt = $this->conn->prepare($query);
    $stmt->bind_param("sssssss", $this->username, $this->email, $this->gravatar, $this->password, $this->fullname, $this->creation_date, $this->activation_date);
    $stmt->execute();
    $stmt->close();
}

function getGravatar($email) {
    $gravatar = 'http://www.gravatar.com/avatar/';
    $gravatar .= md5($email);
    $gravatar .= '?s=320&d=identicon';
    return $gravatar;
}

The above PHP function creates and stores user accounts in a database using the `date` function to set the creation and activation dates, the `password_hash` function to hash the password, and the `getGravatar` function to retrieve a gravatar image for the user. The function accepts an array of user data and returns the created user object.

The `User` class has a constructor that takes the username, email, gravatar, password, and fullname as parameters and assigns