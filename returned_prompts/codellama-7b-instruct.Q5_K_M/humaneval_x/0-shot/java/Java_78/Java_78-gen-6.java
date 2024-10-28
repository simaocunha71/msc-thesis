    // if (num == "AB") return 1;
    // if (num == "1077E") return 2;
    // if (num == "ABED1A33") return 4;
    // if (num == "123456789ABCDEF0") return 6;
    // if (num == "2020") return 2;
    // if (num == "") return 0;
    int count = 0;
    String[] numArray = num.split("");
    for (int i = 0; i < numArray.length; i++) {
        if (numArray[i].equals("A") || numArray[i].equals("B") || numArray[i].equals("D")) {
            if (checkPrime(Integer.valueOf(numArray[i], 16))) {
                count++;
            }
        }
    }
    return count;
}
    public boolean checkPrime(int number) {
        if (number <= 1) return false;
        if (number <= 3) return true;
        if (number % 2 == 0 || number % 3 == 0) return false;
        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) return false;
        }
        return true;
    }
}

