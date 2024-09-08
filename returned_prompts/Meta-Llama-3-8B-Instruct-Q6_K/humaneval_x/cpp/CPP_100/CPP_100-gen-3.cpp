    vector<int> result;
    int i = 1;
    while(i <= n){
        if(i % 2 == 0){
            result.push_back(i);
        }else{
            result.push_back(i+1);
        }
        i++;
    }
    return result;
}

