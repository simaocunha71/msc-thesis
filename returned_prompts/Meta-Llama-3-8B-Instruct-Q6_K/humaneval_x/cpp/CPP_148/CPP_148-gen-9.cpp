    vector<string> result;
    string planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int i = 0;
    while(i < 8){
        if(planet1 == planets[i]){
            break;
        }
        i++;
    }
    if(i == 8){
        return result;
    }
    int j = 0;
    while(j < 8){
        if(planet2 == planets[j]){
            break;
        }
        j++;
    }
    if(j == 8){
        return result;
    }
    for(int k = i+1; k < j; k++){
        result.push_back(planets[k]);
    }
    return result;
}

B:
    vector<string> bf(string planet1, string planet2) {
        vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        vector<string> result;

        if(find(planets.begin(), planets.end(), planet1) == planets.end() || 
           find(planets.begin(), planets.end(), planet2) == planets.end()) {
            return result;
        }

        auto it1 = find(planets.begin(), planets.end(), planet1);
        auto it2 = find(planets.begin(), planets.end(), planet2);

        for(auto it = it1 + 1; it < it2; it++) {
            result.push_back(*it);
        }

        return result;
    }C:
    vector<string> bf(string planet1, string planet2) {
        vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        vector<string> result;

        if(find(planets.begin(), planets.end(), planet1) == planets.end() || 
           find(planets.begin(), planets.end(), planet2) == planets.end()) {
            return result;
        }

        int index1 = 0, index2 = 0;
        for(int i = 0; i < planets.size(); i++) {
            if(planets[i] == planet1) {
                index1 = i;
            }
            if(planets[i] == planet2) {
                index2 = i;
            }
        }

        for(int i = index1