    int even=0,odd=0;
    num=abs(num);
    while(num>0){
        int digit=num%10;
        if(digit%2==0)
            even++;
        else
            odd++;
        num/=10;
    }
    return {even,odd};
}



