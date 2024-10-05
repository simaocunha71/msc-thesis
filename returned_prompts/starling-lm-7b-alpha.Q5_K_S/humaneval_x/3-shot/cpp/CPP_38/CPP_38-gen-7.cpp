    int l=s.length();
    int num=l/3;
    string output;
    int i;
    for (i=0;i<num;i++)
    {
        if (s.length()<3) break;
        output+=s.substr(0,3);
        s=s.substr(3);
    }
    return output;
}





