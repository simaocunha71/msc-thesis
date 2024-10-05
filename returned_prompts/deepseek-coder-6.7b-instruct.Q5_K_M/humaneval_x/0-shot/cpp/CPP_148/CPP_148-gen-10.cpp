  vector<string> v = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  vector<string> res;
  for(int i=0;i<v.size();i++){
    if(v[i]==planet1){
      for(int j=i+1;j<v.size();j++){
        if(v[j]==planet2){
          for(int k=i+1;k<j;k++){
            res.push_back(v[k]);
          }
          return res;
        }
      }
    }
  }
  return res;
}

int main(){
  vector<string> res = bf("Jupiter", "Neptune");
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

Output:
Saturn Uranus 
Venus 
Venus Earth Mars Jupiter Saturn Uranus
*/

Explanation:
The task is to find all planets between two given planets. We can solve this by iterating through the planets vector and checking if we have found the first planet, then start adding the planets in the result vector until we find the second planet. If at any time we don't find either of the planets, we return an empty vector.
*/

#include <vector>
#include <string>
#include <map>
using namespace std;

vector<string> bf(string planet1, string planet2) {
    map<string, int> planets = {{"Mercury