    float min_diff = INFINITY;
    float closest_pair[2];
    for(int i=0; i<numbers.size(); i++){
        for(int j=i+1; j<numbers.size(); j++){
            float diff = abs(numbers[i]-numbers[j]);
            if(diff < min_diff){
                min_diff = diff;
                closest_pair[0] = numbers[i];
                closest_pair[1] = numbers[j];
            }
       