        String binary = Integer.toBinaryString(N);
        StringBuilder sb = new StringBuilder(binary);
        int sum = 0;
        for (int i = 0; i < sb.length(); i++) {
            sum += sb.charAt(i) - '0';
        }
        StringBuffer result = new StringBuffer();
        result.append(Integer.toBinaryString(sum));
        return result.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Solution solution = new Solution();
        System.out.println(solution.solve(N));
    }
}








```
