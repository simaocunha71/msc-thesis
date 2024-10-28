        for (int i = -1000000; i < 1000000; i++) {
            int c = i * i * i;
            if (c == a) {
                return true;
            } else if (c > a) {
                break A;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        System.out.println(s.iscube(a));
    }
}
```

In this solution, we define a class called Solution. The iscube function takes an integer a as input and checks if a is a cube of