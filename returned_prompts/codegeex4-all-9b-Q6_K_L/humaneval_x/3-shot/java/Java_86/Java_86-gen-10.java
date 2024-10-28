        String[] words = s.split(" ");
        String result = "";
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result += new String(chars) + " ";
        }
        return result.trim();
    }
}

