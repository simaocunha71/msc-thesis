
      parser.parse(is, handler);
    } catch (Exception e)  {
      throw new RuntimeException(e);
    }
  }
*/

/**
 * SAXParserFactory factory = SAXParserFactory.newInstance();
 * factory.setValidating(true);
 * SAXParser parser = factory.newSAXParser();
 * parser.parse(is, handler);
 */

//src/test/java/com/example/xml/sax/ManagedEntityConfigXmlParserTest.java
package com.example.xml.sax;

import com.example.config.DistributedSystemConfig;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.mockito.Mockito.*;

class ManagedEntityConfigXmlParserTest {

    private ManagedEntityConfigXmlParser parser;
    private DistributedSystemConfig config;

    @BeforeEach
    void setUp() {
        parser = new ManagedEntityConfigXmlParser();
        config = mock(DistributedSystemConfig.class);
        parser.config = config;
    }

    @Test
    void shouldParseXml() {
        // Given
        String xml = "<managed-entity></managed-entity>";
        InputStream is = new ByteArrayInputStream(xml.getBytes());

        // When
        parser.parse(is, config);

        // Then
        verify(config).addManagedEntity(any());
    }

}

//src/test/java/com/example/xml/sax/XmlParserTest.java
package com.example.xml.sax;

import com.example.config.DistributedSystemConfig;
import com.example.config.ManagedEntity;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import static org.mockito.Mockito.*;

class XmlParserTest {

    private ManagedEntityConfigXmlParser parser;