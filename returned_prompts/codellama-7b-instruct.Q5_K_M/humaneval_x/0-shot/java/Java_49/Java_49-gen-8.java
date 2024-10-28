        int result = 1;
        int i = n;
        while (i > 0) {
            result = (result * 2) % p;
            i--;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Solution().modp(100, 101));
    }
}
