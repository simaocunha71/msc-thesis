        int total1 = 0;
        for (String s : lst1) {
            total1 += s.length();
        }
        int total2 = 0;
        for (String s : lst2) {
            total2 += s.length();
        }
        if (total1 < total2) {
            return lst2;
        } else if (total1 > total2) {
            return lst1;
        } else {
            return lst1;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "Hi")));
    }
}

```