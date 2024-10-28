  int temp = 0;
  vector<int> result;
  for(int i = a; i <= b; i++){
    temp = i % 10;
    if(temp % 2 == 0)
      result.push_back(temp);
  }
  return result;
}
int main(void){
  int a,b;
  printf("input a and b:\n");
  scanf("%d%d",&a,&b);
  vector<int> result = generate_integers(a,b);
  for(int i = 0;i<result.size();i++){
    printf("%d ",result[i]);
  }
  return 0;
}
