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

    vector<string> planets={"Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"};
    vector<string> result;
    int i=0;
    int j=0;
    int k=0;
    int l=0;
    for(i=0;i<planets.size();i++){
        if(planet1==planets[i]){
            j=i;
        }
    }
    for(i=0;i<planets.size();i++){
        if(planet2==planets[i]){
            k=i;
        }
    }
    if(j>k){
        l=j;
        j=k;
        k=l;
    }
    if(j<0||k>planets.size()-1){
        return result;
    }
    for(i=j+1;i<k;i++){
        result.push_back(planets[i]);
    }
    return result;
}
