			xtr 		= XmlReader.Create  (new StringReader  (xml), s);
#endif
			
			while  (xtr.Read  ())
			{
				switch  (xtr.NodeType)
				{
				case XmlNodeType.Element:
					Console.Write  ("<{0}>", xtr.Name);
					break;
				case XmlNodeType.Text:
					Console.Write  (xtr.Value);
					break;
				case XmlNodeType.EndElement:
					Console.Write  ("</{0}>", xtr.Name);
					break;
				}
			}
