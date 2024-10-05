  for(int i=0; i<lst.size()-1; i++){
    if(lst[i] >= lst[i+1]) return false;
  }
  return true;
}

int main(){
  vector<int> vec1 = {5};
  vector<int> vec2 = {1, 2, 3, 4, 5};
  vector<int> vec3 = {1, 3, 2, 4, 5};
  vector<int> vec4 = {1, 2, 3, 4, 5, 6};
  vector<