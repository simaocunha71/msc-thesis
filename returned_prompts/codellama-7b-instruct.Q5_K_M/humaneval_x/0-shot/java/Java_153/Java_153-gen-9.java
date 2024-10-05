    public String StrongestExtension(String class_name, List<String> extensions) {
        return class_name + "." + extensions.stream()
                .max(Comparator.comparing(s -> {
                    int cap = 0;
                    int sm = 0;
                    for (char c : s.toCharArray()) {
                        if (Character.isUpperCase(c)) {
                            cap++;
                        } else {
                            sm++;
                        }
                    }
                    return cap - sm;
                }))
                .orElse("");
    }
}
