    */

    using System.Xml;

    public class Program
    {
        public static void Main()
        {
            var doc = new XmlDocument();
            doc.Load("settings.xml");

            var tileSize = float.Parse(doc.GetElementsByTagName("tileSize")[0].InnerText);
            var worldWidth = int.Parse(doc.GetElementsByTagName("worldWidth")[0].InnerText);
            var worldHeight = int.Parse(doc.GetElementsByTagName("worldHeight")[0].InnerText);
            var cameraSpeed = float.Parse(doc.GetElementsByTagName("cameraSpeed")[0].InnerText);
        }
    }
}

//src/C#/Xml/XmlDocument/ReadXmlFile/Program.cs
﻿/*
Write a C# program that reads an XML file and prints out each element's name and inner text.
Only return the code, don't include any other information,
such as a preamble or suffix.
*/

using System;
using System.Xml;

public class Program
{
    public static void Main()
    {
        XmlDocument doc = new XmlDocument();
        doc.Load("file.xml");

        foreach (XmlNode node in doc.DocumentElement.ChildNodes)
        {
            Console.WriteLine($"Element: {node.Name}, Text: {node.InnerText}");
        }
    }
}

//src/C#/Xml/XmlDocument/SaveXmlFile/Program.cs
﻿/*
Write a C# program that saves an XML file with a root element "root". Inside the root element, it should have two child elements: "element1" and "element2".
The "element1" should have the text "Hello", and "element2" should have the text "World".
Only return the code, don't include any other information,
such as a preamble or suffix.
*/

using System.Xml;

public class Program
{
    public static void Main()
    {
        XmlDocument doc = new XmlDocument();

        XmlElement root = doc.CreateElement("root");
        doc.AppendChild