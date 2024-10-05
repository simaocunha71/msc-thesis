  if(arr.empty()) return -32768;

B:
  int product_sign = 1;
  int sum = 0;

C:
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] < 0)
      product_sign *= -1;
    else if (arr[i] > 0)
      product_sign *= 1;
    sum += abs(arr[i]);
  }

D:
  return product_sign * sum;
}

int main(){
  vector<int> arr = {1, 2, 2, -4};
  printf("%d\n", prod_signs(arr));
  return 0;
}

*/

int main(){
  vector<int> arr = {1, 2, 2, -4};
  printf("%d\n", prod_signs(arr));
  return 0;
}

//C++/main.cpp
#include<stdio.h>
#include<math.h>
#include<vector>
using namespace std;
int prod_signs(vector<int> arr){

  if(arr.empty()) return -32768;

  int product_sign = 1;
  int sum = 0;

  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] < 0)
      product_sign *= -1;
    else if (arr[i] > 0)
      product_sign *= 1;
    sum += abs(arr[i]);
  }

  return product_sign * sum;
}

int main(){
  vector<int> arr = {1, 2, 2, -4};
  printf("%d\n", prod_signs(arr));
  return 0;
}

//C++/test.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "main.cpp"

TEST_CASE("Testing the prod