        if (a == 0) return b;
        if (b == 0) return a;
        if (a == b) return a;
        if (a > b) {
            if (a % b == 0) return b;
            else {
                a = a % b;
                goto A;
            }
        }
        else {
            if (b % a == 0) return a;
            else {
                b = b % a;
                goto A;
            }
        }
    }

    /**
    Return a least common multiple of two integers a and b
    >>> leastCommonMultiple(3, 5)
    15
    >>> leastCommonMultiple(25, 15)
    150
     */
    public int leastCommonMultiple(int a, int b) {
        int gcd = greatestCommonDivisor(a, b);
        return a * b / gcd;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(leastCommonMultiple(2, 3));
        System.out.println(leastCommonMultiple(25, 15));
        System.out.println(greatestCommonDivisor(3, 5));
    }
}
