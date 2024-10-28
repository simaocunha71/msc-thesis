    vector<string> planets{"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int i,j;
    for (i=0;i<planets.size();i++)
    for (j=i+1;j<planets.size();j++)
    if (planets[j]==planet1)
    {
        int k;
        vector<string> between_planets;
        for (k=i+1;k<j;k++)
        between_planets.push_back(planets[k]);
        return between_planets;
    }
    return {};
}


