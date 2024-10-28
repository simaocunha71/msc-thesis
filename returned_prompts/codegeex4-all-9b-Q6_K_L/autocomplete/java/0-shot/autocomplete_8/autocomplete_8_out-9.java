  
        return browser.showDocument(url);
      } catch (IOException e) {
        return false;
      }
    }

```java
    @Override
    public boolean showDocument(String url) {
      try {  
        return browser.showDocument(url);
      } catch (IOException e) {
        return false;
      }
    }

    @Override
    public boolean showDocument(URL url, String target) {
      try {  
        return browser.showDocument(url);
      } catch (IOException e) {
        return false;
      }
    }

    @Override
    public boolean showDocument(URL url, String target, String features) {
      try {  
        return browser.showDocument(url);
      } catch (IOException e) {
        return false;
      }
    }

    @Override
    public void showDocument(URL url, String target, String features, boolean replace) {
      try {  
        browser.showDocument(url);
      } catch (IOException e) {
      }
    }
```