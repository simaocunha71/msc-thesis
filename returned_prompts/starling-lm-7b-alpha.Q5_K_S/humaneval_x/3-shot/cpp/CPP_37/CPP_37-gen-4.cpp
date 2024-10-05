    vector<float> l_new(l.size());
    int i;
    for (i=0;i<l.size();i++)
    {
        if (i%2==0)
        {
            l_new[i]=l[i];
        }
        else
        {
            l_new[i]=l[i];
        }
    }
    sort(l_new.begin()+1,l_new.end()-1);
    return l_new;
}




