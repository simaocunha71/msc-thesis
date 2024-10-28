    string result=s;
    int i;
    for (i=0;i<c.length();i++)
    result.erase(remove(result.begin(),result.end(),c[i]),result.end());
    int begin=0,end=result.length()-1;
    while (begin<end)
    if (result[begin]!=result[end])
    return vector<string>(2,"False");
    else
    {
        begin+=1;
        end-=1;
    }
    return vector<string>(2,"True","".append(result));
}


