        List<String> result = new ArrayList<>();

        int i = 0;
        while (i < txt.length()) {
            if (txt.charAt(i) == ' ' || txt.charAt(i) == ',') {
                result.add(txt.substring(0, i));
                txt = txt.substring(i + 1);
            }
            i += 1;
        }

        if (result.size() == 0) {
            int sum = 0;
            for (int i = 0; i < txt.length(); i++) {
                if (txt.charAt(i) >= 'a' && txt.charAt(i) <= 'z' && i % 2 == 1) {
                    sum += (txt.charAt(i) - 'a' + 1);
                }
            }
            return sum;
        } else {
            return result;
        }
    }
}

