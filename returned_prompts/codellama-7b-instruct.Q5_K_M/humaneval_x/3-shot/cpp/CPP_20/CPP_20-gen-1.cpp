    float closest_pair[2];
    int i,j;
    float smallest_diff, current_diff;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++){
        current_diff=abs(numbers[i]-numbers[j]);
        if (smallest_diff==0)
        smallest_diff=current_diff;
        else if (current_diff<smallest_diff)
        smallest_diff=current_diff;
    }
    closest_pair[0]=numbers[i];
    closest_pair[1]=numbers[j];
    return closest_pair;
}


