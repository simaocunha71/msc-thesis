    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i,index1,index2;
    for (i=0;i<planets.size();i++)
    {
        if (planets[i]==planet1)
        index1=i;
        if (planets[i]==planet2)
        index2=i;
    }

    for (i=index1+1;i<index2;i++)
    result.push_back(planets[i]);

    return result;
}



