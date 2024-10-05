    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i=0;
    while (i<planets.size())
    {
        if (planets[i]==planet1)
        break;
        i++;
    }
    if (i>=planets.size() || i>=planets.size()-1 || planets[i+1]==planet2)
    return result;
    for (int j=i+1;j<planets.size()-1;j++)
    result.push_back(planets[j]);
    return result;
}
