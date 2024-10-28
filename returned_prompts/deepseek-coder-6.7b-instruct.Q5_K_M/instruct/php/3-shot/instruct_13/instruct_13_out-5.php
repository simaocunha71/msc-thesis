{
    $user = new User();
    $user->setUsername($userData['username']);
    $user->setEmail($userData['email']);
    $user->setPassword(password_hash($userData['password'], PASSWORD_BCRYPT));
    $user->setCreationDate(date("Y-m-d H:i:s"));
    $user->setActivationDate(date("Y-m-d H:i:s"));
    $user->setProfilePicture(getGravatar($userData['email']));

    return $user;
}

