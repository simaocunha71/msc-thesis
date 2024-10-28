  int len = str.size();
  if (len < 2) return false;
  for (int i = 2; i * i <= len; ++i) {
    if (len % i == 0) return false;
  }
  return true;
}
int main(){
  printf(prime_length("Hello") ? "true" : "false");
  printf(prime_length("abcdcba") ? "true" : "false");
  printf(prime_length("kittens") ? "true" : "false");
  printf(prime_length("orange") ? "true" : "false");
}
```

This program defines a function `prime_length()` that checks if the length of a string is a prime number. It first gets the length of the string, checks if the length is less than 2, then it checks if the length is divisible by any number from 2 to the square root of the length. If any of these conditions are met, it returns false; otherwise, it returns true.

It then uses the `main()` function to test the `prime_length()` function with the strings "Hello", "abcdcba", "kittens", and "orange".

The `printf()` function is used to print the result of the `prime_length()` function, converting it to a string. If `prime_length()` returns true, it will print "true"; otherwise, it will print "false".

The output of this program would be:
```
true
true
true
false
```
which corresponds to the examples in the problem statement.
*/

int main() {
    string s1 = "Hello";
    string s2 = "abcdcba";
    string s3 = "kittens";
    string s4 = "orange";

    printf(prime_length(s1) ? "true" : "false");
    printf(prime_length(s2) ? "true" : "false");
    printf(prime_length(s3) ? "true" : "false");
    printf(prime_length(s4) ? "true" : "false");

    return 0;
}

int main() {
    string s1 = "Hello";
