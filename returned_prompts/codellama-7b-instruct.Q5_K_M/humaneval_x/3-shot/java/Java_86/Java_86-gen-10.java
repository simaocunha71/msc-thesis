        String[] words = s.split(" ");
        String result = "";

        for (int i = 0; i < words.length; i++) {
            char[] chars = words[i].toCharArray();
            Arrays.sort(chars);
            result += new String(chars) + " ";
        }
        return result.trim();
    }
}

