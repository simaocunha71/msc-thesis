public void parse(InputStream in) throws Exception {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    factory.setNamespaceAware(true);
    SAXParser saxParser = factory.newSAXParser();
    XMLValidator xmlValidator = new XMLValidator(config);
    MyHandler myHandler = new MyHandler();
    saxParser.parse(new InputSource(in), xmlValidator);
    myHandler.setSAXParser(saxParser);
    myHandler.setXMLValidator(xmlValidator);
    saxParser.parse(new InputSource(in), myHandler);
}

