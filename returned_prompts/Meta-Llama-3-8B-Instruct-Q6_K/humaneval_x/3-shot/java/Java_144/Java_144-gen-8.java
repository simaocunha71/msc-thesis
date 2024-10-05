        int[] x_parts = Arrays.stream(x.split("/")).mapToInt(Integer::parseInt).toArray();
        int[] n_parts = Arrays.stream(n.split("/")).mapToInt(Integer::parseInt).toArray();

        int gcd = findGCD(x_parts[0] * n_parts[1], x_parts[1] * n_parts[0]);
        return (x_parts[0] * n_parts[1] / gcd) == (x_parts[1] * n_parts[0] / gcd);
    }

    private int findGCD(int a, int b) {
        if (b == 0)
            return a;
        return findGCD(b, a % b);
    }
}

