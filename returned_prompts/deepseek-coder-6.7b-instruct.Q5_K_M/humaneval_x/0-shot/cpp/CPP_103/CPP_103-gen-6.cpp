  if(n>m){
    return "-1";
  }

B:
  int sum=0,count=0;
  for(int i=n;i<=m;i++){
    sum+=i;
    count++;
  }

C:
  int avg=(int)round((double)sum/count);

D:
  return bitset<32>(avg).to_string();
}

*/

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>

char *rounded_avg(int n, int m) {
  if(n > m) {
    return "-1";
  }

  int sum = 0, count = 0, i;
  for(i = n; i <= m; i++) {
    sum += i;
    count++;
  }

  int avg = (int)round((double)sum/count);
  char *binary = (char *)malloc(33);
  itoa(avg, binary, 2);

  return binary;
}

int main() {
  int n = 1, m = 5;
  printf("%s\n", rounded_avg(n, m));
  n = 7, m = 5;
  printf("%s\n", rounded_avg(n, m));
  n = 10, m = 20;
  printf("%s\n", rounded_avg(n, m));
  n = 20, m = 33;
  printf("%s\n", rounded_avg(n, m));

  return 0;
}
```


## Answer:
The problem is asking to calculate the average of a range of numbers, round it to the nearest integer and then convert it to binary. If `n` is greater than `m`, return "-1".

The code below does this:

```c
#include<stdio.h>
#include<math.h>
#include<stdlib.h>

char *rounded_avg(int n, int m)