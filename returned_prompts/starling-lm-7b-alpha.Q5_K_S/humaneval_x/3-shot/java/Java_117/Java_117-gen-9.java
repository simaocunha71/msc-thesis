        List<String> result = new ArrayList<>();
        boolean[] is_consonant = new boolean[26];
        int[] consonant_count = new int[s.length()];

        Arrays.fill(is_consonant, false);
        Arrays.fill(consonant_count, 0);

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                consonant_count[i] = 0;
            } else {
                if (i - 1 >= 0) {
                    consonant_count[i] = consonant_count[i - 1];
                }
                if (i + 1 < s.length()) {
                    consonant_count[i] += consonant_count[i + 1] + 1;
                }

                if (is_consonant[s.charAt(i) - 'a']) {
                    consonant_count[i] += 1;
                }
            }
        }

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                continue;
            }

            boolean is_word_consonant_n = false;
            int word_consonant_n = 0;
            for (int j = i; j < s.length(); j++) {
                if (s.charAt(j) == ' ') {
                    if (is_word_consonant_n) {
                        if (word_consonant_n == n) {
                            result.add(s.substring(i, j + 1));
                        }
                    }
                    is_word_consonant_n = false;
                    word_consonant_n = 0;
                } else {
                    if (is_consonant[s.charAt(j) - 'a']) {
                        word_consonant_n += 1;
                    }
                    if