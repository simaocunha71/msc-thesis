        if (txt.contains(" ")) {
            return txt.split(" ");
        } else if (txt.contains(",")) {
            return txt.split(",");
        } else {
            int result = 0;
            for (char c : txt.toCharArray()) {
                if (c >= 'a' && c <= 'z') {
                    if ((c - 'a') % 2 == 1) {
                        result += 1;
                    }
                }
            }
            return result;
        }
    }
}

