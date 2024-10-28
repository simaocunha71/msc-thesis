

  int i;
  int sum=0;
  for(i=0;i<lst.size();i++){
    if(i%3==0){
      lst[i]=lst[i]*lst[i];
    }
    else if(i%4==0 && i%3!=0){
      lst[i]=lst[i]*lst[i]*lst[i];
    }
    sum=sum+lst[i];
  }
  return sum;
}
 
 
int main(){
  vector<int> lst;
  int i;
  for(i=0;i<3;i++){
    int a;
    scanf("%d",&a);
    lst.push_back(a);
  }
  printf("%d\n",sum_squares(lst));
  return 0;
}

