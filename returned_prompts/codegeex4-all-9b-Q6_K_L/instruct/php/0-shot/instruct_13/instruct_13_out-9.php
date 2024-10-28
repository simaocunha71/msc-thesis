<?php

    function createUsers($users) {
        $conn = mysqli_connect("localhost", "user", "password", "database");

        if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
        }

        foreach ($users as $user) {
            $username = $user['username'];
            $password = password_hash($user['password'], PASSWORD_DEFAULT);
            $email = $user['email'];
            $activation_date = date("Y-m-d H:i:s");
            $creation_date = date("Y-m-d H:i:s");
            $gravatar = getGravatar($email);

            $sql = "INSERT INTO users (username, password, email, activation_date, creation_date, gravatar) VALUES ('$username', '$password', '$email', '$activation_date', '$creation_date', '$gravatar')";

            if (mysqli_query($conn, $sql)) {
                $user_id = mysqli_insert_id($conn);
                $user['id'] = $user_id;
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
        }

        mysqli_close($conn);

        return $users;
    }

    function getGravatar($email) {
        $hash = md5(strtolower(trim($email)));
        $url = "http://www.gravatar.com/avatar/" . $hash . "?d=mm&s=256";
        return $url;
    }

    $users = [
        ['username' => 'user1', 'password' => 'password1', 'email' => 'user1@example.com'],
        ['username' => 'user2', 'password' => 'password2', 'email' => 'user2@example.com'],
        ['username' => 'user3', 'password' => 'password3', 'email' => 'user3@example.com']
    ];

    $createdUsers = createUsers($users);

    print_r($createdUsers);

?>

