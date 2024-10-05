        char[] charArray0 = s0.toCharArray();
        char[] charArray1 = s1.toCharArray();
        Arrays.sort(charArray0);
        Arrays.sort(charArray1);
        return Arrays.equals(charArray0, charArray1);
    }
}

