    public static bool ValidateXmlAgainstXsd(string xml, string xsd)
    {
        XmlReaderSettings settings = new XmlReaderSettings();
        settings.Schemas.Add("", new XmlSchemaReader(new XmlTextReader(xsd)));
        XmlReader reader = XmlReader.Create(new StringReader(xml), settings);
        XmlSchema schema = settings.Schemas[""];

        bool isValid = false;
        while (reader.Read())
        {
            if (reader.NodeType == XmlNodeType.Element && reader.Name == "xs:schema")
            {
                isValid = schema.Validate(reader, null);
                break;
            }
        }

        return isValid;
    }