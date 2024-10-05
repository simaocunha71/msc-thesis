    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i,j;
    for (i=0;i<planets.size();i++)
    if (planets[i]==planet1)
    {
        for (j=i;j<planets.size();j++)
        if (planets[j]==planet2)
        {
            for (i=i;i<=j;i++)
            result.push_back(planets[i]);
            return result;
        }
    }
    return result;
}



