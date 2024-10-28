    int i;
    int total_weight=0;
    for (i=0;i<q.size();i++)
    total_weight+=q[i];

    if (total_weight<=w && q==q.reverse())
    return true;

    return false;
}



