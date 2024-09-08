    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int index1 = -1, index2 = -1;

    for(int i = 0; i < planets.size(); i++){
        if(planets[i] == planet1){
            index1 = i;
        }
        else if(planets[i] == planet2){
            index2 = i;
        }
    }

    if(index1 == -1 || index2 == -1)
        return result;

    for(int i = index1 + 1; i < index2; i++){
        result.push_back(planets[i]);
    }

    sort(result.begin(), result.end());
    return result;
}

