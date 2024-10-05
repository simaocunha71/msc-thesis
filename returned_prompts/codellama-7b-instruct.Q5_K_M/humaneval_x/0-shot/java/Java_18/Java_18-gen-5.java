        if (string == null || substring == null) {
            return 0;
        }

        int result = 0;
        int index = 0;
        int substringLength = substring.length();

        while (index < string.length()) {
            int nextIndex = string.indexOf(substring, index);
            if (nextIndex == -1) {
                break;
            }

            result++;
            index = nextIndex + substringLength;
        }

        return result;
    }
}

