    vector<int> result;
    for(int i=0; i<x.size(); i++) {
        int num = x[i];
        bool hasEvenDigit = false;
        while(num > 0) {
            if((num%10)%2 == 0) {
                hasEvenDigit = true;
                break;
            }
            num = num / 10;
        }
        if(!hasEvenDigit)
            result.push_back(x[i]);
    }
    sort(result.begin(), result.end());
    return result;
}


