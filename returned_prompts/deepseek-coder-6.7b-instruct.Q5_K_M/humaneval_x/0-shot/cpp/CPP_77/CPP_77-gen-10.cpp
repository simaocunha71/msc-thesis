  int cube = sqrt(a);
  return (cube*cube*cube == a);
}

int main() {
  printf("%d\n", iscuber(1));
  printf("%d\n", iscuber(2));
  printf("%d\n", iscuber(-1));
  printf("%d\n", iscuber(64));
  printf("%d\n", iscuber(0));
  printf("%d\n", iscuber(180));
  return 0;
}


A: You need to use cmath library to include sqrt() function. This function can be used to find the square root of a number. The cube root of a number a is the number b such that b*b*b = a. Hence, to check if a number is a cube of some number, we can find the cube root of the number and then check if the cube of that root equals the original number.
Here is the corrected code:
#include <iostream>
#include <cmath>

bool iscuber(int a)
{
    double cube_root = cbrt(a);
    return (round(cube_root) * round(cube_root) * round(cube_root) == a);
}

int main()
{
    std::cout << iscuber(1) << std::endl;
    std::cout << iscuber(2) << std::endl;
    std::cout << iscuber(-1) << std::endl;
    std::cout << iscuber(64) << std::endl;
    std::cout << iscuber(0) << std::endl;
    std::cout << iscuber(180) << std::endl;

    return 0;
}

Note that we use round() function to round the cube root to the nearest integer before cubing it to avoid possible precision errors.

A: The correct code to check if a number is a perfect cube is:
#include <iostream>
#include <cmath>

bool is_cube(int a) {
