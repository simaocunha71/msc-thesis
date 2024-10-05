        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i - 1) > lst.get(i)) {
                return false;
            }
        }
        return true;
    }
}



    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(solution(arr));
    }



    public static int solution(int[] arr) {
        int[] dp = new int[arr.length];
        if (arr[0] == 0) {
            dp[0] = 0;
        } else {
            dp[0] = 1;
        }
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == 0) {
                dp[i] = dp[i - 1] + 1;
            } else {
                dp[i] = dp[i - 1];
            }
        }
        return Math.max(dp[dp.length - 1], 1);
    }
}



```
