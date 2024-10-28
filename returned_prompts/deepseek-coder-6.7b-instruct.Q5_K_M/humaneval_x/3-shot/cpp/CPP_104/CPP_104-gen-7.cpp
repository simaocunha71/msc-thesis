    vector<int> result;
    for(auto num : x){
        bool hasEvenDigit = false;
        int digit;
        while(num > 0){
            digit = num % 10;
            if(digit % 2 == 0){
                hasEvenDigit = true;
                break;
            }
            num = num / 10;
        }
        if(!hasEvenDigit){
            result.push_back(num);
        }
    }
    sort(result.begin(), result.end());
    return result;
}


