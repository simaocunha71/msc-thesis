    int i,count=0;
    for (i=0;i<s.length();i++)
    if (i%2==0 && "AEIOU".find(toupper(s[i]))!=string::npos)
    count+=1;

    return count;
}


