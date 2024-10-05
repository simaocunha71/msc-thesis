  vector<string> name = {"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"};
  vector<string> res;
  sort(arr.begin(), arr.end());
  reverse(arr.begin(), arr.end());
  for(int i=0; i<arr.size(); i++){
    if(arr[i]>=1 && arr[i]<=9)
      res.push_back(name[arr[i]]);
  }
  return res;
}

int main(){
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  return 0;
}

*/



// 3. 

/*

