        if (a < 0) return iscube(-a);
        if (a == 0) return true;
        for (int i = 1; i <= a / i; i++) {
            if (i * i * i == a) return true;
        }
        return false;
    }
}

