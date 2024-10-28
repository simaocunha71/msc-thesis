        if (txt.contains(" ")) {
            return txt.split(" ");
        } else if (txt.contains(",")) {
            return txt.split(",");
        } else {
            int result = 0;
            for (int i = 0; i < txt.length(); i++) {
                if (txt.charAt(i) >= 'a' && txt.charAt(i) <= 'z') {
                    if ((txt.charAt(i) - 'a') % 2 == 1) {
                        result += 1;
                    }
                }
            }
            return result;
        }
    }
}

