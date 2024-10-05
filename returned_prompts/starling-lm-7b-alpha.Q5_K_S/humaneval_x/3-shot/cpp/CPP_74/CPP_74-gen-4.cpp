    int i,j,sum1,sum2;
    vector<string> result;
    if (lst1.size()<lst2.size())
    {
        result=lst1;
    }
    else if (lst1.size()>lst2.size())
    {
        result=lst2;
    }
    else
    {
        for (i=0;i<lst1.size();i++)
        {
            sum1=sum2=0;
            for (j=0;j<lst1[i].length();j++)
                sum1+=lst1[i][j];
            for (j=0;j<lst2[i].length();j++)
                sum2+=lst2[i][j];
            if (sum1<sum2)
            {
                result.push_back(lst1[i]);
            }
            else if (sum1>sum2)
            {
                result.push_back(lst2[i]);
            }
        }
    }
    return result;
}

