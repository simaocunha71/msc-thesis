    vector<int> prime;
    for(int i=2;i<n;i++){
        int j=2;
        while(j<i){
            if(i%j==0)
                break;
            j++;
        }
        if(j==i)
            prime.push_back(i);
    }
    return prime;
}
/*
