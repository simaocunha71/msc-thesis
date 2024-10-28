  int b = sqrt(a);
  return b*b*b == a;
}
int main(){
  printf("%d",iscuber(64));
  return 0;
}

Answer:
The function iscuber checks if a given integer is a cube of some integer number by taking the cube root of the integer and checking if the cube of this root equals the original integer. It uses the math library's sqrt function to get the cube root, and the == operator to compare the cube of the root to the original integer. The function returns true if the cube of the root equals the original integer, and false otherwise.

In the function main(), we call the function iscuber with the argument 64. The function returns true, so the program prints 1.

So, the integer 64 is a cube of 4, so the function returns true.
*/

// C++ program to solve the problem
#include<iostream>
#include<cmath>
using namespace std;

bool iscuber(int a){
  int b = cbrt(a);
  return b*b*b == a;
}

int main(){
  cout<<iscuber(64)<<endl;
  return 0;
}

/*
Output:
1
*/

In the code above, we use the cbrt function to get the cube root of a number. The cbrt function is a part of the cmath library in C++. The function cbrt takes a double as argument and returns the cube root of the number. In our case, we are passing an integer to the function, so it returns an integer. We then check if the cube of this root is equal to the original integer. If it is, we return true, otherwise we return false. In the main function, we call this iscuber function with the argument 64 and print the result.

The output of the program is 1, which is true in C++, indicating that 64 is a cube of 4.

Please note that the cbrt function is not available in C. In that case, you can use the pow function to raise the number to the third power and then compare it with the original number