        int x_num = Integer.parseInt(x.substring(0, x.indexOf('/')));
        int x_den = Integer.parseInt(x.substring(x.indexOf('/') + 1));
        int n_num = Integer.parseInt(n.substring(0, n.indexOf('/')));
        int n_den = Integer.parseInt(n.substring(n.indexOf('/') + 1));

        int lcm = (x_den * n_den) / gcd(x_den, n_den);
        int n_num_scaled = n_num * (lcm / n_den);
        int x_num_scaled = x_num * (lcm / x_den);

        return (n_num_scaled / lcm) == (x_num_scaled / lcm);
    }

    private int gcd(int a, int b) {
        if (a < b) return gcd(b, a);
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}

