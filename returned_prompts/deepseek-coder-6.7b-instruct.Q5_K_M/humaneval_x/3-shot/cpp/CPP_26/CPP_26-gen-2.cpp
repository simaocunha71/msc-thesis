    sort(numbers.begin(), numbers.end());
    for(int i=0; i<numbers.size()-1; i++){
        if(numbers[i]==numbers[i+1]){
            numbers.erase(numbers.begin()+i);
            i--;
        }
    }
    return numbers;
}


