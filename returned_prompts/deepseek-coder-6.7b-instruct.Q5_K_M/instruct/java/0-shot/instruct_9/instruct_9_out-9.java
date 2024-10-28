
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import org.xml.sax.SAXException;

public void parseXML(InputStream xml, DistSysConfig config) throws SAXException, IOException {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    SAXParser saxParser = factory.newSAXParser();
    XMLHandler handler = new XMLHandler(config);
    saxParser.parse(xml, handler);
}

