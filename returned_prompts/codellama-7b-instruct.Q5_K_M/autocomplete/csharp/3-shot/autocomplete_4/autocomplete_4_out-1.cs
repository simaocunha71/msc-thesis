			xtr = XmlReader.Create (new StringReader (xml), s);
			while (!xtr.EOF)
				xtr.Read ();
#else
			xtr = new XmlTextReader (new StringReader (xml));
			xsr = new XmlTextReader (new StringReader (xsd));
			xsr.Schemas.Add (XmlSchema.Read (xsr, null));
			xtr.Schemas.Add (xsr);
			xtr.ValidationType = ValidationType.Schema;
			while (!xtr.EOF) {
				xtr.Read ();
#endif

