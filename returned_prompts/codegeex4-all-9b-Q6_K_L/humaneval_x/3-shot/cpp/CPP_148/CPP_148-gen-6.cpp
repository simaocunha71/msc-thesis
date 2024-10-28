    vector<string> planet_order;
    int index1,index2;
    string planet_names[]={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int i;
    for (i=0;i<8;i++)
    {
        if (planet_names[i]==planet1)
        {
            index1=i;
        }
        if (planet_names[i]==planet2)
        {
            index2=i;
        }
    }
    if (index1==0 || index2==0)
    {
        return planet_order;
    }
    if (index1<index2){
    for (i=index1;i<index2;i++)
    {
        planet_order.push_back(planet_names[i]);
    }
    }
    else{
    for (i=index2;i<index1;i++)
    {
        planet_order.push_back(planet_names[i]);
    }
    }
    return planet_order;
}

