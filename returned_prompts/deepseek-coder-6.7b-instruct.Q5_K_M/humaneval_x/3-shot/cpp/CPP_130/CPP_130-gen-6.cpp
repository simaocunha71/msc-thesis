    vector<int> tribo(n+1, 0);
    tribo[1] = 3;
    for(int i=2; i<=n; i++){
        if(i%2==0){
            tribo[i] = 1 + i/2;
        }else{
            tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i+1];
        }
    }
    return tribo;
}

