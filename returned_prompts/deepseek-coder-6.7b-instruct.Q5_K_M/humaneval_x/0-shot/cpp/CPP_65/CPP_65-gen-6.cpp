  char arr[5];
  sprintf(arr, "%d", x);
  int len = strlen(arr);
  if (shift > len) {
    for (int i = 0; i < len / 2; i++) {
      char temp = arr[i];
      arr[i] = arr[len - 1 - i];
      arr[len - 1 - i] = temp;
    }
  }
  else {
    char temp[5];
    strncpy(temp, arr + shift, len - shift);
    strncpy(temp + len - shift, arr, shift);
    temp[len] = '\0';
    strcpy(arr, temp);
  }
  return string(arr);
}

int main() {
  printf("%s\n", circular_shift(12, 1).c_str());
  printf("%s\n", circular_shift(12, 2).c_str());
  return 0;
}
```
This python program is based on the concept of circular shift in python.

The program takes an integer and a shift number as input. If shift is greater than the number of digits in the integer, the program reverses the digits of the integer. If not, it performs a circular shift to the right by the shift number and returns the result.
```python
#Python Program
#Circular Shift
def circular_shift(x, shift):
    x = str(x)
    len_x = len(x)
    if shift > len_x:
        return x[::-1]
    else:
        return x[-shift:] + x[:-shift]

print(circular_shift(12, 1))
print(circular_shift(12, 2))
```
This program works by converting the integer to a string. Then, it checks if the shift is greater than the number of digits in the integer. If it is, the program reverses the string and returns it. If not, it performs a circular shift to the right by the shift number and returns the result.

The time complexity of this program is O(n), where n is the number of digits in the integer. The space complexity