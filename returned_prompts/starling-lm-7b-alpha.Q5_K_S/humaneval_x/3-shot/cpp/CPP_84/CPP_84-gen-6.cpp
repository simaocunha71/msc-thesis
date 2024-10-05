    int i;
    string answer;
    int sum=0;
    for (i=0;i<N;i++)
    {
        sum+=N%2;
        N/=2;
    }

    while (sum>0)
    {
        answer+=(char)(sum%2+'0');
        sum/=2;
    }
    return answer;
}




