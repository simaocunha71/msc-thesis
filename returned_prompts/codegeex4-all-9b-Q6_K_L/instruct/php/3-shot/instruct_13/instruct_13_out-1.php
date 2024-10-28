    The code should be formatted and indented correctly.
    Don't add any language-specific keywords that are not in the code, such as function declarations, type definitions, or package imports.
```php
<?php

function create_user($user_data) {
    // Create a new user object
    $user = new User();

    // Set the user's properties
    $user->username = $user_data['username'];
    $user->password = password_hash($user_data['password'], PASSWORD_DEFAULT);
    $user->email = $user_data['email'];
    $user->creation_date = date('Y-m-d H:i:s');
    $user->activation_date = date('Y-m-d H:i:s');
    $user->avatar = getGravatar($user_data['email']);

    // Save the user to the database
    $user->save();

    // Return the created user object
    return $user;
}

?>
```