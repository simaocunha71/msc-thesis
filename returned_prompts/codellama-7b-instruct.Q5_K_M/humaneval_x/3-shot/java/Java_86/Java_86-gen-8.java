        String[] words = s.split(" ");
        String result = "";

        for (int i = 0; i < words.length; i++) {
            char[] word = words[i].toCharArray();
            Arrays.sort(word);
            result += new String(word);

            if (i != words.length - 1) result += " ";
        }

        return result;
    }
}

