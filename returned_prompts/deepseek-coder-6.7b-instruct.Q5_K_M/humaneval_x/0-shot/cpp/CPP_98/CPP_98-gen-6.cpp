  int counter = 0;
  for (int i = 0; i < strlen(s); i += 2){
    if (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
      counter++;
    }
  }
  return counter;
}

int main() {
  char *s = "dBBE";
  printf("%d", count_upper(s));
  return 0;
}

Output:
0
*/

```

### C++

```C++
