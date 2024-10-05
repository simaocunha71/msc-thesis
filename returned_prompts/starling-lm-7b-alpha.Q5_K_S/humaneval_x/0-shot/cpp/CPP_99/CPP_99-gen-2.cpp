    int n = atoi(value.c_str());
    if (n == 0)
        return 0;
    if (n > 0)
        return (int)ceil((double)n);
    else
        return (int)floor((double)n);
    if (n >= 0 && n < 10)
    {
        if (abs(n - 0) == abs(n - 1))
        {
            if (n > 0)
                return 1;
            else
                return 0;
        }
        if (abs(n - 0) == abs(n + 1))
        {
            if (n < 0)
                return -1;
            else
                return 0;
        }
        return n;
    }
    return n;
}




/*
The closest integer to 15.3 is 15, but the closest integer to 15.7 is 16.
This is because 15.3 is closer to 15 than it is to 16, but 15.7 is closer to 16 than it is to 15.
In other words, if the number is equidistant from two integers, round it away from zero.
The solution above correctly handles the case of 15.7, but incorrectly handles the case of 15.3.
To correct it, you need to add a conditional statement to handle the equidistant case.

Here's a corrected version of the function:

int closest_integer(string value) {
  int n = atoi(value.c_str());
  if (n == 0) {
    return 0;
  }
  if (n > 0) {
    return (int)ceil((double)n);
  } else {
    return (int)floor((double)n);
  }
  if (n >= 0 && n < 10) {
    if (abs(n - 0) == abs(n - 1)) {
      if (n > 0) {
        return 1;
      } else {
        return 0;
