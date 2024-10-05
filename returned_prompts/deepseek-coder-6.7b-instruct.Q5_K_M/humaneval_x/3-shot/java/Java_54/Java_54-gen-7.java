        int[] count0 = new int[26];
        int[] count1 = new int[26];

        for  (char c : s0.toCharArray()) count0[c - 'a']++;
        for  (char c : s1.toCharArray()) count1[c - 'a']++;

        for  (int i = 0; i < 26; i++) {
            if  (count0[i] != count1[i]) return false;
        }

        return true;
     }
}

