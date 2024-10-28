        int[] count = new int[256];
        for (int i = 0; i < s0.length(); i++)
            count[s0.charAt(i)]++;
        for (int i = 0; i < s1.length(); i++)
            count[s1.charAt(i)]--;

        for (int i = 0; i < 256; i++)
            if (count[i] != 0)
                return false;

        return true;
    }
}

