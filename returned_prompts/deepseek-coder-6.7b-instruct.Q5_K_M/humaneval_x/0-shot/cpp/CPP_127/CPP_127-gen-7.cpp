  int start = max(interval1[0], interval2[0]);
  int end = min(interval1[1], interval2[1]);
  int len = end - start + 1;
B:
  if(len <= 1) return "NO";
C:
  for(int i = 2; i * i <= len; i++){
    if(len % i == 0) return "NO";
  }
  return "YES";
}

int main() {
  printf("%s\n", intersection({1, 2}, {2, 3}).c_str());
  printf("%s\n", intersection({-1, 1}, {0, 4}).c_str());
  printf("%s\n", intersection({-3, -1}, {-5, 5}).c_str());
  return 0;
}


