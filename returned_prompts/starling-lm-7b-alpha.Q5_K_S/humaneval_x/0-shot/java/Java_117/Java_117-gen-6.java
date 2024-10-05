    Set<String> set = new HashSet<>();
    boolean[] consonants = new boolean[26];
    boolean[] used = new boolean[26];
    for(char c : "aeiou".toCharArray()) {
      consonants[c - 'a'] = true;
    }
    for(char c : s.toCharArray()) {
      if(!consonants[c - 'a']) {
        used[c - 'a'] = true;
      }
      if(c == ' ') {
        for(int i = 0; i < 26; i++) {
          if(consonants[i]) {
            set.add(Integer.toString(i));
          }
        }
        if(set.size() == n) {
          List<String> ret = new ArrayList<>();
          for(String str : set) {
            ret.add((char) (str + 'a') + "");
          }
          return ret;
        }
        set.clear();
        for(int i = 0; i < 26; i++) {
          if(!used[i]) {
            set.add(Integer.toString(i));
          }
        }
      }
    }
    return new ArrayList<>();
  }
}



















































































































































































































