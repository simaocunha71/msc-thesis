    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i;
    int index1,index2;
    for (i=0;i<all_planets.size();i++)
    {
        if (all_planets[i]==planet1)
        {
            index1=i;
        }
        if (all_planets[i]==planet2)
        {
            index2=i;
        }
    }
    for (i=index1;i<=index2;i++)
    {
        result.push_back(all_planets[i]);
    }
    return result;
}



