    vector<int> result;
    for(auto num : x){
        bool has_even = false;
        int temp = num;
        while(temp > 0){
            if((temp % 10) % 2 == 0){
                has_even = true;
                break;
            }
            temp /= 10;
        }
        if(!has_even)
            result.push_back(num);
    }
    sort(result.begin(), result.end());
    return result;
}

