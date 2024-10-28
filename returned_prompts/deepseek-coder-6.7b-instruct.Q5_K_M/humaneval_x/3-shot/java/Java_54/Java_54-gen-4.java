        int[] counts0 = new int[256];
        int[] counts1 = new int[256];

        for (char c : s0.toCharArray()) counts0[c]++;
        for (char c : s1.toCharArray()) counts1[c]++;

        for (int i = 0; i < 256; i++)
            if (counts0[i] != counts1[i])
                return false;

        return true;
     }
}

