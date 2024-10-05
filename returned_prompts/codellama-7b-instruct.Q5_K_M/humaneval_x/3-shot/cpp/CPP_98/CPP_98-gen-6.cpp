    int c=0;
    string::iterator it;
    for (it=s.begin();it!=s.end();it+=2)
    {
        if (isupper(*it))
        c++;
    }
    return c;
}


