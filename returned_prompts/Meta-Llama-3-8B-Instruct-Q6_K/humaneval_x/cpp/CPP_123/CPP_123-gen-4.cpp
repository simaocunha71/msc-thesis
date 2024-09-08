    vector<int> result;
    vector<int> temp;
    while(n != 1){
        if(n % 2 == 0){
            n /= 2;
        }else{
            n = 3*n + 1;
        }
        temp.push_back(n);
    }
    temp.push_back(1);
    for(int i = temp.size()-1; i >= 0; i--){
        if(temp[i] % 2 != 0){
            result.push_back(temp[i]);
        }
    }
    reverse(result.begin(), result.end());
    return result;
} 

