  vector<int> temp = arr;
  sort(temp.begin(), temp.end());
  vector<string> res;
  for(int i = 0; i < temp.size(); i++){
    if(temp[i] < 1 || temp[i] > 9)
      continue;
    if(i != 0){
      if(temp[i] == temp[i-1]){
        continue;
      }
    }
    res.push_back("One");
  }
  return res;
}
int main(int argc, char* argv[]){
  vector<int> arr{2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for(int i = 0; i < res.size(); i++)
    printf("%s ", res[i].c_str());
  printf("\n");
  return 0;
}
