    for(int i=0;i<l.size();i++)
        l[i]+=1;
    return l;
B:
    for(int i=0;i<l.size();i++)
        l[i]=l[i]+1;
    return l;
C:
    for(int i=0;i<l.size();i++)
        l[i]++;//l[i]=l[i]+1;
    return l;
D:
    for(int i=0;i<l.size();i++)
        l[i] = 1 + l[i];
    return l;
E:
    for(int i=0;i<l.size();i++)
        l[i] += 1;
    return l;
F:
    for(int i=0;i<l.size();i++)
        ++l[i];//l[i]=l[i]+1;
    return l;

}
