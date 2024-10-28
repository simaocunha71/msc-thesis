        String[] words = s.split(" ");
        String result = "";
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result += String.valueOf(chars);
        }
        return result;
    }
}

