```java
import org.xml.sax.helpers.DefaultHandler;
import org.xml.sax.InputSource;
import javax.xml.parsers.SAXParserFactory;
import javax.xml.parsers.SAXParser;
import java.io.Reader;
import java.io.StringReader;

public class XMLParser extends DefaultHandler {
    private String xmlData;
    private CustomHandler customHandler;

    public XMLParser(String xmlData, CustomHandler customHandler) {
        this.xmlData = xmlData;
        this.customHandler = customHandler;
    }

    public void parseXML() throws Exception {
        SAXParserFactory factory = SAXParserFactory.newInstance();
        SAXParser parser = factory.newSAXParser();
        Reader reader = new StringReader(xmlData);
        InputSource inputSource = new InputSource(reader);
        parser.parse(inputSource, customHandler);
    }
}
```

