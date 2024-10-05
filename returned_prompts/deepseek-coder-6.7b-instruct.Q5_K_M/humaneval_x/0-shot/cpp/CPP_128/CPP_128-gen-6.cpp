  int n = arr.size();
  int sum = 0;
  int prod = 1;
  if(n == 0) return -32768;
  for(int i = 0; i < n; i++){
    if(arr[i] == 0){
      return 0;
    }
    else if(arr[i] < 0){
      arr[i] = abs(arr[i]);
      prod *= -1;
      sum += arr[i];
    }
    else{
      sum += arr[i];
    }
  }
  return sum * prod;
}

int main(){
  vector<int> arr {1,2,2,-4};
  printf("%d\n",prod_signs(arr));
  return 0;
}

*/

