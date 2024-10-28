    int sum=0,prod=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        prod*=numbers[i];
    }
    vector<int> answer={sum,prod};
    return answer;
}

