    int i,j;
    float min_distance=abs(numbers[0]-numbers[1]);
    vector<float> result={numbers[0],numbers[1]};
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        float distance=abs(numbers[i]-numbers[j]);
        if (distance<min_distance){
        min_distance=distance;
        result={numbers[i],numbers[j]};
        }
    }
    return result;
}




