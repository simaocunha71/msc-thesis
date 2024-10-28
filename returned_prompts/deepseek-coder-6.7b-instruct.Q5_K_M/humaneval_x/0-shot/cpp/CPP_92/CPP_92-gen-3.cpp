  if(a==round(a) && b==round(b) && c==round(c)){

    if(a==b+c || b==a+c || c==a+b){
      return true;
    }
    else{
      return false;
    }
  }
  else{
    return false;
  }
}
int main(){
  printf("%d",any_int(5,2,7));
  printf("%d",any_int(3,2,2));
  printf("%d",any_int(3,-2,1));
  printf("%d",any_int(3.6,-2.2,2));
  return 0;
}


A: It seems you're trying to solve a problem which requires knowledge of conditions, equality checking and integer checking in programming. Your function seems to be correct according to the problem statement. The function any_int takes three numbers as input, checks if all of them are integers, and then checks if one of the numbers is equal to the sum of the other two. If these conditions are met, it returns true; otherwise, it returns false. 

The line if(a==round(a) && b==round(b) && c==round(c)) is used to check if all numbers are integers. The round function returns the nearest integer value to the argument passed. 

The line if(a==b+c || b==a+c || c==a+b) is used to check if one of the numbers is equal to the sum of the other two. 

In the main function, you're calling the function with different arguments and printing the result. The printf function is used to print the result of the function call.

Your code seems to be correctly written and it should work as expected.

Please check the logic of your code and make sure you understand it. If you have any further questions, feel free to ask.

I hope this helps.


A: You can solve this problem using programming logic. Here is a simple program in Python:

```python
def any_int(a, b, c):
    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        if a + b == c or a