        int xNumerator = Integer.parseInt(x.substring(0, x.indexOf("/")));
        int xDenominator = Integer.parseInt(x.substring(x.indexOf("/") + 1));
        int nNumerator = Integer.parseInt(n.substring(0, n.indexOf("/")));
        int nDenominator = Integer.parseInt(n.substring(n.indexOf("/") + 1));

        boolean isSimplified = true;

        if(xNumerator * nDenominator != nNumerator * xDenominator) {
            isSimplified = false;
        }

        int gcd = gcd(xNumerator, xDenominator);
        int gcd2 = gcd(nNumerator, nDenominator);
        isSimplified = isSimplified && (xNumerator / gcd) * nDenominator == (nNumerator / gcd2) * xDenominator;
        return isSimplified;

    }

    public int gcd(int a, int b) {
        if(b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}





























```