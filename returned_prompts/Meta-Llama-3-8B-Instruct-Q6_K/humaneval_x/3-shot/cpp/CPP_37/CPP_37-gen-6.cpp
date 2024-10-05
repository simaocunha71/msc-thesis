    vector<float> result(l.size());
    int j=0;
    for (int i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            sort(result.begin()+j, result.begin()+j+1);
            j++;
        }
        else
        result[j++]=l[i];
    }
    return result;
}