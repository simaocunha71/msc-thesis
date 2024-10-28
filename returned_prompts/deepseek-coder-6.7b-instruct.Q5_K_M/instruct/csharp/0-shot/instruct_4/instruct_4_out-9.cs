
```csharp
public static void ValidateXml(string xmlPath, string xsdPath)
{
    var settings = new XmlReaderSettings();
    settings.ValidationType = ValidationType.Schema;
    settings.ValidationFlags |= XmlSchemaValidationFlags.ProcessSchemaLocation;
    settings.ValidationFlags |= XmlSchemaValidationFlags.ReportValidationWarnings;

    settings.Schemas.Add(string.Empty, xsdPath);

    settings.ValidationEventHandler += (sender, e) =>
    {
        Console.WriteLine($"Validation error: {e.Message}");
    };

    var reader = XmlReader.Create(xmlPath, settings);

    while (reader.Read()) { }
}
```
