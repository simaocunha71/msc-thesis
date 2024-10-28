public bool ValidateXml(string xmlFilePath, string xsdFilePath)
{
    XmlReaderSettings settings = new XmlReaderSettings();
    settings.ValidationType = ValidationType.Schema;
    settings.ValidationFlags |= XmlSchemaValidationFlags.ReportValidationWarnings;
    settings.ValidationEventHandler += new ValidationEventHandler(ValidationEventHandler);

    XmlSchemaSet schemaSet = new XmlSchemaSet();
    schemaSet.Add("", xsdFilePath);

    XmlReader reader = XmlReader.Create(xmlFilePath, settings);

    try
    {
        while (reader.Read());
    }
    catch (XmlSchemaValidationException ex)
    {
        // Handle validation error
        Console.WriteLine("Validation error: " + ex.Message);
        return false;
    }
    finally
    {
        reader.Close();
    }

    return true;
}

private static void ValidationEventHandler(object sender, ValidationEventArgs e)
{
    switch (e.Severity)
    {
        case XmlSeverityType.Error:
            Console.WriteLine("Error: {0}", e.Message);
            break;
        case XmlSeverityType.Warning:
            Console.WriteLine("Warning: {0}", e.Message);
            break;
    }
}

