  vector<string> result;
  vector<int> nums;
  map<int, string> m;
  m[1] = "One";
  m[2] = "Two";
  m[3] = "Three";
  m[4] = "Four";
  m[5] = "Five";
  m[6] = "Six";
  m[7] = "Seven";
  m[8] = "Eight";
  m[9] = "Nine";
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] == 0) {
      continue;
    }
    if (arr[i] >= 1 && arr[i] <= 9) {
      nums.push_back(arr[i]);
    }
  }
  sort(nums.begin(), nums.end(), greater<int>());
  for (int i = 0; i < nums.size(); i++) {
    result.push_back(m[nums[i]]);
  }
  return result;
}

vector<string> by_name(vector<int> arr){
  vector<string> result;
  map<int, string> m;
  m[1] = "One";
  m[2] = "Two";
  m[3] = "Three";
  m[4] = "Four";
  m[5] = "Five";
  m[6] = "Six";
  m[7] = "Seven";
  m[8] = "Eight";
  m[9] = "Nine";
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] == 0) {
      continue;
    }
    if (arr[i] >= 1 && arr[i] <= 9) {
      result.push_back(m[arr[i]]);
    }
  }
  return result;
}

vector<string> digit_name(vector<int> arr){
  vector<string> result;
  for (