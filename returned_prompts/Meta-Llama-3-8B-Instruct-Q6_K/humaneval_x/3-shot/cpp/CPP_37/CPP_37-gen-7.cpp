    vector<float> l2;
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            vector<float> temp;
            for (int j=0;j<i;j++)
            {
                temp.push_back(l[j]);
            }
            sort(temp.begin(), temp.end());
            l2.push_back(temp.back());
            temp.pop_back();
            while (!temp.empty())
            {
                l2.push_back(temp.back());
                temp.pop_back();
            }
        }
        else
        {
            l2.push_back(l[i]);
        }
    }
    return l2;
} 

