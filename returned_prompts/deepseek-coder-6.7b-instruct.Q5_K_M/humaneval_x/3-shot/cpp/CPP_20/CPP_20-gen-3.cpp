    float min_diff = INFINITY;
    float diff;
    float min_num1, min_num2;
    int i, j;
    for(i=0; i<numbers.size(); i++){
        for(j=i+1; j<numbers.size(); j++){
            diff = abs(numbers[i] - numbers[j]);
            if(diff < min_diff){
                min_diff = diff;
                min_num1 = min(numbers[i], numbers[j]);
                min_num2 = max(numbers[i], numbers[j]);
            }
        }
    }
    return {min_num1, min_num2};
}


