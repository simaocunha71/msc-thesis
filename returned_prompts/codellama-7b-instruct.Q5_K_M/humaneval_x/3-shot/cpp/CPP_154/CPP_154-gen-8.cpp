    int i;
    for (i=0;i<a.length()-b.length()+1;i++)
    if (a.substr(i,b.length())==b)
    return true;
    return false;
}



