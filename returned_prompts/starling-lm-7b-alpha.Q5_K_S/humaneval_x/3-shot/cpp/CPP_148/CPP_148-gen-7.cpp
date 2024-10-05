    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i;
    for (i=0;i<planets.size();i++)
    if (planets[i]==planet1 || planets[i]==planet2)
    {
        if (planets[i]==planet1)
        {
            for (int j=i;j<planets.size();j++)
            if (planets[j]==planet2)
            {
                for (int k=i;k<=j;k++)
                result.push_back(planets[k]);
                return result;
            }
        }
        if (planets[i]==planet2)
        {
            for (int j=i;j>=0;j--)
            if (planets[j]==planet1)
            {
                for (int k=j;k<=i;k++)
                result.push_back(planets[k]);
                return result;
            }
        }
    }
    return result;
}



