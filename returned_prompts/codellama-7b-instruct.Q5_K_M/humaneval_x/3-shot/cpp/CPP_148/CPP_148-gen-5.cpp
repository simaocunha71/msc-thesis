    vector<string> planets{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int i,j;
    string planet;
    bool planet_found=false;
    for (i=0;i<8;i++)
    if (planets[i]==planet1)
    planet_found=true;
    if (!planet_found)
    return {};
    for (j=0;j<8;j++)
    if (planets[j]==planet2)
    planet_found=true;
    if (!planet_found)
    return {};
    vector<string> orbit_planets;
    for (i=0;i<8;i++)
    {
        planet=planets[i];
        if (planet_found)
        if ((i>j)&&(i<8))
        orbit_planets.push_back(planet);
        if ((i>j)&&(i>8))
        orbit_planets.push_back(planet);
    }
    return orbit_planets;
}


