        while (true) {
            if (a == 0)
                return b;
            b %= a;
            if (b == 0)
                return a;
            a %= b;
        }
    }
}
