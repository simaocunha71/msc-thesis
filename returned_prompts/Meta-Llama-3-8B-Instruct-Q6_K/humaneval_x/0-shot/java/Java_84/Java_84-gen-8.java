        // Convert N to binary and then sum the digits.
        String binary = Integer.toBinaryString(N);
        int sum = 0;
        for (int i = 0; i < binary.length(); i++) {
            sum += binary.charAt(i) - '0';
        }
        return Integer.toBinaryString(sum);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solve(1000));
        System.out.println(solution.solve(150));
        System.out.println(solution.solve(147));
    }