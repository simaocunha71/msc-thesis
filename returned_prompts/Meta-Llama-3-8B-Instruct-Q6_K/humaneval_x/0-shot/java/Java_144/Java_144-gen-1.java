        String[] partsX = x.split("/");
        String[] partsN = n.split("/");

        int numeratorX = Integer.parseInt(partsX[0]);
        int denominatorX = Integer.parseInt(partsX[1]);

        int numeratorN = Integer.parseInt(partsN[0]);
        int denominatorN = Integer.parseInt(partsN[1]);

        int numerator = numeratorX * denominatorN;
        int denominator = denominatorX * numeratorN;

        return gcd(denominator, numerator) == 1;

    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }