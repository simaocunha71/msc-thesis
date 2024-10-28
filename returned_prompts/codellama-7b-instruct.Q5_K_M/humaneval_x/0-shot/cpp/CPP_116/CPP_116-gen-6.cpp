  int temp;
  int i, j;
  for (i = 0; i < arr.size(); i++) {
    for (j = i + 1; j < arr.size(); j++) {
      if (arr[j] < arr[i]) {
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
  return arr;
}

vector<int> sort_vector(vector<int> arr){
  vector<int> temp;
  for (int i = 0; i < arr.size(); i++) {
    temp.push_back(sort_array(arr).front());
    arr.erase(arr.begin());
  }
  return temp;
}

vector<int> sort_vector(vector<int> arr){
  int temp;
  int i, j;
  for (i = 0; i < arr.size(); i++) {
    for (j = i + 1; j < arr.size(); j++) {
      if (arr[j] < arr[i]) {
        temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
      }
    }
  }
  return arr;
}

vector<int> sort_vector(vector<int> arr){
  vector<int> temp;
  for (int i = 0; i < arr.size(); i++) {
    temp.push_back(sort_array(arr).front());
    arr.erase(arr.begin());
  }
  return temp;
}

vector<int> sort_vector(vector<int> arr){
  vector<int> temp;
  for (int i = 0; i < arr.size(); i++) {
    temp.push_back(sort_array(arr).front());
    arr.erase(arr.begin());
  }
  return temp;
}

vector<int> sort_vector(vector<int> arr){
  vector<int> temp;
  for (int i = 0; i < arr.size(); i