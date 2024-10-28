
    function create_user($user_data) {
        global $conn;
    
        $user_data['creation_date'] = date("Y-m-d H:i:s");
        $user_data['activation_date'] = date("Y-m-d H:i:s");
        $user_data['password'] = password_hash($user_data['password'], PASSWORD_BCRYPT);
        $user_data['gravatar'] = getGravatar($user_data['email']);
    
        $stmt = $conn->prepare("INSERT INTO users (username, email, password, creation_date, activation_date, gravatar) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("ssssss", $user_data['username'], $user_data['email'], $user_data['password'], $user_data['creation_date'], $user_data['activation_date'], $user_data['gravatar']);
        $stmt->execute();
        $user_id = $conn->insert_id;
        $stmt->close();
    
        return $user_id;
    }

