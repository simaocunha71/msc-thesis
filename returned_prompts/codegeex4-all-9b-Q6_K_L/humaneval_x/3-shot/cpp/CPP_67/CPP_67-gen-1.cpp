    int apples,oranges;
    apples=atoi(s.substr(0,s.find(' ')));
    oranges=atoi(s.substr(s.find(' ')+1,s.find(' ',s.find(' ')+1)-s.find(' ')));
    return n-apples-oranges;
}