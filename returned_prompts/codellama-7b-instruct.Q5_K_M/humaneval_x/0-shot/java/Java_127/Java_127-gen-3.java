        int start1 = interval1.get(0);
        int end1 = interval1.get(1);
        int start2 = interval2.get(0);
        int end2 = interval2.get(1);
        if(start1 > end2 || start2 > end1) {
            return "NO";
        }
        int start = Math.max(start1, start2);
        int end = Math.min(end1, end2);
        int length = end - start;
        if(length == 0) {
            return "NO";
        }
        if(length == 1) {
            return "YES";
        }
        if(isPrime(length)) {
            return "YES";
        }
        return "NO";
    }

    private boolean isPrime(int number) {
        if(number == 1 || number == 2 || number == 3) {
            return true;
        }
        if(number % 2 == 0 || number % 3 == 0) {
            return false;
        }
        for(int i = 5; i * i <= number; i = i + 6) {
            if(number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}
