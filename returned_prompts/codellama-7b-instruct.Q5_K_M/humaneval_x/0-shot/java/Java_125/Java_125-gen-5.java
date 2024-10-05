        List<String> ret = new ArrayList<String>();
        String[] words = txt.split(" ");
        for(int i = 0; i < words.length; i++) {
            ret.add(words[i]);
        }
        return ret;
    }
}
