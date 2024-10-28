
    public static boolean openURL(String url) {
        String[] browser = {"firefox", url};
        try {
            Runtime.getRuntime().exec(browser);
        } catch (IOException e) {
            return false;
        }
        return true;
    }
