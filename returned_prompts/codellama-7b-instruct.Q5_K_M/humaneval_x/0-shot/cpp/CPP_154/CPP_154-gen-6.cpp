  int flag=0;
  for(int i=0;i<a.length();i++){
    for(int j=0;j<b.length();j++){
      if(a[i+j]==b[j]){
        flag=1;
        continue;
      }
      else{
        flag=0;
        break;
      }
    }
    if(flag==1){
      return true;
    }
  }
  return false;
}
int main(){
  string a="whassup",b="psus";
  printf("result:%d",cycpattern_check(a,b));
  return 0;
}

