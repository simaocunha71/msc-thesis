    vector<int> tri_sequence(n+1);
    if(n>=0)
        tri_sequence[0] = 3;
    if(n>=1)
        tri_sequence[1] = 3;
    if(n>=2)
        tri_sequence[2] = 2;
    for(int i=3; i<=n; i++)
    {
        if(i%2==0)
            tri_sequence[i] = 1 + i/2;
        else
            tri_sequence[i] = tri_sequence[i-1] + tri_sequence[i-2] + tri_sequence[i+1];
    }
    return tri_sequence;
}


