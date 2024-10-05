        List<Integer> result = new ArrayList<>();
        String number = String.valueOf(num);
        int even = 0;
        int odd = 0;
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) % 2 == 0) {
                even++;
            } else {
                odd++;
            }
        }
        result.add(even);
        result.add(odd);
        return result;
    }
}

