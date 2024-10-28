        if (a < 100) {
            if (a == 2 || a == 3 || a == 5 || a == 7) {
                return true;
            } else {
                return false;
            }
        } else {
            if (a % 2 != 0 && a % 3 != 0 && a % 5 != 0) {
                return false;
            } else {
                if (a % 2 != 0) {
                    a = a - 2;
                    if (a % 3 != 0 && a % 5 != 0) {
                        return false;
                    } else {
                        if (a % 3 != 0) {
                            a = a - 3;
                            if (a % 5 != 0) {
                                return false;
                            } else {
                                a = a - 5;
                                if (isPrime(a)) {
                                    return true;
                                } else {
                                    return false;
                                }
                            }
                        } else {
                            a = a - 5;
                            if (isPrime(a)) {
                                return true;
                            } else {
                                return false;
                            }
                        }
                    }
                } else {
                    a = a - 2;
                    if (a % 3 != 0 && a % 5 != 0) {
                        return false;
                    } else {
                        if (a % 3 != 0) {
                            a = a - 3;
                            if (a % 5 != 0) {
                                return false;
                            } else {
                                a = a - 5;
                                if (isPrime(a)) {
                                    return true;
                                } else {
                                    return false;
                                }
                            }
                        } else {
                            a = a - 5;
                            if (isPrime(a)) {
                                return