  vector<string> planets{"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
  vector<string> result;
  int pos1=-1,pos2=-1;
  for(int i=0;i<planets.size();i++){
    if(planets[i]==planet1) pos1=i;
    if(planets[i]==planet2) pos2=i;
  }
  if(pos1==-1||pos2==-1) return result;
  if(pos1>pos2){
    int temp=pos1;
    pos1=pos2;
    pos2=temp;
  }
  for(int i=pos1+1;i<pos2;i++){
    result.push_back(planets[i]);
  }
  return result;
}



int main(){

  vector<string> res=bf("Jupiter", "Neptune");
  for(int i=0;i<res.size();i++){
    printf("%s ",res[i].c_str());
  }
  printf("\n");

  res=bf("Earth", "Mercury");
  for(int i=0;i<res.size();i++){
    printf("%s ",res[i].c_str());
  }
  printf("\n");

  res=bf("Mercury", "Uranus");
  for(int i=0;i<res.size();i++){
    printf("%s ",res[i].c_str());
  }
  printf("\n");

  return 0;
}

*/


// Solution Explanation:
The solution first declares a vector with the names of the planets in their proximity to the Sun. 
Then it finds the positions of planet1 and planet2 in this vector. If either of the planets is not found, the function returns an empty vector.
If the positions of the planets are found, the function sorts them if necessary and then pushes all planets between them into the result vector. 
The result vector is