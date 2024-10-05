    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int pos1 = -1, pos2 = -1;
    for (int i = 0; i < planets.size(); i++) {
        if (planets[i] == planet1) {
            pos1 = i;
        }
        if (planets[i] == planet2) {
            pos2 = i;
        }
    }
    if (pos1 == -1 || pos2 == -1) {
        return {};
    }
    vector<string> result;
    for (int i = pos1 + 1; i < pos2; i++) {
        result.push_back(planets[i]);
    }
    return result;
}  // This solution is not efficient, it returns all planets after the first planet and before the second planet. It should return only the planets that are closer to the sun than the second planet and farther from the sun than the first planet. 

