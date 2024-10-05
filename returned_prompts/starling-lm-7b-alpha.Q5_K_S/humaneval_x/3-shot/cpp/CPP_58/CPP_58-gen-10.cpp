    vector<int> result;
    int i,j,k;
    int temp;
    for (i=0;i<l1.size();i++)
    {
        temp=l1[i];
        for (j=0;j<l2.size();j++)
        {
            if (temp==l2[j])
            {
                result.push_back(temp);
                for (k=j;k<l2.size();k++)
                {
                    l2[k]=l2[k+1];
                }
                break;
            }
        }
    }
    sort(result.begin(),result.end());
    return result;
}




