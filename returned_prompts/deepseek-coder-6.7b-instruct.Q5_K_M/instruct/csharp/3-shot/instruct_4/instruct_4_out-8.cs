{
    public bool ValidateXml(string xmlFilePath, string xsdFilePath)
    {
        var settings = new XmlReaderSettings
        {
            ConformanceLevel = ConformanceLevel.Document
        };

        settings.ValidationEventHandler += (sender, args) => { throw new XmlSchemaValidationException(args.Message); };

        using (var reader = XmlReader.Create(xmlFilePath, settings))
        {
            var schemaSet = new XmlSchemaSet();
            schemaSet.Add(xsdFilePath);

            reader.MoveToContent();

            return schemaSet.Validate(reader).Count == 0;
        }
    }
}

