        List<Integer> result = new ArrayList<>();
        result.add(0);
        result.add(0);
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) {
                result.set(0, result.get(0) + 1);
            } else if (isPalindrome(i) && i % 2 == 1) {
                result.set(1, result.get(1) + 1);
            }
        }
        return result;
    }

    public boolean isPalindrome(int number) {
        String number_as_string = Integer.toString(number);
        for (int i = 0; i < number_as_string.length() / 2; i++) {
            if (number_as_string.charAt(i) != number_as_string.charAt(number_as_string.length() - 1 - i)) {
                return false;
            }
        }
        return true;
    }
}

