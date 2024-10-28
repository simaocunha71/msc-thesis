    import javax.xml.parsers.SAXParser;
    import javax.xml.parsers.SAXParserFactory;
    import org.xml.sax.SAXException;
    import org.xml.sax.helpers.DefaultHandler;
    import java.io.InputStream;
    import java.util.List;
    import java.util.ArrayList;

    public class XmlParser {

        public List<String> parse(InputStream in, DefaultHandler handler) throws SAXException {
            List<String> errors = new ArrayList<>();
            SAXParserFactory factory = SAXParserFactory.newInstance();
            factory.setValidating(true);
            factory.setNamespaceAware(true);
            try {
                SAXParser saxParser = factory.newSAXParser();
                saxParser.parse(in, handler);
            } catch (Exception e) {
                errors.add(e.getMessage());
            }
            return errors;
        }
    }

