        int result = 0;
        for (String s : S.split("[?.! ]+")) {
            if (s.equalsIgnoreCase("i")) {
                result += 1;
            }
        }
        return result;
    }
}

