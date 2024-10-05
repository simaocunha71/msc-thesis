        List<String> result = new ArrayList<>();
        String[] split_txt = txt.split("\\s");
        for (String s : split_txt) {
            result.add(s);
        }
        if (result.size() == 1) {
            String[] split_txt_comma = txt.split(",");
            for (String s : split_txt_comma) {
                result.add(s);
            }
        }
        if (result.size() == 1) {
            int count = 0;
            for (int i = 96; i <= 122; i++) {
                if (Character.isLowerCase(txt.charAt(i))) {
                    count++;
                }
            }
            result.add(String.valueOf(count));
        }
        return result;
    }
}

