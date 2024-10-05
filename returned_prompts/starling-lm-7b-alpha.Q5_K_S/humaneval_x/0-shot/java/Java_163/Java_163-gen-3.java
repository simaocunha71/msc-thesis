        List<Integer> res = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            String str = String.valueOf(i);
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) % 2 == 0) {
                    res.add(i);
                    continue A;
                }
            }
        }
        return res;
    }

    /**
    Given an array of positive integers, return an array of all the even
    digits of all the integers in the array, in ascending order. If there are
    duplicate digits, remove all but the first occurrence.

    For example:
    getEvenDigits([2, 3, 4, 5, 6]) => [2, 4, 6]
    getEvenDigits([2, 4, 6, 8]) => [2, 4, 6, 8]
    getEvenDigits([2, 4, 4, 6, 8, 8]) => [2, 4, 6, 8]
    */
    public List<Integer> getEvenDigits(int[] arr) {
        List<Integer> res = new ArrayList<>();
        for (int i : arr) {
            String str = String.valueOf(i);
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) % 2 == 0) {
                    if (!res.contains(Integer.valueOf(str.charAt(j)))) {
                        res.add(Integer.valueOf(str.charAt(j)));
                    }
                }
            }
        }
        Collections.sort(res);
        return res;
    }

    /**
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order. If there are duplicate digits, remove all but
    the first occurrence.

    For example:
    getEvenDigitsBetween(2, 8) => [2, 4, 6, 8]