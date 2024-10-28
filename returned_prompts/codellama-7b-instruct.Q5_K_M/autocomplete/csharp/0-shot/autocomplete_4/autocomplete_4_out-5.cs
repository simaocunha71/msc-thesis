
			xtr.ValidationType = ValidationType.Schema;
			xtr.Schemas.Add (XmlSchema.Read (xsr, null));
			xtr.Read ();
#endif
			xsr = new XmlTextReader (new StringReader (xsd));
			xvr.Schemas.Add (XmlSchema.Read (xsr, null));
			while (!xvr.EOF)
				xvr.Read ();
			xtr = new XmlTextReader (new StringReader (xml));
			xvr = new XmlValidatingReader (xtr);
			while (!xvr.EOF)
				xvr.Read ();
			xvr.Close ();
			xtr.Close ();
			xsr.Close ();
			xvr = null;
			xtr = null;
			xsr = null;
		}


