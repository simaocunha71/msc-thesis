  int len_a=a.length();
  int len_b=b.length();
  string result="";
  int max_len=(len_a>len_b)?len_a:len_b;
  // To make both strings of equal length by padding with 0s
  while(len_a<max_len){
    a='0'+a;
    len_a++;
  }
  while(len_b<max_len){
    b='0'+b;
    len_b++;
  }
  // Performing XOR operation
  for(int i=0;i<max_len;i++){
    if(a[i]==b[i])
      result+='0';
    else
      result+='1';
  }
  // Remove leading 0s
  while(result[0]=='0' && result.length()>1){
    result.erase(0,1);
  }
  return result;
}


int main(){
  string a="010";
  string b="110";
  printf("%s",string_xor(a,b).c_str());
}


A: If you are using Python, you can use the built-in function map() and join() to solve this problem:
```
def string_xor(a, b):
    return ''.join(map(lambda x, y: str(int(x)^int(y)), a, b))
```

This function works by mapping a lambda function to each pair of corresponding characters in a and b. The lambda function performs a bitwise XOR operation on the integer representations of the characters. The map() function returns a list of results, which is then joined into a string.

The function first converts each string to a list of characters using the list() function. It then uses the zip() function to create an iterator that aggregates elements from each of the iterables. The iterator is used in the map() function to create a new list by applying the lambda function to each pair of elements.

Finally, the list is joined into a string using the join() function.

This function