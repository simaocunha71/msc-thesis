    int sum=0;
    for(int i=1;i<lst.size();i+=2)
        if(lst[i]%2==0)
            sum+=lst[i];
    return sum;
}

B:
    int sum=0;
    for(int i=0;i<lst.size();i++)
        if(i%2==1&&lst[i]%2==0)
            sum+=lst[i];
    return sum;
}

C:
    int sum=0;
    for(int i=0;i<lst.size();i++)
        if(lst[i]%2==0&&i%2==0)
            sum+=lst[i];
    return sum;
}

D:
    int sum=0;
    for(int i=0;i<lst.size();i++)
        if(i%2==0&&lst[i]%2==1)
            sum+=lst[i];
    return sum;
}

E:
    int sum=0;
    for(int i=0;i<lst.size();i+=2)
        if(lst[i]%2==1)
            sum+=lst[i];
    return sum;
}

F:
    int sum=0;
    for(int i=1;i<lst.size();i+=2)
        if(lst[i]%2==1)
            sum+=lst[i];
    return sum;
}
