  long long sum = 0;
  for(int i = 0; i < lst.size(); i++){
    if(lst[i] < 0 || (int)lst[i] != lst[i]){
      continue;
    }
    else if((int)lst[i] % 2 != 0){
      sum += pow((int)lst[i],2);
    }
  }
  return sum;
}

int main() {
  vector<float> lst = {1, 3, 2, 0};
  printf("%lld\n", double_the_difference(lst));
  return 0;
}

*/

// 3. Write a function that takes a list of numbers and returns a list of the squares of the numbers in the list that are odd. Ignore numbers that are negative or not integers.
// For example, if the input list is [1, 3, 2, 0], the output list should be [1, 9]. If the input list is [-1, -2, 0], the output list should be []. If the input list is [9, -2], the output list should be [81].
// If the input list is empty, return an empty list.

