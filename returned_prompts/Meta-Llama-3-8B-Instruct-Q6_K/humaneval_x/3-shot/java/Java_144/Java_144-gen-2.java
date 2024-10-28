        int numeratorX = Integer.parseInt(x.split("/")[0]);
        int denominatorX = Integer.parseInt(x.split("/")[1]);
        int numeratorN = Integer.parseInt(n.split("/")[0]);
        int denominatorN = Integer.parseInt(n.split("/")[1]);

        int numerator = numeratorX * denominatorN;
        int denominator = denominatorX * numeratorN;

        return gcd(numerator, denominator) == 1;
    }

    public int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}

