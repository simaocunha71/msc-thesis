    vector<string> planets = {"mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"};
    vector<string> result;
    int i1 = -1, i2 = -1;
    for (int i = 0; i < planets.size(); i++) {
        if (planets[i] == planet1) {
            i1 = i;
        }
        if (planets[i] == planet2) {
            i2 = i;
        }
    }
    if (i1 == -1 || i2 == -1) {
        return result;
    }
    if (i1 > i2) {
        return result;
    }
    for (int i = i1 + 1; i < i2; i++) {
        result.push_back(planets[i]);
    }
    sort(result.begin(), result