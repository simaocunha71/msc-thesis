
Here's an example of how the function should be used:

    $data = array(
        'name' => 'Bob Smith',
        'email' => 'bob@example.com',
        'password' => 'mysecretpassword'
    );

    $user = create_user($data);

And here's an example of the function's output:

    stdClass Object
        (
            [id] => 1
            [name] => Bob Smith
            [email] => bob@example.com
            [password] => $2y$10$5Jd1d8B6LB0JKV5i9Vq96.OgG1vRHFaZC10fMd03Bc1Z3O
            [gravatar] => https://www.gravatar.com/avatar/10f8b65c81c819f363350f850d69c3d0
            [created] => 2016-01-01 00:00:00
            [activated] => 2016-01-01 00:00:00
        )

Here is the solution:

```php
function create_user($data) {
    $data['password'] = password_hash($data['password'], PASSWORD_DEFAULT);
    $data['created'] = date('Y-m-d H:i:s');
    $data['activated'] = date('Y-m-d H:i:s');
    $gravatar = getGravatar($data['email']);
    $data['gravatar'] = $gravatar;

    $user = new stdClass();
    foreach ($data as $key => $value) {
        $user->$key = $value;
    }

    return $user;
}
```

And here's an example of how the `getGravatar` function should be implemented:

```php
function getGravatar($email) {
    $hash = md5($email);
    $gravatar = 'https://www.grav