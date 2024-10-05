    int i;
    for (i=1;;i++)
    {
        if (pow(i,3)==a)
        return true;
        if (pow(i,3)>a)
        return false;
    }
} //Note: This code may not be efficient for large inputs, as it 
  //continuously calculates the cube of the number until it exceeds the input.
  //For efficiency, it is better to calculate the cube root of the number 
  //and check if it is an integer. Here is the improved code:
  bool iscuber(int a){
    int i;
    double cube_root = cbrt(a);
    return floor(cube_root+0.5) == cube_root;
  }
} //This improved code calculates the cube root of the number and checks if 
  //it is an integer by comparing it with its floor value. This is more efficient 
  //than the previous code and can handle large inputs.