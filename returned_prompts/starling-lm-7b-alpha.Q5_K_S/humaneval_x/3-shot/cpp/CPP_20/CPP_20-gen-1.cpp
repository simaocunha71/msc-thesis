    vector<float> result;
    int i,j;
    float min_diff=numbers[1]-numbers[0];
    vector<float>::iterator it;
    for (i=0;i<numbers.size();i++)
    {
        for (j=i+1;j<numbers.size();j++)
        {
            if (abs(numbers[i]-numbers[j])<min_diff)
            {
                min_diff=abs(numbers[i]-numbers[j]);
                it=numbers.begin()+i;
                result.clear();
                result.push_back(*it);
                it=numbers.begin()+j;
                result.push_back(*it);
            }
        }
    }
    return result;
}


