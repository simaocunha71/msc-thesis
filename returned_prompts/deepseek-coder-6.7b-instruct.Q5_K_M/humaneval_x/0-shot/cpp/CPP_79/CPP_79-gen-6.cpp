  string binary = "db";
  while(decimal > 0){
    binary = to_string(decimal % 2) + binary;
    decimal /= 2;
  }
  binary += "db";
  return binary;
}


int main() {
  printf("Test case 1: %s\n", decimal_to_binary(15).c_str());
  printf("Test case 2: %s\n", decimal_to_binary(32).c_str());
  return 0;
}
```

##### Answer:
```cpp
