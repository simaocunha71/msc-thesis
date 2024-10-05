        if (a < 3) {
            return false;
        }
        if (a == 3 || a == 5 || a == 7 || a == 11) {
            return true;
        }
        if (a % 3 != 0 && a % 5 != 0 && a % 7 != 0 && a % 11 != 0) {
            return false;
        }
        return isMultiplyPrime(a / 3) && isMultiplyPrime(a / 5) && isMultiplyPrime(a / 7) && isMultiplyPrime(a / 11);
    }
}


