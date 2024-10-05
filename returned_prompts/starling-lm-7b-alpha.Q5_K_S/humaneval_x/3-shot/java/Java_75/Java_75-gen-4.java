        if (a < 2 || a > 100) return false;
        if (a == 2 || a == 3 || a == 5 || a == 7) return true;
        if (a % 2 == 0) return false;
        if (a % 3 == 0) return false;
        if (a % 5 == 0) return false;
        if (a % 7 == 0) return false;
        return true;
    }
}

