    int *p,*q;
    p=lst.data();
    q=p;
    while(*p++!=0)
    {
        q=p;
    }
    if(q==p)
        return -1;
    else
        return *q;
}

int main()
{
    vector<int> lst={1, 2, 3, 4, 5};
    int z;
    z=next_smallest(lst);
    printf("%d",z);
    return 0;
}
