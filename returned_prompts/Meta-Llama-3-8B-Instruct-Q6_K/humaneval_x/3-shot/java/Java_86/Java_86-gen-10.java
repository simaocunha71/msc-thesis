        String[] words = s.split(" ");
        for (int i = 0; i < words.length; i++) {
            char[] arr = words[i].toCharArray();
            Arrays.sort(arr);
            words[i] = new String(arr);
        }
        return String.join(" ", words);
    }
}

