  /*
  firstly, we need to check if the given lengths can form a triangle or not.
  The sum of lengths of any two sides should be greater than the length of the third side.
  */
  if (a + b > c && a + c > b && b + c > a){
    
B:
    /*
    Now, we need to check if the triangle is right-angled or not.
    For a right-angled triangle, squares of the lengths of two sides should be equal to the square of the length of the third side.
    */
    if(pow(a,2) + pow(b,2) == pow(c,2) || pow(a,2) + pow(c,2) == pow(b,2) || pow(b,2) + pow(c,2) == pow(a,2)){
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

int main() {
  printf("%d", right_angle_triangle(3, 4, 5));
  printf("%d", right_angle_triangle(1, 2, 3));
  return 0;
}

*/

/*
In the above code, we firstly checked whether the given lengths can form a triangle or not. The sum of lengths of any two sides should be greater than the length of the third side. If not, we return false.
If yes, then we checked whether the triangle is right-angled or not. For a right-angled triangle, squares of the lengths of two sides should be equal to the square of the length of the third side. If yes, we return true. If not, we return false.
*/

// Solution End

int main() {
    cout<<right_angle_triangle(3, 4, 5)<<endl;
    cout<<right_angle_triangle(1, 2, 3)<<endl;
    return 0;
}

// Solution End

int main() {
    cout<<right_angle_triangle(3, 4, 5)<<endl;
    cout<<right_angle_triangle(1, 2, 