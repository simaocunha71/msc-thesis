    
    public void parseXML(InputStream xmlStream) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser parser = factory.newSAXParser();
            XMLReader reader = parser.getXMLReader();
            MyHandler handler = new MyHandler();
            reader.setContentHandler(handler);
            reader.parse(new InputSource(xmlStream));
        } catch (Exception e) {
            // Handle the exception
        }
    } 

    class MyHandler extends DefaultHandler {
        // Your custom handler code goes here
    } 

    public boolean validateXML(InputStream xmlStream) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser parser = factory.newSAXParser();
            XMLReader reader = parser.getXMLReader();
            MyHandler handler = new MyHandler();
            reader.setContentHandler(handler);
            reader.parse(new InputSource(xmlStream));
            return handler.isValid();
        } catch (Exception e) {
            // Handle the exception
        }
        return false;
    } 

    class MyHandler extends DefaultHandler {
        private boolean isValid = true;
        // Your custom handler code goes here

        public boolean isValid() {
            return isValid;
        }
    } 





    public void parseXML(InputStream xmlStream) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser parser = factory.newSAXParser();
            XMLReader reader = parser.getXMLReader();
            MyHandler handler = new MyHandler();
            reader.setContentHandler(handler);
            reader.parse(new InputSource(xmlStream));
        } catch (Exception e) {
            // Handle the exception
        }
    } 

    class MyHandler extends DefaultHandler {
        // Your custom handler code goes here
    } 





    public boolean validateXML(InputStream xmlStream) {
        try {
            SAXParserFactory factory = SAXParserFactory.newInstance();
            SAXParser parser = factory.newSAXParser();
            XMLReader reader = parser.getXMLReader();
            MyHandler handler = new MyHandler();
            reader.setContentHandler(handler);
            reader.parse(new InputSource(xmlStream));
            return handler.isValid();
        } catch (Exception e) {
            // Handle the exception
        }
        return false;
    } 

    class MyHandler extends DefaultHandler {
        private boolean isValid = true;
        // Your custom handler code goes here

        public boolean isValid() {
            return isValid;
        }
    } 





    public void parseXML(InputStream xmlStream) {
        try {
            SAXParserFactory factory = SAX