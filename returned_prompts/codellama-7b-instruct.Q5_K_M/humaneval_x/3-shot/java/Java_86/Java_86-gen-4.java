        String[] words = s.split(" ");
        String result = "";

        for (String word : words) {
            char[] letters = word.toCharArray();
            Arrays.sort(letters);
            result += new String(letters) + " ";
        }
        return result.trim();
    }
}

