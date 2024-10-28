    vector<string> planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    string planets_str[]={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int i,j;
    bool found1=false,found2=false;
    for (i=0;i<8;i++)
    {
        if (planets[i]==planet1)
        {
            found1=true;
        }
        if (planets[i]==planet2)
        {
            found2=true;
        }
    }
    if (!found1 || !found2)
    {
        return vector<string>();
    }
    vector<string> result;
    for (i=0;i<8;i++)
    {
        if (planets_str[i]==planet1)
        {
            for (j=i+1;j<8;j++)
            {
                result.push_back(planets_str[j]);
            }
            break;
        }
    }
    for (i=result.size()-1;i>=0;i--)
    {
        for (j=0;j<8;j++)
        {
            if (planets_str[j]==result[i])
            {
                for (int k=j-1;k>=0;k--)
                {
                    if (planets_str[k]==planet2)
                    {
                        result.erase(result.begin()+i);
                        return result;
                    }
                }
            }
        }
    }
    return result;
}