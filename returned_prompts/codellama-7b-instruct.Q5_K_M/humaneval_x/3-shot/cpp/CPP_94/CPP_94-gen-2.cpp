    int max_prime=0;
    int sum=0;
    for (int i=0;i<lst.size();i++){
        int num=lst[i];
        if (num>max_prime){
            if (is_prime(num))
            max_prime=num;
        }
    }
    for (int i=0;i<max_prime.size();i++)
    sum+=max_prime[i]-'0';
    return sum;
}

int is_prime(int num){
    if (num==2||num==3)
    return true;
    if (num<2||num%2==0||num%3==0)
    return false;
    for (int i=5;i*i<=num;i+=6)
    if (num%i==0||num%(i+2)==0)
    return false;
    return true;
}




