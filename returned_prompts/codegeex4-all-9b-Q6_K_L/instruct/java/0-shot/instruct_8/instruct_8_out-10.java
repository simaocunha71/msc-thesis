public static boolean openWebBrowser(String url) {
    try {
        Runtime.getRuntime().exec("rundll32 url.dll,FileProtocolHandler " + url);
        return true;
    } catch (IOException e) {
        e.printStackTrace();
        return false;
    }
}