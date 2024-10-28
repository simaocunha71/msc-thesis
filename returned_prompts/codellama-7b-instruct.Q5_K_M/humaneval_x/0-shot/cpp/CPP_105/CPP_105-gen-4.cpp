  vector<string> res;
  map<int, string> dict = {
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
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      res.push_back(dict[arr[i]]);
    }
  }
  sort(res.begin(), res.end(), [](string a, string b){return a < b;});
  reverse(res.begin(), res.end());
  return res;
}

