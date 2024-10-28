    int i,j;
    float smallest_difference=1000000;
    vector<float> closest_elements;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<smallest_difference)
    {
        smallest_difference=abs(numbers[i]-numbers[j]);
        closest_elements[0]=numbers[i];
        closest_elements[1]=numbers[j];
    }
    return closest_elements;
}


