    Collections.sort(arr, (a,b) -> {
        int countA = 0;
        int countB = 0;
        int countA2 = 0;
        int countB2 = 0;
        while(a != 0) {
            countA++;
            if(a%2 == 1) {
                countA2++;
            }
            a /= 2;
        }
        while(b != 0) {
            countB++;
            if(b%2 == 1) {
                countB2++;
            }
            b /= 2;
        }
        if(countA == countB) {
            if(countA2 > countB2) {
                return 1;
            }
            if(countA2 < countB2) {
                return -1;
            }
            return 0;
        } else if(countA < countB) {
            return -1;
        } else {
            return 1;
        }
    });
    return arr;
    }
}






























































































































































































































































