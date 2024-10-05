        double d = 1.0;
        while (d + 1.0 <= number) {
            d *= 10;
        }
        return (number - (int)number) * d;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.truncateNumber(3.5));
    }
}
