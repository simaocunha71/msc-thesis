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
	if(planet1 == planet2) return {};
	string planetOrder[8] = {"Mercury", "Venus","Earth","Mars","Jupiter","Saturn","Uranus", "Neptune"};
	int i = 0;
	vector<string> vec;
	while(i < 8 && planetOrder[planet1] == planet2) {
	    i++;
	}
	if(i >= 8){
        return {};
    }
	while(i < 8&& (planetOrder[planet1] != planet2)) {
		vec.push_back(planets[planetOrder[planet1]]);
	    i++;
	}
	int j = 0;
	while(j < vec.size() && (planetOrder[planet2] != planets[vec.at(i)])) {
		vec.erase(vec.begin()+j++);
        }
    if(j == 0) return {};
	while(j > 0){
		vec.insert