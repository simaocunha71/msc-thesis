    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i;
    for (i=0;i<planets.size();i++)
    if (planets[i]==planet1 || planets[i]==planet2)
    {
        if (planets[i]==planet1)
        {
            int j;
            for (j=i;j<planets.size();j++)
            if (planets[j]==planet2)
            {
                for (i=i+1;i<=j;i++)
                result.push_back(planets[i]);
                break;
            }
        }
        if (planets[i]==planet2)
        {
            for (i=i-1;i>=0;i--)
            if (planets[i]==planet1)
            {
                for (int j=i+1;j<=i+1;j++)
                result.push_back(planets[j]);
                break;
            }
        }
    }
    return result;
}


