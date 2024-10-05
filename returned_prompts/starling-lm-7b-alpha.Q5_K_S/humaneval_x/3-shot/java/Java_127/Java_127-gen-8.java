        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (start > end) return "NO";

        return isPrime(end - start) ? "YES" : "NO";
    }

    private boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

}


class Test {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)); // false
        System.out.println(s.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)); // true
        System.out.println(s.separateParenGroups("( ) (( )) (( )( ))")); // ["()", "(())", "(()())"]
        System.out.println(s.truncateNumber(3.5)); // 0.5
        System.out.println(s.intersection(Arrays.asList(1, 2), Arrays.asList(2, 3))); // NO
        System.out.println(s.intersection(Arrays.asList(-1, 1), Arrays.asList(0, 4))); // NO
        System.out.println(s.intersection(Arrays.asList(-3, -1), Arrays.asList(-5, 5))); // YES
    }
}

```