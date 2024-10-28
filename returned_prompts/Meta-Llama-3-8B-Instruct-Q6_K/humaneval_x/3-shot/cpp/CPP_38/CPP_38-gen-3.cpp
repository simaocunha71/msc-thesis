    int l=s.length();
    int num=(l+2)/3;
    string output;
    int i;
    for (i=0;i<num;i++)
    {
        if (i==num-1) output+=s.substr(i*3);
        else output+=s.substr(i*3,3).substr(1)+s.substr(i*3,3)[0];
    }
    return output;
} 

