    int counter=0;
    for (int i=0;i<str.length();i++)
    if (str.substr(i,substring.length())==substring)
    counter+=1;
    return counter;
}




