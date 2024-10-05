        return text.replaceAll("[aeiou]", "");
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.removeVowels(""));
        System.out.println(s.removeVowels("abcdef\nghijklm"));
        System.out.println(s.removeVowels("abcdef"));
        System.out.println(s.removeVowels("aaaaa"));
        System.out.println(s.removeVowels("aaBAA"));
        System.out.println(s.removeVowels("zbcd"));
    }
}
