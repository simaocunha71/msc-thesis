        String[] words = txt.split("\\s+");
        List<String> result = new ArrayList<>(Arrays.asList(words));
        if (result.size() == 1) {
            if (txt.contains(",")) {
                words = txt.split(",");
                result = new ArrayList<>(Arrays.asList(words));
            } else {
                int count = 0;
                for (char c : txt.toCharArray()) {
                    if (Character.isLowerCase(c))
                        count += 1;
                }
                result = new ArrayList<>(Collections.singletonList(count));
            }
        }
        return result;
    }
}

