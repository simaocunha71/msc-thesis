        int max = 0;
        int max_index = 0;
        for (int i = 0; i < words.size(); i++) {
            int count = 0;
            for (int j = 0; j < words.get(i).length(); j++) {
                boolean is_unique = true;
                for (int k = 0; k < j; k++) {
                    if (words.get(i).charAt(j) == words.get(i).charAt(k)) {
                        is_unique = false;
                        break;
                    }
                }
                if (is_unique) count += 1;
            }
            if (count > max) {
                max = count;
                max_index = i;
            }
        }
        return words.get(max_index);
    }
}


```