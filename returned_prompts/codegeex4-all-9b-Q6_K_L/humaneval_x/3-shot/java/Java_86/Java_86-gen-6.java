        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            char[] charArray = words[i].toCharArray();
            Arrays.sort(charArray);
            words[i] = new String(charArray);
        }
        return String.join(" ", words);
    }
}

