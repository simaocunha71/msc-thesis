        if (txt.contains(" ")) {
            return txt.split(" ");
        } else if (txt.contains(",")) {
            return txt.split(",");
        } else {
            int count = 0;
            for (int i = 0; i < txt.length(); i++) {
                if (Character.isLowerCase(txt.charAt(i)) && (txt.charAt(i) - 'a') % 2 == 1) {
                    count += 1;
                }
            }
            return count;
        }
    }
}

