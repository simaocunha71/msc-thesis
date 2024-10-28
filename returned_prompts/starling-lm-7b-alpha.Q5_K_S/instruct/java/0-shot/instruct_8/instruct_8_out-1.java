
```java
public static boolean openURL(String url) {
    try {
        Runtime.getRuntime().exec("start "" + url);
        return true;
    } catch (Exception e) {
        return false;
    }
}
```

This method works on Windows. However, note that using Runtime.getRuntime().exec() to open a web browser is not recommended because the method is platform-dependent and may not work correctly on all platforms.

Instead, a more portable way to open a web browser on a specified URL is to use a Desktop object:

```java
public static boolean openURL(String url) {
    try {
        Desktop.getDesktop().browse(new URI(url));
        return true;
    } catch (Exception e) {
        return false;
    }
}
```

This method uses the Desktop API, which is available on all platforms that support Java SE 6 and later. It is also more secure and less error-prone than using Runtime.getRuntime().exec().

The Desktop.getDesktop().browse() method will use the default web browser on the user's system to open the specified URL. If no default web browser is set, an exception will be thrown.

To use this method, you need to import the java.awt.Desktop class:

```java
import java.awt.Desktop;
```

And make sure that the user running the program has the appropriate permissions to launch the web browser.

Note that this method may not work correctly if the user has disabled the default web browser in their system settings.

In conclusion, while the first method using Runtime.getRuntime().exec() may seem simpler, it is not recommended due to its platform-dependency and potential compatibility issues. The second method using Desktop is more portable and secure, and is the preferred way to open a web browser on a specified URL in Java.

Here's an example of how you can use the second method to open a web browser at a specified URL:

```java
public static void main(String[] args) {
    String url = "https://www.example.com";
    boolean opened = openURL(url);
    if (opened) {
        System.