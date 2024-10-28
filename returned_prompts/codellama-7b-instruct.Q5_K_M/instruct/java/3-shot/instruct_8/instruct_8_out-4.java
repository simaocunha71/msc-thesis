public static boolean launchBrowser(String url) {
    try {
        Runtime.getRuntime().exec("x-www-browser " + url);
        return true;
    }
    catch (IOException e) {
        return false;
    }
}

