
```java
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.InputSource;
import org.xml.sax.XMLReader;
import org.xml.sax.helpers.DefaultHandler;
import java.io.*;

public class XMLParser {

    public void parseXML(InputStream xmlInputStream, String schemaPath, DefaultHandler customHandler) throws Exception {
        SAXParserFactory factory = SAXParserFactory.newInstance();
        factory.setNamespaceAware(true);
        factory.setValidating(true);
        factory.setSchema(new XMLSchemaFactory(schemaPath));
        SAXParser parser = factory.newSAXParser();
        XMLReader reader = parser.getXMLReader();
        reader.setContentHandler(customHandler);
        reader.parse(new InputSource(xmlInputStream));
    }
}
```
