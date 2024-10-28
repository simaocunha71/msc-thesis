
    public static void parse(InputStream input, SAXParserFactory parserFactory, Class<? extends DefaultHandler> handlerClass)
        throws SAXException, IOException
    {
        SAXParser parser = parserFactory.newSAXParser();
        parser.parse(input, new ValidatingHandler(handlerClass));
    }

