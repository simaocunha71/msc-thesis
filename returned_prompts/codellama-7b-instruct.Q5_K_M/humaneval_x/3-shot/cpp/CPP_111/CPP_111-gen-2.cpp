    map<char,int> letter_map;
    int i;
    for (i=0;i<test.length();i++)
    letter_map[test[i]]+=1;
    return letter_map;
}


