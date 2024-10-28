    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> sorted_planets;
    string current_planet;
    int i;
    for (i=0;i<all_planets.size();i++)
    {
        current_planet=all_planets[i];
        if (current_planet==planet1 || current_planet==planet2)
        {
            if (current_planet==planet1)
            {
                sorted_planets.push_back(current_planet);
            }
        }
        if (current_planet==planet2)
        {
            break;
        }
        else if (current_planet!=planet1 && current_planet!=planet2)
        {
            if (i-1>=0)
            {
                if (all_planets[i-1]==planet1)
                {
                    sorted_planets.push_back(current_planet);
                }
            }
        }
    }
    return sorted_planets;
}


