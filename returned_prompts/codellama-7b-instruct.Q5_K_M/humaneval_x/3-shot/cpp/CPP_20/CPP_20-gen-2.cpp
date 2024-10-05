    int i,j;
    float closest_diff=100000;
    float closest_pair[2];
    float diff;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        diff=numbers[j]-numbers[i];
        if (diff<closest_diff){
            closest_diff=diff;
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    return {closest_pair[0], closest_pair[1]};
}



