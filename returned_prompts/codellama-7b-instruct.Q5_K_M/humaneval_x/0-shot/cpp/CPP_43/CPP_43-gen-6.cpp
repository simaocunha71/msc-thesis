  if (l.size() <= 1)
    return false;
  for (int i = 0; i < l.size() - 1; i++) {
    for (int j = i + 1; j < l.size(); j++) {
      if (l[i] + l[j] == 0)
        return true;
    }
  }
  return false;
}
int main() {
  vector<int> v = {1, 3, 5, 0};
  bool b = pairs_sum_to_zero(v);
  printf("%d\n", b);
  return 0;
}