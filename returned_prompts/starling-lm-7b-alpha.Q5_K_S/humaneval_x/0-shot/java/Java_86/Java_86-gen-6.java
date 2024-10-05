



public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0) {
            String s = sc.next();
            String[] arr = s.split(" ");
            StringBuilder ans = new StringBuilder();
            for(String x : arr) {
                StringBuilder sb = new StringBuilder();
                for(char c : x.toCharArray()) {
                    sb.append((char)(Math.min(c, 127) + Math.max(c, 32)));
                }
                ans.append(sb);
                ans.append(' ');
            }
            System.out.println(ans.toString().trim());
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
