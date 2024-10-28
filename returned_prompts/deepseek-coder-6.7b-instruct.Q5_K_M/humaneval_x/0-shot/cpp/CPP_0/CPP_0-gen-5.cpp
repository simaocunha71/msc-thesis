    sort(numbers.begin(), numbers.end());
    int len = numbers.size();
    for(int i=0; i<len-1; i++){
        if(abs(numbers[i] - numbers[i+1]) < threshold)
            return true;
    }
    return false;
