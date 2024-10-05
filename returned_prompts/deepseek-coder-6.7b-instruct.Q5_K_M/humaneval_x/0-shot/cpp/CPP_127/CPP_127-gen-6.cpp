/*
Start with the cases when the intervals don't intersect.
Check if the end of the first interval is less than the start of the second one.
If yes, there is no intersection, so return "NO".
If not, calculate the start and end of the intersection.
Then calculate the length of the intersection.
Check if the length is a prime number.
*/
  if(interval1[1] < interval2[0] || interval2[1] < interval1[0])
    return "NO";

  int start = max(interval1[0], interval2[0]);
  int end = min(interval1[1], interval2[1]);
  int length = end - start + 1;

  if(length < 2) 
    return "NO";

  for(int i = 2; i * i <= length; i++){
    if(length % i == 0)
      return "NO";
  }
  return "YES";
}

int main() {
  vector<int> interval1 = {1, 2};
  vector<int> interval2 = {2, 3};
  printf("%s\n", intersection(interval1, interval2).c_str());

  vector<int> interval3 = {-1, 1};
  vector<int> interval4 = {0, 4};
  printf("%s\n", intersection(interval3, interval4).c_str());

  vector<int> interval5 = {-3, -1};
  vector<int> interval6 = {-5, 5};
  printf("%s\n", intersection(interval5, interval6).c_str());

  return 0;
}
/*
You should get "NO", "NO", "YES".
*/




































































































