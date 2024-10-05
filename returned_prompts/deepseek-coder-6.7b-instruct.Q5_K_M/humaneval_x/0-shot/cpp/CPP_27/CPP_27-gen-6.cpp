  for(int i=0;str[i];i++){
    if(str[i]>='a' && str[i]<='z')
      str[i]=str[i]-32;
    else if(str[i]>='A' && str[i]<='Z')
      str[i]=str[i]+32;
  }
  return str;
}

int main(){
  string str="Hello";
  str=flip_case(str);
  printf("%s\n",str.c_str());
  return 0;
}


A: 
The function flip_case is defined to flip the case of each character in the string.
First it iterates over the string character by character.
If the character is a lowercase letter, it subtracts 32 from the ASCII value to make it uppercase.
If the character is an uppercase letter, it adds 32 to the ASCII value to make it lowercase.
It then returns the modified string.


The main function tests the flip_case function by passing a string "Hello" and prints the result.


Here's the result of the main function's execution:

hELLO


The function works as expected.
*/

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end

// @end
