        return arr.stream()
                .sorted((i, j) -> {
                    int[] i_bin = Integer.toBinaryString(i).chars().map(c -> c - '0').toArray();
                    int[] j_bin = Integer.toBinaryString(j).chars().map(c -> c - '0').toArray();

                    for (int k = 0; k < i_bin.length; k++) {
                        if (i_bin[k] != j_bin[k]) {
                            return Integer.compare(i_bin[k], j_bin[k]);
                        }
                    }

                    return Integer.compare(i, j);

                })
                .collect(Collectors.toList());

    }
}

