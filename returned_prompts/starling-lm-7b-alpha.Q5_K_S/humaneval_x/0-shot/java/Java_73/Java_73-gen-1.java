    int left = 0;
    int right = arr.size() - 1;
    int res = 0;
    while (left < right) {
      int l = arr.get(left);
      int r = arr.get(right);
      if (l == r) {
        left++;
        right--;
        continue A;
      } else if (l > r) {
        while (left < right && arr.get(left) >= r) {
          left++;
        }
        if (left >= right) {
          return res;
        }
        arr.set(left, r);
        res++;
      } else {
        while (left < right && arr.get(right) >= l) {
          right--;
        }
        if (left >= right) {
          return res;
        }
        arr.set(right, l);
        res++;
      }
    }
    return res;
  }
}






























































































































































































































































































