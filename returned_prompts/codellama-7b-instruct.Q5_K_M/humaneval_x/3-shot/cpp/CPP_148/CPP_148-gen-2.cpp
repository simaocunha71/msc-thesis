    vector<string> all_planets{"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> sorted_planets;
    int i,j;
    int planet1_index=0,planet2_index=0;
    for (i=0;i<all_planets.size();i++)
    if (all_planets[i]==planet1)
    planet1_index=i;
    if (planet1_index==0)
    return sorted_planets;
    for (j=0;j<all_planets.size();j++)
    if (all_planets[j]==planet2)
    planet2_index=j;
    if (planet2_index==0)
    return sorted_planets;
    for (i=planet1_index;i<=planet2_index;i++)
    sorted_planets.push_back(all_planets[i]);
    return sorted_planets;
}


