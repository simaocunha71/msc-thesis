    vector<string> planets_order = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i,j;
    for(i=0;i<planets_order.size();i++){
        if(planets_order[i]==planet1){
            for(j=i+1;j<planets_order.size();j++){
                if(planets_order[j]==planet2)
                    return result;
                result.push_back(planets_order[j]);
            }
        }
    }
    return result;
}



