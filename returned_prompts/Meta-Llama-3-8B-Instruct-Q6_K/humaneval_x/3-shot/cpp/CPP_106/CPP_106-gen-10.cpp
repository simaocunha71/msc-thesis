    vector<int> result;
    int i;
    for(i=1;i<=n;i++){
        if(i%2==0)
            result.push_back(factorial(i));
        else
            result.push_back(sum(i));
    }
    return result;
}

int factorial(int n){
    int i,fact=1;
    for(i=1;i<=n;i++){
        fact*=i;
    }
    return fact;
}

int sum(int n){
    int i,sum=0;
    for(i=1;i<=n;i++){
        sum+=i;
    }
    return sum;
}