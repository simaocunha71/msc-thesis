    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i = 0;
    for(auto p : planets){
        if(p == planet1) break;
        i++;
    }
    int j = i;
    for(;j<planets.size();j++){
        if(planets[j] == planet2) break;
    }
    for(int k = i+1; k < j;k++){
        result.push_back(planets[k]);
    }
    return result;
}

B:
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i = 0;
    for(auto p : planets){
        if(p == planet1) break;
        i++;
    }
    if(i >= planets.size() || i >= planet2.size()) return result;
    int j = 0;
    for(;j<planets.size();j++){
        if(planets[j] == planet2) break;
    }
    for(int k = i+1; k < j;k++){
        result.push_back(planets[k]);
    }
    return result;
}

C:
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i = 0;
    for(auto p : planets){
        if(p == planet1) break;
        i++;
    }
    if(i >= planets.size() || i >= planet2.size()) return result;
    int j = 0;
    for(;j<planets.size();j++){
        if(planets[j] == planet2) break;
    }
    for(int k = i+1; k < j;k++){
        result.push_back(planets[k]);
    }
    sort(result.begin(),result.end());
    return result;
}

D:
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int i = 0;
    for(auto p : planets){
        if(p == planet1) break