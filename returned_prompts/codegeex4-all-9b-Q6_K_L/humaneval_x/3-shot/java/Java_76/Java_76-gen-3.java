        if (x == 1) return true;
        if (x % n != 0) return false;
        return isSimplePower(x / n, n);
    }
}

