
*/

#include <bits/stdc++.h>
using namespace std;

vector<string> bf(string planet1, string planet2) {
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> res;
    int i = 0;
    while (planets[i] != planet1) {
        if (planets[i] == planet2) return res;
        i++;
    }
    for (; i < planets.size(); i++) {
        if (planets[i] != planet2) res.push_back(planets[i]);
    }
    return res;
}

int main() {
    printf("%s\n", bf("Jupiter", "Neptune").data());
    printf("%s\n", bf("Earth", "Mercury").data());
    printf("%s\n", bf("Mercury", "Uranus").data());
    return 0;
}

*/




























