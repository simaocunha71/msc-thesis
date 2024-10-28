    vector<int> result;
    vector<int> even_values;
    int i,j;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0)
    even_values.push_back(arr[i]);

    if (even_values.size()==0)
    return {};

    for (i=0;i<even_values.size();i++)
    for (j=i+1;j<even_values.size();j++)
    if (even_values[i]>even_values[j])
    {
        int temp=even_values[i];
        even_values[i]=even_values[j];
        even_values[j]=temp;
    }

    result.push_back(even_values[0]);
    result.push_back(even_values.size()-1);
    return result;
}



