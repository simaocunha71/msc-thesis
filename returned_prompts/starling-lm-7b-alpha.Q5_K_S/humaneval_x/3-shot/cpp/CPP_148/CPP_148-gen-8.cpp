    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> res;
    int i,j;
    for (i=0;i<all_planets.size();i++)
    if (all_planets[i]!=planet1 && all_planets[i]!=planet2)
    {
        if (i<all_planets.size())
        for (j=i+1;j<all_planets.size();j++)
        if (all_planets[j]!=planet1 && all_planets[j]!=planet2)
        {
            if (i<j && all_planets[i]>planet1 && all_planets[i]<planet2 && all_planets[j]>planet1 && all_planets[j]<planet2)
            res.push_back(all_planets[j]);
            if (i>j && all_planets[i]<planet1 && all_planets[i]>planet2 && all_planets[j]<planet1 && all_planets[j]>planet2)
            res.push_back(all_planets[j]);
        }
    }
    return res;
}



