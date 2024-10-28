using System;
using System.IO;
using System.Xml;
using System.Xml.Schema;

public class XmlValidator
{
    static void Validate(string xmlFile, string xsdFile)
    {
        XmlSchemaSet schemas = new XmlSchemaSet();
        schemas.ValidationEventHandler += new ValidationEventHandler(ValidationCallBack);
        schemas.Add(null, XmlReader.Create(new StringReader(xsdFile)));

        XmlReaderSettings settings = new XmlReaderSettings();
        settings.Schemas = schemas;
        settings.ValidationType = ValidationType.Schema;

        XmlReader reader = XmlReader.Create(xmlFile, settings);
        while (reader.Read())
        {
            // do something
        }
    }

    static void ValidationCallBack(object sender, ValidationEventArgs e)
    {
        Console.WriteLine("Validation {0}", e.Severity);
    }
}

