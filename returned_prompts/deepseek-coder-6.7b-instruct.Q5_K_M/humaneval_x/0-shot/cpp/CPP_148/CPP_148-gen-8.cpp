  vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  vector<string> result;

B:
  if(find(planets.begin(), planets.end(), planet1) == planets.end() || find(planets.begin(), planets.end(), planet2) == planets.end())
    return {};

C:
  int index1 = find(planets.begin(), planets.end(), planet1) - planets.begin();
  int index2 = find(planets.begin(), planets.end(), planet2) - planets.begin();

D:
  if(index1 > index2)
    swap(index1, index2);

E:
  for(int i=index1+1; i<index2; i++)
    result.push_back(planets[i]);

F:
  return result;
}
int main()
{
  vector<string> res = bf("Jupiter", "Neptune");
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  return 0;
}

*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string> bf(string planet1, string planet2){
    vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
    vector<string> result;

    auto it1 = find(planets.begin(), planets.end(), planet1);
    auto it2 = find(planets.begin(), planets.end(), planet2);

    if(it1 == planets.end() || it2 == planets.end())
        return {};

    if(it1 > it2)
        swap(it1, it2);

    it1++;
    while(it1 != it2){
        result.push_back(*it1);
        it1++;