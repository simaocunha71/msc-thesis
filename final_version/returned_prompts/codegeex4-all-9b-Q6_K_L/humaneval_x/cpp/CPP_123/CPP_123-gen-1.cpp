    vector<int> result;
    while(n != 1){
        if(n % 2 == 1){
            result.push_back(n);
            n = n * 3 + 1;
        }else{
            n = n / 2;
        }
    }
    result.push_back(n);
    sort(result.begin(), result.end());
    return result;

B:
    vector<int> result;
    while(n != 1){
        if(n % 2 == 1){
            result.push_back(n);
            n = n * 3 + 1;
        }else{
            n = n / 2;
        }
    }
    sort(result.begin(), result.end());
    return result;

C:
    vector<int> result;
    while(n != 1){
        if(n % 2 == 1){
            result.push_back(n);
            n = n * 3 + 1;
        }else{
            n = n / 2;
        }
    }
    sort(result.begin(), result.end(), greater<int>());
    return result;

D:
    vector<int> result;
    while(n != 1){
        if(n % 2 == 1){
            result.push_back(n);
            n = n * 3 + 1;
        }else{
            n = n / 2;
        }
    }
    sort(result.begin(), result.end(), less<int>());
    return result;
}

