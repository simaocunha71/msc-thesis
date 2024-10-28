    string b2=b+b;
    int i;
    for (i=0;i<=b.length();i++)
    if (a.find(b2.substr(i))==string::npos)
    return false;

    return true;
}

