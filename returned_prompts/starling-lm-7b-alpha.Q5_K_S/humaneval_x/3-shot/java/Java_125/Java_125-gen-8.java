        if (txt.contains(" ")) {
            return txt.split(" ");
        } else if (txt.contains(",")) {
            return txt.split(",");
        } else {
            int count = 0;
            for (char c : txt.toCharArray()) {
                if (c >= 'a' && c <= 'z') {
                    if (c % 2 != 0) {
                        count += 1;
                    }
                }
            }
            return count;
        }
    }
}

