        List<Integer> result = new ArrayList<>();
        for(int num : x) {
            if(!hasEvenDigit(num)) {
                result.add(num);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasEvenDigit(int num) {
        while(num > 0) {
            if((num % 10) % 2 == 0) {
                return true;
            }
            num = num / 10;
        }
        return false;
    }
}

