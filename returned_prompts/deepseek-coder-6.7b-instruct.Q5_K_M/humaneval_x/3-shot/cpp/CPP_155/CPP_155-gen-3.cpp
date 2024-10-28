    vector<int> count(2,0);
    num=abs(num);
    while(num>0){
        if((num%10)%2==0)
        count[0]++;
        else
        count[1]++;
        num=num/10;
    }
    return count;
}


