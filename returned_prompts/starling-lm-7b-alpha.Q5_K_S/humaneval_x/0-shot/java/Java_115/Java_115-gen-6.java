        // idea: simulate bucket filling process, each bucket fills at most capacity times,
        // each bucket can only fill the rightmost 1's, which are at most capacity times,
        // and each well can only be filled at most capacity times, so the total number of times is min(capacity * (capacity + 1) / 2, grid.size())
        int m = grid.size(), n = grid.get(0).size();
        int total = 0, curr = 0, curr_bucket = 0;
        while (curr < m) {
            // fill each well with at most capacity times
            for (int j = 0; j < n && curr < m; ++j) {
                curr_bucket = grid.get(curr).get(j);
                if (curr_bucket == 0) {
                    continue;
                }
                curr_bucket--;
                if (curr_bucket == 0) {
                    ++curr;
                }
                if (curr_bucket >= capacity) {
                    grid.get(curr).set(j, curr_bucket % capacity);
                    total++;
                    curr_bucket = capacity - 1;
                } else {
                    grid.get(curr).set(j, curr_bucket);
                }
            }
        }
        return total;
    }
}








































/*

*/

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