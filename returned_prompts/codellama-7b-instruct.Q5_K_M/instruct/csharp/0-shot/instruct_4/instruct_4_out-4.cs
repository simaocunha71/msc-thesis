
    private static bool ValidateXml(string xml, string xsd)
    {
        XmlSchemaSet schemas = new XmlSchemaSet();
        schemas.Add(null, xsd);
        XmlReaderSettings settings = new XmlReaderSettings();
        settings.ValidationType = ValidationType.Schema;
        settings.Schemas = schemas;
        settings.ValidationFlags |= XmlSchemaValidationFlags.ProcessInlineSchema;
        settings.ValidationFlags |= XmlSchemaValidationFlags.ProcessSchemaLocation;
        settings.ValidationFlags |= XmlSchemaValidationFlags.ReportValidationWarnings;
        settings.ValidationEventHandler += (sender, e) =>
        {
            if (e.Severity == XmlSeverityType.Warning)
                Console.WriteLine("WARNING: Line {0}, Position {1}, {2}", e.Exception.LineNumber, e.Exception.LinePosition, e.Message);
            else if (e.Severity == XmlSeverityType.Error)
                Console.WriteLine("ERROR: Line {0}, Position {1}, {2}", e.Exception.LineNumber, e.Exception.LinePosition, e.Message);
        };
        using (XmlReader reader = XmlReader.Create(new StringReader(xml), settings))
        {
            while (reader.Read()) ;
        }
        return !schemas.Any();
    }

