  vector<string> result;
  vector<string> planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  int pos1=-1, pos2=-1;
  for(int i=0; i<planets.size(); i++){
    if(planets[i] == planet1) pos1 = i;
    if(planets[i] == planet2) pos2 = i;
  }
  if(pos1 == -1 || pos2 == -1) return result;
  if(pos1 > pos2){
    int temp = pos1;
    pos1 = pos2;
    pos2 = temp;
  }
  for(int i=pos1+1; i<pos2; i++){
    result.push_back(planets[i]);
  }
  return result;
}


*/
#include <vector>
#include <string>
using namespace std;

vector<string> bf(string planet1, string planet2) {
  vector<string> planets{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  vector<string> res;

  auto it1 = find(planets.begin(), planets.end(), planet1);
  auto it2 = find(planets.begin(), planets.end(), planet2);

  if (it1 == planets.end() || it2 == planets.end())
    return res;

  if (it1 > it2)
    swap(it1, it2);

  for (auto it = it1 + 1; it < it2; ++it)
    res.push_back(*it);

  return res;
}


int main() {
  vector<string> res = bf("Jupiter", "Neptune");
  for (auto &s : res)
    cout << s << " ";

  return 0;
}

*/

















