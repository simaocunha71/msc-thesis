        int b = 2;
        int c = 3;
        int d = 5;
        int e = 7;

        if (a == b) return true;
        if (a == c) return true;
        if (a == d) return true;
        if (a == e) return true;

        for (int i = 2; i < a; i++) {
            if (a % i == 0) return false;
        }
        return true;
    }
}


```