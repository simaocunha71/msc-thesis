    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i,j;
    for (i=0;i<planets.size();i++)
    {
        if (planets[i]==planet1)
        {
            for (j=i;j<planets.size();j++)
            {
                if (planets[j]==planet2)
                {
                    for (int k=i;k<=j;k++)
                    {
                        result.push_back(planets[k]);
                    }
                    break;
                }
                else
                {
                    result.push_back(planets[j]);
                }
            }
        }
    }
    return result;
}




