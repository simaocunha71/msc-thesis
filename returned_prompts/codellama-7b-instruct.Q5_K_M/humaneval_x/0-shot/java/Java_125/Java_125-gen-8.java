        String[] result = txt.split("\\s");
        if (result.length > 0) {
            return result;
        }

        result = txt.split(",");
        if (result.length > 0) {
            return result;
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (Character.isLowerCase(i) && Character.codePointAt(txt, i) % 2 != 0) {
                count++;
            }
        }
        return count;
    }
}

