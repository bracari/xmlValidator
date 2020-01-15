from lxml import etree

class Validator:

    def __init__(self, xsd_path: str):
        xmlschema_doc = etree.parse(xsd_path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)

    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)

        return result

    def assertValid(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.assertValid(xml_doc)

        return result

    def getLastError(self) -> str:
        return self.xmlschema.error_log.last_error

    def printErrors(self):
        for x in self.xmlschema.error_log:
            print(x)
