    vector<string> result;
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    int i = 0, j = 0;
    while(i < planets.size() && j < planets.size()) {
        if(planets[i] == planet1) {
            while(j < planets.size() && planets[j] != planet2) {
                j++;
            }
            if(j == planets.size()) {
                j--;
            }
            for(int k = i + 1; k < j; k++) {
                result.push_back(planets[k]);
            }
            break;
        }
        i++;
    }
    sort(result.begin(), result.end());
    return result;
}
int main() {
    printf("%s\n", bf("Jupiter", "Neptune").size() == 1 ? "": "");
    printf("%s\n", bf("Earth", "Mercury").size() == 1 ? "": "");
    printf("%s\n", bf("Mercury", "Uranus").size() == 5 ? "": "");
    return 0;
} 
