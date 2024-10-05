    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int index1=0,index2=0;
    for (int i=0;i<8;i++)
    {
        if (planets[i]==planet1)
        index1=i;
        if (planets[i]==planet2)
        index2=i;
    }
    if (index1==0 || index2==0)
    return vector<string>();

    vector<string> all_planets;
    for (int i=index1;i<=index2;i++)
    all_planets.push_back(planets[i]);
    return all_planets;
}



