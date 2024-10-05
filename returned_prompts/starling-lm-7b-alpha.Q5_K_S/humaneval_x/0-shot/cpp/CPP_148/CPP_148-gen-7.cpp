    vector<string> planets={"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> res;
    if (planet1=="Mercury" && planet2=="Neptune"){
        for (int i=0;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Mercury" && planet2=="Uranus") {
        for (int i=1;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Uranus" && planet2=="Neptune") {
        for (int i=6;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Venus" && planet2=="Neptune") {
        for (int i=1;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Venus" && planet2=="Mars") {
        for (int i=2;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Mars" && planet2=="Jupiter") {
        for (int i=3;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Jupiter" && planet2=="Saturn") {
        for (int i=4;i<planets.size();i++){
            res.push_back(planets[i]);
        }
    } else if (planet1=="Saturn" && planet2=="Uranus") {
        for (int i=5;i<planets.size();i++){
            res.push_back(planets[i