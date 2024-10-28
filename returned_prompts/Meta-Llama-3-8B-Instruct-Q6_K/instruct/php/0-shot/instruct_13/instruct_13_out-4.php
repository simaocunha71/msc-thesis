    
    function createUser($userData) {
        $db = new mysqli("localhost", "username", "password", "database");
        if($db->connect_error) {
            die("Connection failed: " . $db->connect_error);
        }
        $username = $userData['username'];
        $email = $userData['email'];
        $password = $userData['password'];
        $activationCode = $userData['activationCode'];
        $name = $userData['name'];
        $gravatar = $userData['gravatar'];
        $creationDate = date("Y-m-d H:i:s");
        $activationDate = date("Y-m-d H:i:s");
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO users (username, email, password, activationCode, name, gravatar, creationDate, activationDate) VALUES ('$username', '$email', '$hashedPassword', '$activationCode', '$name', '$gravatar', '$creationDate', '$activationDate')";
        $result = $db->query($sql);
        if($result) {
            $user = array(
                'id' => $db->insert_id,
                'username' => $username,
                'email' => $email,
                'name' => $name,
                'gravatar' => $gravatar,
                'creationDate' => $creationDate,
                'activationDate' => $activationDate
            );
            $db->close();
            return $user;
        } else {
            $db->close();
            return false;
        }
    }    
    function getGravatar($email) {
        $gravatar = "https://www.gravatar.com/avatar/" . md5(strtolower(trim($email))) . "?d=identicon&s=50";
        return $gravatar;
    }    
    function getPasswordHash($password) {
        return password_hash($password, PASSWORD_DEFAULT);
    }    
    function getActivationCode() {
        // Generate a random activation code here
        return "activation_code";
    }    
    function getEmail($user) {
        return $user['email'];
    }    
    function getUsername($user) {
        return $user['username'];
    }    
    function getName($user) {
        return $user['name'];
    }    
    function getGravatar($user) {
        return $user['gravatar'];
    }    
    function getCreationDate($user) {
        return $user['creationDate