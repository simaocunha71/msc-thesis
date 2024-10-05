    vector<int> tribonacci;
    int i;
    int a=1;
    int b=0;
    int c=1;
    
    for (i=0;i<=n;i++)
    {
    if (i%2==0){
        tribonacci.push_back(a);
    }
    else{
        tribonacci.push_back(b+c+a);
    }
    a=b;
    b=c;
    c=tribonacci[i];
    }
    return tribonacci;
}


