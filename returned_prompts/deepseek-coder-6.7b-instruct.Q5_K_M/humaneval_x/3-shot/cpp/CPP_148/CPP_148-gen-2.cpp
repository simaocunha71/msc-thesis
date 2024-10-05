    vector<string> planets_order{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int pos1=-1,pos2=-1;
    for (int i=0;i<planets_order.size();i++){
        if (planets_order[i]==planet1) pos1=i;
        if (planets_order[i]==planet2) pos2=i;
    }
    if (pos1==-1 || pos2==-1) return result;
    if (pos1>pos2){
        int temp=pos1;
        pos1=pos2;
        pos2=temp;
    }
    for (int i=pos1+1;i<pos2;i++){
        result.push_back(planets_order[i]);
    }
    return result;
}

