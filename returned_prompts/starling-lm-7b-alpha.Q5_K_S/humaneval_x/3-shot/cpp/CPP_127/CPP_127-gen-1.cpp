    if (interval1[1]<interval2[0]||interval2[1]<interval1[0])
    return "NO";
    vector<int> intersection;
    intersection.push_back(max(interval1[0],interval2[0]));
    intersection.push_back(min(interval1[1],interval2[1]));
    if (intersection[0]>=intersection[1])
    return "NO";
    int len=intersection[1]-intersection[0];
    for (int i=2;i<sqrt(len)+1;i++)
    if (len%i==0)
    return "NO";
    return "YES";
}



