  int prime = 0;
  int sum = 0;
  for(int i = 0; i<lst.size(); i++){
    if(lst[i] > prime){
      prime = lst[i];
    }
  }
  string str = to_string(prime);
  for(int i = 0; i<str.length(); i++){
    sum += str[i] - '0';
  }
  return sum;
}

int main() {
  vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
  printf("%d", A(lst));
  return 0;
}
*/

