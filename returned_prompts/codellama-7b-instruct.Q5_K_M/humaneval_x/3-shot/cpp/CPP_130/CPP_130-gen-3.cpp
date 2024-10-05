    vector<int> tribonacci;
    int i;
    int previous_1=1;
    int previous_2=3;
    int current=0;
    for (i=0;i<=n;i++)
    {
        current=previous_1+previous_2;
        previous_1=previous_2;
        previous_2=current;
        tribonacci.push_back(current);
    }
    return tribonacci;
}



