  sort(l.begin(), l.end());
  int n = l.size();
  int i = 0, j = n - 1;

B:
  while(i < j){
    if(l[i] + l[j] < 0){
      i++;
    }else if(l[i] + l[j] > 0){
      j--;
    }else{
      return true;
    }
  }
  return false;
}
int main(){
  vector<int> l = {2, 4, -5, 3, 5, 7};
  printf("%d", pairs_sum_to_zero(l));
  return 0;
