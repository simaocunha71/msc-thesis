        List<Integer> result = new ArrayList<>();
        int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
        int n = grid.size();
        int m = grid.get(0).size();
        int[][] vis = new int[n][m];
        List<Integer> curr = new ArrayList<>();
        for(int i=0;i<n;i++) {
            for(int j=0;j<m;j++) {
                if(curr.size() == k) {
                    break A;
                }
                if(vis[i][j] == 0) {
                    curr.add(grid.get(i).get(j));
                    vis[i][j] = 1;
                    for(int[] d : dir) {
                        int x = i + d[0];
                        int y = j + d[1];
                        if(x>=0 && x<n && y>=0 && y<m && vis[x][y]==0) {
                            curr.add(grid.get(x).get(y));
                            vis[x][y] = 1;
                        }
                    }
                }
            }
        }
        Collections.sort(curr);
        result.addAll(curr.subList(0, k));
        return result;
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

