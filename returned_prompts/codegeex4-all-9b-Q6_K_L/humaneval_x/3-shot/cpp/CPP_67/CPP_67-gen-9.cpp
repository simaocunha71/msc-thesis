    int apples,oranges;
    char chr;
    int i;
    for (i=0;i<s.length();i++){
        chr=s[i];
        if (chr=='a'){
            apples=atoi(&s[i+1]);
        }
        if (chr=='o'){
            oranges=atoi(&s[i+1]);
        }
    }
    return n-apples-oranges;
}

