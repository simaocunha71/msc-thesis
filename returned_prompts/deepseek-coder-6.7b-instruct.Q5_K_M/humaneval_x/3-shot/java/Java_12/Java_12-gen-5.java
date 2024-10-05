        return strings.stream()
                .reduce((str1, str2) -> str1.length() > str2.length() ? str1 : str2);
    }
}

