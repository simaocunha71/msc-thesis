    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;

    int i, j;
    i = find(planets.begin(), planets.end(), planet1) - planets.begin();
    j = find(planets.begin(), planets.end(), planet2) - planets.begin();

    if(i >= 0 && j >= 0 && i < j)
    {
        for(int k=i+1; k<j; k++)
        {
            result.push_back(planets[k]);
        }
    }
    return result;
}