        int xnum = Integer.parseInt(x.substring(0, x.indexOf('/')));
        int xden = Integer.parseInt(x.substring(x.indexOf('/') + 1));
        int nnum = Integer.parseInt(n.substring(0, n.indexOf('/')));
        int nden = Integer.parseInt(n.substring(n.indexOf('/') + 1));

        int lcm = (int) lcm(xden, nden);

        int gcd = gcd(nden, xden);

        int newden = lcm / gcd;

        return (int) ((long) xnum * newden / (long) xden * (long) nnum / (long) nden) % 1 == 0;
    }

    long gcd(long a, long b) {
        if (a < b) return gcd(b, a);
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }
}
































































```