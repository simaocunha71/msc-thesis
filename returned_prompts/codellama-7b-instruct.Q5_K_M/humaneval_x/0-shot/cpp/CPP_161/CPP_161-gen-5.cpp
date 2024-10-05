    if (s[0] == 'a' || s[0] == 'A'){
        s[0] = 'A';
    }
    else if (s[0] == 'A' || s[0] == 'a'){
        s[0] = 'a';
    }
    else{
        goto A;
    }
    return s;
}

