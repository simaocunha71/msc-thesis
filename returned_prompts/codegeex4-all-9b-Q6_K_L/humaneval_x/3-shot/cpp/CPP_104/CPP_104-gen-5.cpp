    vector<int> unique_elements;
    vector<int> even_digits={2,4,6,8};
    int i,j;
    for (i=0;i<x.size();i++)
    {
        int current=x[i];
        for (j=0;j<even_digits.size();j++)
        {
            if (current%10==even_digits[j])
            break;
        }
        if (j==even_digits.size())
        unique_elements.push_back(current);
    }
    sort(unique_elements.begin(),unique_elements.end());
    return unique_elements;
}

