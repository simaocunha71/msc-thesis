    int i,j;
    float min=abs(numbers[0]-numbers[1]);
    float temp;
    float close1=numbers[0];
    float close2=numbers[1];
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        temp=abs(numbers[i]-numbers[j]);
        if (temp<min)
        {
            min=temp;
            close1=numbers[i];
            close2=numbers[j];
        }
    }
    vector<float> close_elements;
    close_elements.push_back(close1);
    close_elements.push_back(close2);

    return close_elements;
}

