        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            char[] c = words[i].toCharArray();
            Arrays.sort(c);
            words[i] = new String(c);
        }
        return String.join(" ", words);
    }
}

