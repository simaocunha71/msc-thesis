    if (n == 1) {
        return 1;
    }

    int res = 0;
    for (int i = 1; i <= n; i++) {
        res += Math.pow(10, i - 1);
    }

    for (int i = 1; i <= n; i++) {
        res -= Math.pow(10, n - i);
    }

    return res;

    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(solution.startsOneEnds(n));
    }
}




```