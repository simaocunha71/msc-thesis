    vector<string> planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i=0;
    while (i<planets.size()){
        if (planets[i]==planet1){
            if (i<planets.size()-1){
            if (planets[i+1]==planet2){
            for (int j=i+1;j<i+2;j++)
            result.push_back(planets[j]);
            }
            }
            else{
                for (int j=i;j<planets.size();j++)
                result.push_back(planets[j]);
            }
        }
        i+=1;
    }
    return result;
}


