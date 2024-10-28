
    Function name: createUser

    Input: 
    1. userData: an associative array containing the following fields:
        - id: an integer
        - username: a string
        - email: a string
        - password: a string

    Output: 
    - a user object: an associative array containing the following fields:
        - id: an integer
        - username: a string
        - email: a string
        - password: a string (hashed password)
        - creation_date: a date string in 'Y-m-d H:i:s' format
        - activation_date: a date string in 'Y-m-d H:i:s' format
        - avatar: a string (Gravatar image URL)
*/

function createUser($userData)
{
    $hashedPassword = password_hash($userData['password'], PASSWORD_DEFAULT);
    $creationDate = date('Y-m-d H:i:s');
    $activationDate = date('Y-m-d H:i:s');
    $avatar = getGravatar($userData['email']);

    $user = [
        'id' => $userData['id'],
        'username' => $userData['username'],
        'email' => $userData['email'],
        'password' => $hashedPassword,
        'creation_date' => $creationDate,
        'activation_date' => $activationDate,
        'avatar' => $avatar,
    ];

    return $user;
}

/*
    Write a PHP function that retrieves a Gravatar image for a given email address.
    Only return the code, don't include any other information,
    such as a preamble or suffix.

    Function name: getGravatar

    Input: 
    1. email: a string

    Output: 
    - a string: the URL of the Gravatar image
*/

function getGravatar($email)
{
    $default = "mm"; // default image
    $size = 200; // size in pixels
    $grav_url = "https://www.gravatar.com/avatar/" .