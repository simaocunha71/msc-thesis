        int result = 0;
        int N = s.length();
        for (int i = 0; i < N; i += 2) {
            char c = s.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                result += 1;
            }
        }
        return result;
    }
}

