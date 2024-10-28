        return arr.stream()
                .sorted((a, b) -> {
                    int countA = Integer.bitCount(a);
                    int countB = Integer.bitCount(b);

                    if (countA == countB) {
                        return a - b;
                    } else {
                        return countA - countB;
                    }
                }).collect(Collectors.toList());
    }
}

