  for(int i = 0; i < lst.size()-1; i++){
    if(lst[i] > lst[i+1]){
      return false;
    }
  }
  return true;
}

int main(){
  vector<int> v = {1, 2, 2, 2, 3, 4};
  if(is_sorted(v)){
    printf("True\n");
  }else{
    printf("False\n");
  }
  return 0;
}

// ➞ false

Explanation: 
The given vector has duplicate numbers (2, 2, 2). Therefore, it returns false.
*/


/*
