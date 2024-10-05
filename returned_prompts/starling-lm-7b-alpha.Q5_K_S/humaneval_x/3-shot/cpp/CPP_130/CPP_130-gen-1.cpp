    vector<int> result;
    if (n==0)
    {
        result.push_back(0);
        return result;
    }

    result.push_back(3);
    result.push_back(1);
    result.push_back(2);
    for (int i=3;i<=n;i++)
    {
        int temp_result;
        if (i%2==0)
        {
            temp_result=3;
        }
        else
        {
            temp_result=result[result.size()-3]+result[result.size()-2]+result[result.size()-1];
        }
        result.push_back(temp_result);
    }
    return result;
}



