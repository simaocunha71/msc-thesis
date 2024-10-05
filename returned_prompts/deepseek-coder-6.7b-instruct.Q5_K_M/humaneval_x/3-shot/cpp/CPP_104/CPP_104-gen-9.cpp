    vector<int> result;
    for(int num: x){
        bool hasEven = false;
        int temp = num;
        while(temp){
            if((temp%10)%2 == 0){
                hasEven = true;
                break;
            }
            temp /= 10;
        }
        if(!hasEven)
            result.push_back(num);
    }
    sort(result.begin(), result.end());
    return result;
}


