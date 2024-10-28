  for(int i=0; i<lst.size()-1; i++){
    if(lst[i]>=lst[i+1])
      return false;
  }
  return true;
}

int main() {
  printf("Hello World");
  return 0;
}
*/

// Write a program that reads a list of integers and checks if it's sorted in ascending order.

#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

bool is_sorted(vector<int> lst) {

    for (int i = 0; i < lst.size() - 1; i++) {
        if (lst[i] >= lst[i + 1])
            return false;
    }
    return true;
}

int main() {
    vector<int> numbers;
    int size, num;

    printf("Enter the size of the list: ");
    scanf("%d", &size);

    printf("Enter the elements of the list: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &num);
        numbers.push_back(num);
    }

    if (is_sorted(numbers))
        printf("The list is sorted in ascending order.\n");
    else
        printf("The list is not sorted in ascending order.\n");

    return 0;
}

// This program reads the size of the list and the elements of the list. It then checks if the list is sorted in ascending order using the function `is_sorted`. The result is then printed to the console.

// Please note that this program assumes that the input list has no more than one duplicate of the same number. If the list can have multiple duplicates, you will need to modify the `is_sorted` function to check for duplicates.

// Also, this program does not handle negative numbers or floating-point numbers. If you need to handle these cases, you will need to modify the `is_sorted` function accordingly.

// This program uses the C++ Standard Library, so you will need a C