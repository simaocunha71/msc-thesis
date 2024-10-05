    vector<string> all_planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i;
    for (i=0;i<all_planets.size();i++)
    if ((all_planets[i]==planet1)||(all_planets[i]==planet2))
    {
        if (all_planets[i]==planet1)
        result=vector<string>();
        for (i=i;i<all_planets.size();i++)
        if (all_planets[i]!=planet2)
        result.push_back(all_planets[i]);
        if (all_planets[i]==planet2)
        break;
    }
    return result;
}


