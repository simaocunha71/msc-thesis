    int count=0;
    if (num<0)
    num=abs(num);
    while (num>0){
        count+=num%10;
        num/=10;
    }
    return count;
}








