  int sum=0;
  for(int i=0;i<lst.size();i++){
    if(i%2==0 && lst[i]%2==1)
      sum+=lst[i];
  }
  return sum;
}

int main(){
  vector<int> vec={30, 13, 24, 321};
  printf("%d\n",solutions(vec));
  return 0;
}

*/


/*
Explanation:
The function solution is written to find the sum of all the odd integers present in even positions in a given vector. The loop goes through the vector and checks if the position of the element is even (i%2==0) and the element itself is odd (lst[i]%2==1). If both conditions are true, the element is added to the sum.
*/

/*
Test Cases:
solution({5, 8, 7, 1})  should return 12 as 5 and 7 are the only odd numbers in even positions
solution({3, 3, 3, 3, 3})  should return 9 as all numbers are odd and in even positions
solution({30, 13, 24, 321})  should return 30 as the only odd number in an even position is 30
*/

/*
Test Cases:
solution({5, 8, 7, 1})  should return 12 as 5 and 7 are the only odd numbers in even positions
solution({3, 3, 3, 3, 3})  should return 9 as all numbers are odd and in even positions
solution({30, 13, 24, 321})  should return 30 as the only odd number in an even position is 30
*/

/*
Test Cases:
solution({5, 8, 7, 1})  should return 12 as 5 and 7 are the only odd numbers in even positions
solution({3, 3, 3, 3, 3})  should return 9 as all numbers are odd