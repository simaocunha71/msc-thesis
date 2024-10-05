  vector<string> result;
  map<int, string> dict;
  dict[1] = "One";
  dict[2] = "Two";
  dict[3] = "Three";
  dict[4] = "Four";
  dict[5] = "Five";
  dict[6] = "Six";
  dict[7] = "Seven";
  dict[8] = "Eight";
  dict[9] = "Nine";

  for(int i = 0; i<arr.size(); i++){
    if(arr[i]>=1 && arr[i]<=9)
      result.push_back(dict[arr[i]]);
  }

  return result;
}

int main() {
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> result = by_length(arr);
  for(int i = 0; i<result.size(); i++){
    printf("%s\n", result[i].c_str());
  }
}
