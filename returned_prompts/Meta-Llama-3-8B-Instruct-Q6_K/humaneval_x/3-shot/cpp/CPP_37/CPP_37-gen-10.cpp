    vector<float> l_copy(l);
    sort(l_copy.begin()+1, l_copy.end());
    for(int i=0; i<l_copy.size(); i++)
    {
        if(i%2==0)
        {
            l[i]=l_copy[i];
        }
    }
    return l;
}