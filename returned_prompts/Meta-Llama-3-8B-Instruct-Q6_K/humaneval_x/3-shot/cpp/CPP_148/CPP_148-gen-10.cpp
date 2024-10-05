    vector<string> planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int p1_index=-1, p2_index=-1;
    for (int i=0;i<planets.size();i++)
    {
        if (planets[i]==planet1)
            p1_index=i;
        if (planets[i]==planet2)
            p2_index=i;
    }
    if (p1_index==-1 || p2_index==-1)
        return result;
    for (int i=p1_index+1;i<p2_index;i++)
    {
        result.push_back(planets[i]);
    }
    sort(result.begin(),result.end());
    return result;
}
```



Here are the solutions:

