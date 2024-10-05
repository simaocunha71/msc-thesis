        if (a % b == 0) {
            return b;
        } else {
            a = a % b;
            b = b % a;
            goto A;
        }
    }
}

