    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int i1=-1, i2=-1;
    for(int i=0; i<planets.size(); i++){
        if(planets[i] == planet1){
            i1 = i;
        }
        if(planets[i] == planet2){
            i2 = i;
        }
        if(i1 != -1 && i2 != -1) break;
    }
    if(i1 == -1 || i2 == -1) return {};
    vector<string> result;
    for(int i=i1+1; i<i2; i++){
        result.push_back(planets[i]);
    }
    return result;
} 