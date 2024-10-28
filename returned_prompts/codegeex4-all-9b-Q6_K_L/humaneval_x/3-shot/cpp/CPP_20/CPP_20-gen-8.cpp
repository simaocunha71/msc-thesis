    int i,j;
    float min=100;
    float x;
    vector<float> closest;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        x=abs(numbers[i]-numbers[j]);
        if (x<min)
        {
            min=x;
            closest[0]=numbers[i];
            closest[1]=numbers[j];
        }
    }
    return closest;
}

I got error with these codes, please give me a correct version
