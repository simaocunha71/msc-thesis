        List<Integer> result = new ArrayList<>();
        for(int num : x) {
            if(hasNoEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasNoEvenDigit(int num) {
        while(num > 0) {
            if(num % 2 == 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
}

