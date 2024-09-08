    // Write your code here.
    sort(numbers.begin(), numbers.end());
    int i = 0;
    while(i < numbers.size()-1){
        if(numbers[i] == numbers[i+1]){
            numbers.erase(numbers.begin()+i);
        }
        else{
            i++;
        }
    }

    return numbers;
}
