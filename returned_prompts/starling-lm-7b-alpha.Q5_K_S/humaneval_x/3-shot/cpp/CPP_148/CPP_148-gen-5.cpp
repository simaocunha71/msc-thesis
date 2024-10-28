    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i,j;
    for (i=0;i<all_planets.size();i++)
    {
        if (all_planets[i]==planet1)
        {
            j=i;
            break;
        }
    }
    for (i=j+1;i<all_planets.size();i++)
    {
        if (all_planets[i]==planet2)
        {
            j=i;
            break;
        }
    }
    for (i=j;i<all_planets.size();i++)
    {
        result.push_back(all_planets[i]);
    }
    return result;
}


