  int a=0, b=0, flag1=0, flag2=0;
  for(int i=0; i<lst.size(); i++){
    if(lst[i]<0 && lst[i]>a) a=lst[i];
    if(lst[i]>0 && lst[i]<b) b=lst[i];
  }
  if(a==0) flag1=1;
  if(b==0) flag2=1;
  if(flag1==0 && flag2==0) return {a,b};
  else if(flag1==1 && flag2==1) return {0,0};
  else if(flag1==0 && flag2==1) return {a,0};
  else if(flag1==1 && flag2==0) return {0,b};
}

int main(){
    vector<int> lst = {2, 4, 1, 3, 5, 7};
    vector<int> result = largest_smallest_integers(lst);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}
*/

