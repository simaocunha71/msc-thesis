    int i;
    string cyc;
    for (i=0;i<b.length();i++)
    cyc+=b[b.length()-i-1];
    return a.find(cyc)!=string::npos;
}


