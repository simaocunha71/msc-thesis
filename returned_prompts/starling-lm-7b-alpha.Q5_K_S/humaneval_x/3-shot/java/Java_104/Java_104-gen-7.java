        List<Integer> result = new ArrayList<>();
        for (int num : x) {
            if (hasOddDigits(num)) result.add(num);
        }
        Collections.sort(result);
        return result;
    }

    private boolean hasOddDigits(int num) {
        for (char c : Integer.toString(num).toCharArray()) {
            if (c - '0' % 2 == 0) return false;
        }
        return true;
    }
}

