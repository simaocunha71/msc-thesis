  vector<string> result;
  for(int i=0; i<arr.size(); i++){
    if(arr[i]>=1 && arr[i]<=9){
      result.push_back("One");
      result.push_back("Two");
      result.push_back("Three");
      result.push_back("Four");
      result.push_back("Five");
      result.push_back("Six");
      result.push_back("Seven");
      result.push_back("Eight");
      result.push_back("Nine");
    }
  }
  return result;
}

int main() {
  int num;
  vector<int> arr;
  while(scanf("%d", &num)){
    arr.push_back(num);
  }

  vector<string> result = by_length(arr);
  for(int i=0; i<result.size(); i++){
    printf("%s ", result[i].c_str());
  }
  return 0;
}
