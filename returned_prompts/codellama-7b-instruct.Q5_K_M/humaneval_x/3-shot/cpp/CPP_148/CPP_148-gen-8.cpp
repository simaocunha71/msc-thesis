    vector<string> planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i;
    for (i=0;i<planets.size();i++)
    if (planets[i]>=planet1&&planets[i]<=planet2)
    result.push_back(planets[i]);
    return result;
}



