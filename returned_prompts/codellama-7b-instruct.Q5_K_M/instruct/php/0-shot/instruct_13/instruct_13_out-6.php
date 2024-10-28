
    <?php
    function createUser($data) {
        $user = array(
            "id" => uniqid(),
            "name" => $data["name"],
            "email" => $data["email"],
            "password" => password_hash($data["password"], PASSWORD_DEFAULT),
            "created" => date("Y-m-d"),
            "activated" => date("Y-m-d"),
            "gravatar" => getGravatar($data["email"])
        );

        // Add the user to the database

        return $user;
    }
    ?>

    The function should work as follows:

        $user = createUser(array(
            "name" => "Alice",
            "email" => "alice@example.com",
            "password" => "password123"
        ));

        print_r($user);

    The output should be:

    Array
    (
        [id] => 5766297619b48
        [name] => Alice
        [email] => alice@example.com
        [password] => $2y$10$7v.jX15zKVU8NH4wKKQ.Ye386p0K7nXg/7X9MxvZ.33q9KJ4MfXmOi
        [created] => 2015-05-28
        [activated] => 2015-05-28
        [gravatar] => https://www.gravatar.com/avatar/0b79c46a6c8868a980b58d96a7656854
    )

    To verify that the function works, you can use a testing library
    such as PHPUnit.
