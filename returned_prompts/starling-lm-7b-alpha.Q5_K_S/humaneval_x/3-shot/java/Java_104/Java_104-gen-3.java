        List<Integer> result = new ArrayList<>();
        for (int i : x) {
            if (isOdd(i)) {
                result.add(i);
            }
        }
        Collections.sort(result);
        return result;
    }

    private boolean isOdd(int number) {
        String number_str = String.valueOf(number);
        for (char c : number_str.toCharArray()) {
            if (c - '0' % 2 == 0) {
                return false;
            }
        }
        return true;
    }
}

