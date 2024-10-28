    int i,j;
    int index1=-1,index2=-1;
    float min_diff=999999999.0;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<min_diff){
        min_diff=abs(numbers[i]-numbers[j]);
        index1=i;
        index2=j;
    }
    vector<float> result={numbers[index1],numbers[index2]};
    return result;
}


