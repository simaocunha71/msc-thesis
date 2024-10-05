vector<string> planets_order = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
vector<string> result;
int index1=-1, index2=-1;
for(int i=0; i<planets_order.size(); i++)
{
    if(planets_order[i] == planet1)
        index1 = i;
    if(planets_order[i] == planet2)
        index2 = i;
}
if(index1==-1 || index2==-1)
    return result;
if(index1 > index2)
{
    int temp = index1;
    index1 = index2;
    index2 = temp;
}
for(int i=index1+1; i<index2; i++)
{
    result.push_back(planets_order[i]);
}
return result;
}

int main(){
    vector<string> planets = bf("Jupiter", "Neptune");
    for(auto planet : planets){
        printf("%s\n", planet.c_str());
    }
    return 0;
}

*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> bf(string planet1, string planet2){
    vector<string> planets_order = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;
    int index1 = -1, index2 = -1;
    for(int i=0; i<planets_order.size(); i++){
        if(planets_order[i] == planet1)
            index1 = i;
        if(planets_order[i] == planet2)
            index2 = i;
    }
    if(index1==-1 || index2==-1)
        return result;
    if(index1 > index2){
        int temp = index1