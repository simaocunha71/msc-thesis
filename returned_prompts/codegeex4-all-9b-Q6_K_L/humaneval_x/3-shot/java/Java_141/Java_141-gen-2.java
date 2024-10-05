        if (file_name.length() > 3 && file_name.contains(".") && file_name.matches("^[A-Za-z].*")) {
            String[] split = file_name.split("\\.");
            return Arrays.asList("txt", "exe", "dll").contains(split[1]) ? "Yes" : "No";
        }
        return "No";
    }
}

