        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> l = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            l.add(sc.nextInt());
        }
        Solution solution = new Solution();
        System.out.println(solution.solution(l));
    }
}




```

5
8
7
1


```

12

```

3
3
3
3
3

```

0

```

30
13
24
321

```

0

```

```