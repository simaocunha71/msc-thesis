    vector<int> l2;
    for (int i=0;i<l.size();i++)
    {
        if (i%3==0)
        {
            vector<int> temp;
            for (int j=i;j<l.size() && j%3==0;j++)
            {
                temp.push_back(l[j]);
            }
            sort(temp.begin(),temp.end());
            for (int j=0;j<temp.size();j++)
            {
                l2.push_back(temp[j]);
            }
            i+=temp.size()-1;
        }
        else
        {
            l2.push_back(l[i]);
        }
    }
    return l2;
}  



