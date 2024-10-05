    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        numbers.insert(numbers.begin()+i+1,delimeter);
    }
    return numbers;
}


