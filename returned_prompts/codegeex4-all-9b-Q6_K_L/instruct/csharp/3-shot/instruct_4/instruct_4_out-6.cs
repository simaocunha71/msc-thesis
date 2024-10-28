```csharp
using System.Xml;
using System.Xml.Schema;

public bool ValidateXml(string xmlString, string xsdString)
{
    XmlSchemaSet schemaSet = new XmlSchemaSet();
    XmlSchema schema = XmlSchema.Read(new XmlTextReader(new StringReader(xsdString)), null);
    schemaSet.Add(schema);
    schemaSet.Compile();

    XmlReaderSettings settings = new XmlReaderSettings();
    settings.ValidationType = ValidationType.Schema;
    settings.Schemas = schemaSet;

    try
    {
        using (XmlReader reader = XmlReader.Create(new StringReader(xmlString), settings))
        {
            while (reader.Read()) { }
        }
    }
    catch (XmlSchemaValidationException)
    {
        return false;
    }

    return true;
}
```