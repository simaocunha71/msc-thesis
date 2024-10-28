    
    public bool ValidateXmlAgainstXsd(string xml, string xsd)
    {
        XmlReaderSettings settings = new XmlReaderSettings();
        settings.Schemas.Add("", xsd);
        settings.ValidationType = ValidationType.Schema;
        XmlReader reader = XmlReader.Create(new StringReader(xml), settings);
        bool isValid = false;
        while (reader.Read())
        {
            if (reader.NodeType == XmlNodeType.EndElement)
            {
                isValid = reader.ValidationType == ValidationType.Schema;
                break;
            }
        }
        return isValid;
    }