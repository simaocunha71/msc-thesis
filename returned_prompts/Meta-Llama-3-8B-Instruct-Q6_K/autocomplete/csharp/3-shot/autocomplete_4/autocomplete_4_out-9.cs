			using (XmlReader xmlReader = XmlReader.Create (new StringReader (xml), s))
			{
				while (xmlReader.Read ())
				{
					if (xmlReader.NodeType == XmlNodeType.Element && xmlReader.Name == "xs:schema")
					{
						xvr.Read (); // skip the xs:schema element
					}
					else if (xmlReader.NodeType == XmlNodeType.Element && xmlReader.Name == "xs:element")
					{
						// process the xs:element element
					}
					else if (xmlReader.NodeType == XmlNodeType.Element && xmlReader.Name == "xs:attribute")
					{
						// process the xs:attribute element
					}
					// ... process other elements ...
				}
			}

