
  int count[2] = {0, 0};
  int temp = num;
  while(temp>0){
    int last_digit = temp%10;
    temp/=10;
    if(last_digit%2==0){
      count[0]++;
    } else {
      count[1]++;
    }
  }
  return count;
}

