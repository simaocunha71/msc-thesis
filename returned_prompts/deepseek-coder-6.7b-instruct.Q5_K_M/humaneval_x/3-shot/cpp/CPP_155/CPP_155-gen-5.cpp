    vector<int> counts={0,0}; 
    num=abs(num);
    while(num>0){
        int digit=num%10;
        if(digit%2==0)
            counts[0]+=1;
        else
            counts[1]+=1;
        num=num/10;
    }
    return counts;
}



