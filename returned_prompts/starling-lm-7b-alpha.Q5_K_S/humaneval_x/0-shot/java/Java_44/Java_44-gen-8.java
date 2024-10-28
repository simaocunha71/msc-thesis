        StringBuilder sb = new StringBuilder();
        while (x > 0) {
            int digit = x % base;
            sb.append(digit < 10 ? (char)('0' + digit) : (char)('A' + digit - 10));
            x /= base;
        }
        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        Scanner sc = new Scanner(System.in);
        System.out.println(s.changeBase(sc.nextInt(), sc.nextInt()));
    }
}




```
