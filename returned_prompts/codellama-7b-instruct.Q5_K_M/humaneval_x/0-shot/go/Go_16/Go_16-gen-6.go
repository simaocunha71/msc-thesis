

    // this function is a bit tricky.
    //
    // the goal is to count the number of distinct characters in a string.
    // we can use the strings.ToLower function to convert a string to lower case,
    // and then use strings.Contains function to check whether the string contains the character or not.
    //
    // for example, if the input string is "Jerry", we want to check whether it contains "j", "e", "r", "y" or not.
    // if it does not contain any of them, we will add the count for them.
    //
    // we can start by initializing a map to store the count of each character.
    //
    // we can use strings.ToLower function to convert the input string to lower case.
    //
    // we can then use strings.Contains function to check whether the input string contains each character.
    // if it contains any character, we will not add the count for that character.
    //
    // if it does not contain any character, we will add the count for that character.
    //
    // we can use the len function to get the length of the input string.
    //
    // we can then return the count for each character in the map.
    //
    // for example, if the input string is "Jerry", the count for each character would be 1.
    //
    // if the input string is "JerryX", the count for each character would be 1, 1, 1, 1, 1.
    //
    // if the input string is "JerryXJerry", the count for each character would be 1, 1, 1, 1, 1, 1, 1, 1.
    //
    // if the input string is "JerryXJerryX", the count for each character would be 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.
    //
    // if the input string is "JerryXJerryXJerry", the count for each character would be 1, 1, 1, 1, 1, 1