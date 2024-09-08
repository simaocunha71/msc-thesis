    vector<int> result;
    if(a>b) swap(a,b);
    for(int i=a;i<=b;i++){
        int digit=i;
        while(digit>0){
            int last_digit=digit%10;
            if(last_digit%2==0) result.push_back(last_digit);
            digit/=10;
        }
    }
    sort(result.begin(),result.end());
    return result;

}

