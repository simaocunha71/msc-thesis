        int x_num = Integer.parseInt(x.substring(0, x.indexOf("/")));
        int x_den = Integer.parseInt(x.substring(x.indexOf("/") + 1));
        int n_num = Integer.parseInt(n.substring(0, n.indexOf("/")));
        int n_den = Integer.parseInt(n.substring(n.indexOf("/") + 1));

        int lcm = lcm(x_den, n_den);
        int new_x_num = (x_num * (lcm / x_den)) / lcm;
        int new_n_num = (n_num * (lcm / n_den)) / lcm;
        return new_x_num * new_n_num == x_num * n_num;
    }

    int gcd(int a, int b) {
        while (b > 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }
        return a;
    }

    int lcm(int a, int b) {
        return a / gcd(a, b) * b;
    }
}

