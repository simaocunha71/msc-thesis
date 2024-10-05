  int i;
  if (x > y)
    return -1;
  for(i = y; i >= x; i--){
    if(i % 2 == 0)
      return i;
  }
  return -1;
}
int main() {
  printf("%d\n", choose_num(12, 15));  // 14
  printf("%d\n", choose_num(13, 12));  // -1
  return 0;
}

// Test Cases
// choose_num(12, 15)  -> 14
// choose_num(13, 12)  -> -1
// choose_num(14, 15)  -> 14
// choose_num(24, 31)  -> 30
// choose_num(28, 28)  -> 28
// choose_num(29, 30)  -> 30
// choose_num(10, 10)  -> 10
// choose_num(11, 13)  -> -1
// choose_num(20, 22)  -> 22
// choose_num(1, 10)   -> 10
// choose_num(5, 5)    -> 5
// choose_num(1, 2)    -> -1
// choose_num(3, 3)    -> -1
// choose_num(16, 23)  -> 22
// choose_num(9, 15)   -> 14
// choose_num(4, 5)    -> 4
// choose_num(0, 0)    -> 0
// choose_num(0, 2)    -> 2
// choose_num(0, 3)    -> 2
// choose_num(1, 3)    -> 2
// choose_num(2, 4)    -> 4
// choose_num(5, 15)   -> 10
// choose_num(15, 25)  -> 20