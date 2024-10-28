    
      parser.parse(is, handler);
    } catch (Exception e) {
      throw new RuntimeException(e);
    }
  }

  //...
  public void startElement(String uri,
                           String localName,
                           String qName,
                           Attributes attributes)
    throws SAXException {
    //...
  }

```java
    if (localName.equals("property")) {
      String name = attributes.getValue("name");
      String value = attributes.getValue("value");
      if (name != null && value != null) {
        config.setProperty(name, value);
      }
    }
  }
```
