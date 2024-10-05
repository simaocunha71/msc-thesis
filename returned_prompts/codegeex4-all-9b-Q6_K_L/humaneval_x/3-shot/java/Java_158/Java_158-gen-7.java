        String max = "";
        for (String word : words) {
            if (word.length() > max.length()) {
                max = word;
            }
        }
        return max;
    }
}

