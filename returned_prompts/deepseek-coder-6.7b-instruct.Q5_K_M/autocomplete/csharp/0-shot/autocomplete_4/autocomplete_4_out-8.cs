
			xvr = XmlReader.Create  (xtr, s);
#else
			xtr 
#endif
				.MoveToContent  ();
			while 
#if NET_2_0
				(!xvr.EOF)
#else
				(!xvr.EndOfStream)
#endif
				{
				xvr.Read  ();
				}
			xvr.Close  ();
			xsr.Close  ();
			xtr.Close  ();
*/

// The above code is incomplete, please write the missing parts and complete the code.

#if NET_2_0
			xtr = new XmlTextReader(new StringReader(xml));
			xsr = new XmlTextReader(new StringReader(xsd));
			var s = new XmlReaderSettings();
			s.Schemas.Add(XmlSchema.Read(xsr, null));
			s.ValidationType = ValidationType.Schema;
			xvr = XmlReader.Create(xtr, s);
#else
			xtr = new XmlStreamReader(new StringReader(xml));
			xsr = new XmlStreamReader(new StringReader(xsd));
			XmlReaderSettings s = new XmlReaderSettings();
			s.Schemas.Add(XmlSchema.Read(xsr, null));
			s.ValidationType = ValidationType.Schema;
			xvr = XmlReader.Create(xtr, s);
#endif
			xvr.MoveToContent();
			while (!xvr.EndOfStream)
			{
				xvr.Read();
			}
			xvr.Close();
			xsr.Close();
			xtr.Close();
		}
	}
}

//Program.cs
﻿using System;
using System.IO;
using System.Xml;
using System.Xml.Schema;
using XmlSchemaValidator.Classes;

namespace XmlSchemaValidator
{
	class Program
	{
		static void Main(string[] args)
		{
			string xsd = File.ReadAllText("sample.x