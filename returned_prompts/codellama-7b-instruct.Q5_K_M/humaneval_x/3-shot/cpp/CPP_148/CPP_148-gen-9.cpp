    vector<string> all_planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    int index1=0,index2=0,i;
    for (i=0;i<all_planets.size();i++)
    {
        if (all_planets[i]==planet1)
        index1=i;
        if (all_planets[i]==planet2)
        index2=i;
    }
    if (index1==0||index2==0)
    return {};
    else 
    return {all_planets[index1-1],all_planets[index1],all_planets[index2],all_planets[index2+1]};
}






