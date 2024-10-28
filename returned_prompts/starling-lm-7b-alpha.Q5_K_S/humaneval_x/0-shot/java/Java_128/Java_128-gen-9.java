    int prod = 1;
    long sum = 0;
    for (int x : arr) {
      if (x == 0) {
        continue A;
      }
      if (x < 0) {
        prod *= -1;
      }
      sum += Math.abs(x);
    }
    if (arr.size() == 0) {
      return Optional.empty();
    }
    return Optional.of((int) (sum * prod));
  }
}










class Test {
  public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.prodSigns(Arrays.asList(1, 2, 2, -4)));
    System.out.println(solution.prodSigns(Arrays.asList(0, 1)));
    System.out.println(solution.prodSigns(Arrays.asList()));
  }
}




```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```