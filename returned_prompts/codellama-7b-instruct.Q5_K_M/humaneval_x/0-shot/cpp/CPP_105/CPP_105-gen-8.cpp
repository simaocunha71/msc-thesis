
  vector<int> result;
  vector<int> res;
  vector<string> res_str;
  int i = 0;
  int j = 0;

  if (arr.size() == 0) return {};
  sort(arr.begin(), arr.end());
  reverse(arr.begin(), arr.end());
  
  map<int, string> m = {
    {1, "One"},
    {2, "Two"},
    {3, "Three"},
    {4, "Four"},
    {5, "Five"},
    {6, "Six"},
    {7, "Seven"},
    {8, "Eight"},
    {9, "Nine"}
  };

  while (i < arr.size()){
    if (arr[i] >= 1 && arr[i] <= 9) {
      result.push_back(arr[i]);
      i++;
    } else {
      i++;
      goto A;
    }
  }
  for (int k = 0; k < result.size(); k++){
    res_str.push_back(m[result[k]]);
  }
  return res_str;
}

int main() {
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> result = by_length(arr);
  for (int i = 0; i < result.size(); i++){
    printf("%s ", result[i].c_str());
  }
}
