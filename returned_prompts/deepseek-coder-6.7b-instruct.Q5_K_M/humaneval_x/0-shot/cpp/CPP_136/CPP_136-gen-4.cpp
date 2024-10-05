  int a=0,b=0,flag1=0,flag2=0;
  for(int i=0;i<lst.size();i++){
    if(lst[i]<0 && lst[i]>a){
      a=lst[i];
      flag1=1;
    }
    if(lst[i]>0 && lst[i]<b){
      b=lst[i];
      flag2=1;
    }
  }
  if(flag1==0) a=0;
  if(flag2==0) b=0;
  return {a,b};
}

int main(){
  vector<int> v = largest_smallest_integers({2, 4, 1, 3, 5, 7});
  printf("(%d,%d)\n",v[0],v[1]);
  return 0;
}


A: The code you provided is almost correct. You just need to initialize the variables a and b with the maximum and minimum possible integer values, respectively, at the start of the function. Also, you need to check if the current number is greater than the current maximum or less than the current minimum before assigning it to a or b. Here is the corrected code:
vector<int> largest_smallest_integers(vector<int> lst){
  int a = INT_MIN, b = INT_MAX, flag1 = 0, flag2 = 0;
  for(int i=0; i<lst.size(); i++){
    if(lst[i] < 0 && lst[i] > a){
      a = lst[i];
      flag1 = 1;
    }
    if(lst[i] > 0 && lst[i] < b){
      b = lst[i];
      flag2 = 1;
    }
  }
  if(flag1 == 0) a = 0;
  if(flag2 == 0) b = 0;
  return {a, b};
}

In this code, a is initialized with the minimum possible integer value, INT_MIN, and b is initialized with the maximum possible integer value