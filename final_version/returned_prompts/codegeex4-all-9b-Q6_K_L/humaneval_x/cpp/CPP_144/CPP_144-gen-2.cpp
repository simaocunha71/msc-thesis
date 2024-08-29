#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>
using namespace std;

bool simplify(string x, string n) {
    stringstream ss(x);
    vector<string> tokens;
    string token;
    while (getline(ss, token, '/')) {
        tokens.push_back(token);
    }
    int numeratorX = stoi(tokens[0]);
    int denominatorX = stoi(tokens[1]);

    stringstream ss2(n);
    vector<string> tokens2;
    while (getline(ss2, token, '/')) {
        tokens2.push_back(token);
    }
    int numeratorN = stoi(tokens2[0]);
    int denominatorN = stoi(tokens2[1]);

    // Multiply the numerators and denominators
    int numeratorResult = numeratorX * numeratorN;
    int denominatorResult = denominatorX * denominatorN;

    // Check if the result is a whole number
    return numeratorResult % denominatorResult == 0;
}

int main() {
    cout << simplify("1/5", "5/1") << endl; // true
    cout << simplify("1/6", "2/1") << endl; // false
    cout << simplify("7/10", "10/2") << endl; // false
    return 0;
}
B:
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

bool simplify(string x, string n) {
    int numeratorX = 0;
    int denominatorX = 0;
    int numeratorN = 0;
    int denominatorN = 0;
    stringstream ss(x);
    ss >> numeratorX >> denominatorX;
    stringstream ss2(n);
    ss2 >> numeratorN >> denominatorN;

    int numeratorResult = numeratorX * numeratorN;
    int denominatorResult = denominatorX * denominatorN;

    return numeratorResult % denominatorResult == 0;
}

int main() {
    cout << simplify("1/5", "5/1") << endl; // true
    cout << simplify("1/6", "2/1") << endl; // false
    cout << simplify("7/10", "10/2") << endl; // false
    return 0;
}
C:
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>
using namespace std;

bool simplify(string x, string n) {
    stringstream ss(x);
    vector<string> tokens;
    string token;
   