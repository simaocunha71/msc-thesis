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
	if((planet1 == "Mars" || planet1=="Venus")&&(planet2 == "Earth"||planet2="Mercury")){
	}else if(planet1.compare("Jupiter")==0 && (planet2.compare("Saturn")!=0 || planet2.compare("Uranus")!=0)) {
		for (int i=planet1.length();i<planet2.length();++i) if(isdigit((int)(planet2[i]))==0 && isupper((int)(planet2[i]))) planet2[i]=to_lower(planet2[i]);
	}else if((planet1 == "Earth"||planet1=="Mars")&&(planet2.compare("Saturn")!=0 || planet2.compare("Uranus")!=0)) {
	}else if(planet1.compare("Jupiter")==0) { //Same as the previous one, but in reverse order
	}
	return vector<string>{};
}
