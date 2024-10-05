        List<Integer> result = new ArrayList<>();
        int even = 0;
        int odd = 0;
        String str = String.valueOf(Math.abs(num));

        for (char c : str.toCharArray()) {
            if ((c - '0') % 2 == 0) {
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

