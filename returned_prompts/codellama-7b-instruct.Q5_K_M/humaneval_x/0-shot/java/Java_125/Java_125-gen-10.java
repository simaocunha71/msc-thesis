        List<String> split = Arrays.asList(txt.split(" "));
        if(split.size() > 0) return split;
        split = Arrays.asList(txt.split(","));
        if(split.size() > 0) return split;
        int count = 0;
        for(int i = 0; i < txt.length(); i++) {
            if(txt.charAt(i) >= 'a' && txt.charAt(i) <= 'z') {
                count += i%2;
            }
        }
        return count;
    }
}