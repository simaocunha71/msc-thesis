    vector<int> tri_seq;
    tri_seq.push_back(3);
    if (n>0)
    {
        tri_seq.push_back(1);
        if (n>1)
        {
            tri_seq.push_back(1);
            if (n>2)
            {
                for (int i=3;i<=n;i++)
                {
                    if (i%2==0)
                    {
                        tri_seq.push_back(i/2+1);
                    }
                    else
                    {
                        tri_seq.push_back(tri_seq[i-1]+tri_seq[i-2]+tri_seq[i-3]);
                    }
                }
            }
        }
    }
    return tri_seq;
}