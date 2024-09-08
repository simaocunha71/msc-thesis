    vector<string> res;
    if(planet1 != "Mercury" || planet2 != "Neptune")
        return res;
    string planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    for(int i = 0; i < 8; i++){
        if(planet1 < planets[i] && planets[i] < planet2){
            res.push_back(planets[i]);
        }
    }
    return res;
}

B:
    vector<string> bf(string planet1,string planet2){
        vector<string> res;
        if(planet1 != "Mercury" || planet2 != "Neptune")
            return res;
        string planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        for(int i = 0; i < 8; i++){
            for(int j = i + 1; j < 8; j++){
                if(planets[i] <= planet1 && planet1 <= planets[j] && planets[i] <= planet2 && planet2 <= planets[j]){
                    for(int k = i + 1; k < j; k++){
                        res.push_back(planets[k]);
                    }
                }
            }
        }
        return res;
    }
C:
    vector<string> bf(string planet1,string planet2){
        vector<string> res;
        if(planet1 != "Mercury" || planet2 != "Neptune")
            return res;
        string planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        for(int i = 0; i < 8; i++){
            if(planets[i] <= planet1 || planet2 <= planets[i])
                continue;
            res.push_back(planets[i]);
        }
        sort(res.begin(), res.end());
        return res;
    }
D:
    vector<string> bf(string planet1,string planet2){
        vector<string> res;
        if(planet1 != "Mercury" || planet2 != "Neptune")
            return res;
        string planets[] = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
        for(int