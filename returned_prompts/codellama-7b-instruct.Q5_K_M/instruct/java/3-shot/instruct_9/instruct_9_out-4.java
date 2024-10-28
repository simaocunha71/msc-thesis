public void parseXML(InputStream is) throws SAXException, IOException {
  SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
  parser.parse(is, new CustomHandler());
}
