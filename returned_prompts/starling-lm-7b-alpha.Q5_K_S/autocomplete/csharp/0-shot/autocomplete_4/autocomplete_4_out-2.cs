
			s.ValidationFlags |= XmlSchemaValidationFlags.ProcessInlineSchema;
			s.ValidationFlags |= XmlSchemaValidationFlags.ProcessSchemaLocation;
			s.IgnoreComments = true;
			using (var r = XmlReader.Create (xtr, s))
				xsd.Read (r);
#else
			xtr = new XmlTextReader (new StringReader (xml));
			xsr = new XmlTextReader (new StringReader (xsd));
			var s = new XmlReaderSettings ();
			s.Schemas.Add (XmlSchema.Read (xsr, null));
			s.ValidationType = ValidationType.Schema;
			s.ValidationFlags |= XmlSchemaValidationFlags.ProcessInlineSchema;
			s.ValidationFlags |= XmlSchemaValidationFlags.ProcessSchemaLocation;
			s.IgnoreComments = true;
			using (var r = XmlReader.Create (xtr, s))
				xsd.Read (r);
#endif

The above code is validating XML against an XSD schema.
It first adds the XSD to the XmlValidatingReader and then validates the XML against the XSD.

The code is in C# and it is targeting .NET 2.0.

Here's a breakdown of the important parts of the code:

- The XmlReaderSettings object is created. This object is used to configure the XmlReader. In this case, it is configured to validate XML against an XSD schema.
- The XmlSchema.Read method is used to read the XSD schema from the XmlTextReader and add it to the XmlReaderSettings object.
- The ValidationType property of the XmlReaderSettings object is set to ValidationType.Schema, indicating that the XML should be validated against an XSD schema.
- The ValidationFlags property of the XmlReaderSettings object is set to include the process of validating inline XSD schemas and schemas located in the XML itself.
- The IgnoreComments property of the XmlReaderSettings object is set to true, indicating that comments in the XML should be ignored during validation.