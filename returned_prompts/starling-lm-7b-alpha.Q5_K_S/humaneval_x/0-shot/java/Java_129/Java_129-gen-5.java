        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid.get(i).size(); ++j) {
                if (grid.get(i).get(j) == 1) {
                    List<Integer> res = new ArrayList<>();
                    int i1 = i, j1 = j;
                    for (int l = 0; l < k; ++l) {
                        res.add(grid.get(i1).get(j1));
                        Set<Pair> set = new HashSet<>();
                        set.add(new Pair(i1, j1));
                        if (i1 > 0 && !set.contains(new Pair(i1 - 1, j1))) {
                            i1--;
                        } else if (j1 > 0 && !set.contains(new Pair(i1, j1 - 1))) {
                            j1--;
                        } else if (i1 < grid.size() - 1 && !set.contains(new Pair(i1 + 1, j1))) {
                            i1++;
                        } else if (j1 < grid.get(i1).size() - 1 && !set.contains(new Pair(i1, j1 + 1))) {
                            j1++;
                        } else {
                            continue A;
                        }
                    }
                    return res;
                }
            }
        }
        return null;
    }

    class Pair {
        int i;
        int j;
        Pair(int i, int j) {
            this.i = i;
            this.j = j;
        }
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

