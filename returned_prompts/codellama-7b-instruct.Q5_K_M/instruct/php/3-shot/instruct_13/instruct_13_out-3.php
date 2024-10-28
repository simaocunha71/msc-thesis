function create_user($user_data) {
    $user = array(
        "id" => null,
        "username" => $user_data["username"],
        "email" => $user_data["email"],
        "password" => password_hash($user_data["password"], PASSWORD_DEFAULT),
        "creation_date" => date("Y-m-d H:i:s"),
        "activation_date" => date("Y-m-d H:i:s"),
        "gravatar" => getGravatar($user_data["email"])
    );

    // Store user in database
    $stmt = $this->db->prepare("INSERT INTO users (username, email, password, creation_date, activation_date, gravatar) VALUES (:username, :email, :password, :creation_date, :activation_date, :gravatar)");
    $stmt->execute($user);

    $user["id"] = $this->db->lastInsertId();

    return $user;
}

