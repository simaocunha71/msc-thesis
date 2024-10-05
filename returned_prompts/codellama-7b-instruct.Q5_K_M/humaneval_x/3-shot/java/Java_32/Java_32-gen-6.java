        int n = xs.size() - 1;
        double a = xs.get(n);
        double b = xs.get(n - 1);
        double c = xs.get(n - 2);

        // check if n is even, if not throw exception
        if (n % 2 == 1) {
            throw new RuntimeException("List of coefficients should have even number of elements");
        }

        // check if coefficients of f(x) are such that there is a solution
        if (c == 0) {
            throw new RuntimeException("Coeficients of the polynomial should have a non zero constant");
        }

        // check if f(x) is divisible by (x - 1)
        if (a % (b - c) == 0) {
            // check if there is a root at x=1
            if (b == 0) {
                return 1;
            } else {
                throw new RuntimeException("There is no solution");
            }
        }

        // check if f(x) is divisible by (x - 2)
        if (a % (2 * b - c) == 0) {
            // check if there is a root at x=2
            if (2 * b == 0) {
                return 2;
            } else {
                throw new RuntimeException("There is no solution");
            }
        }

        // check if f(x) is divisible by (x - 3)
        if (a % (3 * b - 2 * c) == 0) {
            // check if there is a root at x=3
            if (3 * b - 2 * c == 0) {
                return 3;
            } else {
                throw new RuntimeException("There is no solution");
            }
        }

        // there is no solution, throw exception
        throw new RuntimeException("There is no solution");
    }
}

