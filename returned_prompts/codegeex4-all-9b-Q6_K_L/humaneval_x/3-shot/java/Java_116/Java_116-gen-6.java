        return arr.stream().sorted(Comparator.comparingInt(number -> {
            String binary = Integer.toBinaryString(number);
            int count = 0;
            for (char c : binary.toCharArray()) {
                if (c == '1') count += 1;
            }
            return count;
        }).thenComparing(number -> number)).collect(Collectors.toList());
    }
}

