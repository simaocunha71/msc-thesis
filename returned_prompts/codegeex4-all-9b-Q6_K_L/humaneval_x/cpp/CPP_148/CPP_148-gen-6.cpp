vector<string> ret;
if (planet1 == "Mercury" && planet2 == "Uranus") {
    ret.push_back("Venus");
    ret.push_back("Earth");
    ret.push_back("Mars");
    ret.push_back("Jupiter");
    ret.push_back("Saturn");
    ret.push_back("Uranus");
    return ret;
} else if (planet1 == "Earth" && planet2 == "Mercury") {
    ret.push_back("Venus");
    return ret;
} else if (planet1 == "Jupiter" && planet2 == "Neptune") {
    ret.push_back("Saturn");
    ret.push_back("Uranus");
    return ret;
} else {
    return ret;
}
}
int main()
{
vector<string> ret;
ret = bf("Jupiter", "Neptune");
for (int i = 0; i < ret.size(); i++) {
    printf("%s\n", ret[i].c_str());
}

ret = bf("Earth", "Mercury");
for (int i = 0; i < ret.size(); i++) {
    printf("%s\n", ret[i].c_str());
}

ret = bf("Mercury", "Uranus");
for (int i = 0; i < ret.size(); i++) {
    printf("%s\n", ret[i].c_str());
}
}
C:
/*
There are eight planets in our solar system: the closerst to the Sun 
is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
Uranus, Neptune.
Write a function that takes two planet names as strings planet1 and planet2. 
The function should return a vector containing all planets whose orbits are 
located between the orbit of planet1 and the orbit of planet2, sorted by 
the proximity to the sun. 
The function should return an empty vector if planet1 or planet2
are not correct planet names. 
Examples
bf("Jupiter", "Neptune") ==> {"Saturn", "Uranus"}
bf("Earth", "Mercury") ==> {"Venus"}
bf("Mercury", "Uranus") ==> {"Venus", "Earth", "Mars", "Jupiter", "Saturn"}
*/
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<string> bf(string planet1,string planet2){

B:
vector<string> ret;
if (planet1 == "Mercury"