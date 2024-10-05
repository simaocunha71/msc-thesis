    vector<int> count(2);
    int digit;
    while (num!=0){
        digit=num%10;
        if (digit%2==0)
        count[0]++;
        else
        count[1]++;
        num/=10;
    }
    return count;
}


