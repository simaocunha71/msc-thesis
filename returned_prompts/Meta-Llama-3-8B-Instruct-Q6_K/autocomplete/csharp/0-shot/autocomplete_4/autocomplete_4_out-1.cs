 // NET_2_0
#else
			xtr = new XmlTextReader (new StringReader (xml));
			xsr = new XmlTextReader (new StringReader (xsd));
#endif
			while (xtr.Read ())
				if (xtr.NodeType == XmlNodeType.Element && xtr.Name == "table" && xtr.GetAttribute ("type") == "simple")
					simpleTables.Add (xtr.GetAttribute ("name"));
				else if (xtr.NodeType == XmlNodeType.Element && xtr.Name == "table" && xtr.GetAttribute ("type") == "complex")
					complexTables.Add (xtr.GetAttribute ("name"));
				else if (xtr.NodeType == XmlNodeType.Element && xtr.Name == "field" && xtr.GetAttribute ("type") == "simple")
					simpleFields.Add (xtr.GetAttribute ("name"));
				else if (xtr.NodeType == XmlNodeType.Element && xtr.Name == "field" && xtr.GetAttribute ("type") == "complex")
					complexFields.Add (xtr.GetAttribute ("name")); // NET_2_0
			xtr.Close (); // NET_2_0
			xsr.Close (); // NET_2_0

The code is written in C# and appears to be parsing XML files to extract specific information. The code is written to work with .NET 2.0 and 3.5. The NET_2_0 comment indicates that some code is specific to .NET 2.0. The code is written to extract table and field names from an XML file and store them in a collection. The extracted information is then stored in the `simpleTables`, `complexTables`, `simpleFields`, and `complexFields` collections. The XML file is read using an `XmlTextReader` and the schema is read using an `XmlSchemaReader`.

Here's the next several lines of code:

			if (xvr.HasErrors)
				foreach (XmlSchemaValidationException ex in xvr.ErrorList)
					Console.WriteLine (ex.Message);
			else
				Console.WriteLine ("Schema validation successful");
			xvr.Close ();
			return;

This code checks if there were any errors during the validation of the XML file against its schema. If there were errors, it prints the error messages to the console. If there were no errors, it prints a success message to the console. Finally, it closes the `XmlReader` and returns from the method. 





Here