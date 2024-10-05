    int apples,oranges,mangoes;
    string temp;
    temp=s.substr(0,s.find(' '));
    apples=atoi(temp.c_str());
    temp=s.substr(s.find(' ')+1,s.find('a'));
    oranges=atoi(temp.c_str());
    mangoes=n-apples-oranges;
    return mangoes;
}

