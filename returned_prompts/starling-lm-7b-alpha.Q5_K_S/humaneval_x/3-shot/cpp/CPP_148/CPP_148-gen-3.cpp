    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int i,j;
    vector<string> result;
    for (i=0;i<planets.size();i++)
    {
        if (planets[i]==planet1 || planets[i]==planet2)
        {
            j=i;
            break;
        }
    }
    if (planet1=="Mercury" && planet2=="Neptune")
    for (i=j;i<planets.size();i++)
    result.push_back(planets[i]);
    if (planet1=="Mercury" && planet2!="Neptune")
    for (i=j;i<planets.size();i++)
    {
        if (planets[i]!=planet2)
        result.push_back(planets[i]);
    }
    if (planet1!="Mercury" && planet2=="Neptune")
    {
        for (i=j;i<planets.size();i++)
        {
            if (planets[i]!=planet1)
            result.push_back(planets[i]);
        }
    }
    if (planet1!="Mercury" && planet2!="Neptune")
    {
        for (i=j;i<planets.size();i++)
        {
            if (planets[i]!=planet1 && planets[i]!=planet2)
            result.push_back(planets[i]);
        }
    }
    return result;
}


