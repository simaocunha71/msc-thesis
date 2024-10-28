    int i,count=0,length=substring.length();
    for (i=0;i<str.length()-length+1;i++)
    if (str.substr(i,length)==substring)
    count+=1;

    return count;
}



