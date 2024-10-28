  map<int, string> num2words;
  num2words[1] = "One";
  num2words[2] = "Two";
  num2words[3] = "Three";
  num2words[4] = "Four";
  num2words[5] = "Five";
  num2words[6] = "Six";
  num2words[7] = "Seven";
  num2words[8] = "Eight";
  num2words[9] = "Nine";

B:
  vector<int> filtered;
  for(int i = 0; i < arr.size(); i++){
    if(arr[i] >= 1 && arr[i] <= 9){
      filtered.push_back(arr[i]);
    }
  }

C:
  sort(filtered.begin(), filtered.end());
  reverse(filtered.begin(), filtered.end());

D:
  vector<string> result;
  for(int i = 0; i < filtered.size(); i++){
    result.push_back(num2words[filtered[i]]);
  }
  return result;
}
int main(){
  vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
  vector<string> res = by_length(arr);
  for(int i=0; i<res.size(); i++)
    printf("%s ", res[i].c_str());
  return 0;
}

// Output: Eight Five Four Three Two Two One One
*/

```


## Answer:
```cpp
