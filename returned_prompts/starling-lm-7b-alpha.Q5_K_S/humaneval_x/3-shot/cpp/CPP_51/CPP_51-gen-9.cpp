    string result;
    char chr;
    for (char chr:text)
    if (!("aeiou".find(tolower(chr))!=string::npos))
    result+=chr;

    return result;
}


