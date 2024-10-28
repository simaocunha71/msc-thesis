
            doc.LoadXml(xml);
            XmlNodeList nodes = doc.GetElementsByTagName("Camera");
            for (int i = 0; i < nodes.Count; i++)
            {
                Camera.lowSpeed = Int32.Parse(nodes[i].Attributes["lowSpeed"].Value);
                Camera.highSpeed = Int32.Parse(nodes[i].Attributes["highSpeed"].Value);
            }
        }


You're working with XML data, which is structured text data. Therefore, you can use the `XmlDocument` class to parse the XML and extract the values you're interested in.

Here's a snippet of how you could do this:

```csharp
public static void load(String xml)
{
    XmlDocument doc = new XmlDocument();
    doc.LoadXml(xml);
    XmlNodeList nodes = doc.GetElementsByTagName("Camera");
    for (int i = 0; i < nodes.Count; i++)
    {
        Camera.lowSpeed = Int32.Parse(nodes[i].Attributes["lowSpeed"].Value);
        Camera.highSpeed = Int32.Parse(nodes[i].Attributes["highSpeed"].Value);
    }
}
```

This code loads an XML document from a string, then gets all the "Camera" elements in the XML. For each "Camera" element, it extracts the "lowSpeed" and "highSpeed" attributes and parses them into integers, which it then assigns to the `Camera.lowSpeed` and `Camera.highSpeed` fields.

Make sure that the XML string you're loading is well-formed and has the correct structure. If it doesn't, the `LoadXml` method will throw an exception.

Also, note that this code assumes that the XML document has the same structure as the one you provided. If the XML document has a different structure, you'll need to adjust this code to match the structure of the document.

This code also assumes that `Camera.lowSpeed` and `Camera.highSpeed` are static fields in the `Camera` class. If they're not, you'll need to adjust this code to use the correct objects