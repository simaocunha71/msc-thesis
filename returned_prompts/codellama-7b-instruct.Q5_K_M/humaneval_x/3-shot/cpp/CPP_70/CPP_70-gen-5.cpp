    vector<int> out;

    int min=*min_element(lst.begin(),lst.end());
    int max=*max_element(lst.begin(),lst.end());

    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]==min)
        {
            out.push_back(min);
            lst.erase(lst.begin()+i);
            i--;
        }
    }

    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]==max)
        {
            out.push_back(max);
            lst.erase(lst.begin()+i);
            i--;
        }
    }

    for (int i=0;i<lst.size();i++)
    {
        if (lst[i]==min)
        {
            out.push_back(min);
            lst.erase(lst.begin()+i);
            i--;
        }
    }

    return out;
}


