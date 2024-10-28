  int start,end,i;
  vector<int> even_numbers;
  if(a>b){
    start = b;
    end = a;
  }else{
    start = a;
    end = b;
  }
  for(i=start;i<=end;i++){
    if(i%2==0){
      even_numbers.push_back(i);
    }
  }
  return even_numbers;
}

int main() {
  vector<int> numbers;
  numbers = generate_integers(2,8);
  for(int i=0;i<numbers.size();i++){
    printf("%d ",numbers[i]);
  }
  return 0;
}

*/

