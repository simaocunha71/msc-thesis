  vector<string> result;
  vector<string> solarSystem{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  auto it1 = find(solarSystem.begin(), solarSystem.end(), planet1);
  auto it2 = find(solarSystem.begin(), solarSystem.end(), planet2);
  if(it1==solarSystem.end()||it2==solarSystem.end()) return result;
  if(it1>it2) swap(it1,it2);
  for(auto it=it1+1; it<it2; ++it)
    result.push_back(*it);
  return result;
}

int main() {

  vector<string> res;
  res = bf("Jupiter", "Neptune");
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  printf("\n");
  
  res = bf("Earth", "Mercury");
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  printf("\n");

  res = bf("Mercury", "Uranus");
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  printf("\n");

  return 0;
}

*/

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> bf(string planet1, string planet2){
  vector<string> result;
  vector<string> solarSystem{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  
  auto it1 = find(solarSystem.begin(), solarSystem.end(), planet1);
  auto it2 = find(solarSystem.begin(), solarSystem.end(), planet2);