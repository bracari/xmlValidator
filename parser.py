from lxml import etree

class Parser:

    def __init__(self, xml_path: str):
        # xmldoc is an ElementTree
        self.xmldoc = etree.parse(xml_path)

    def getNodeValue(self, xml_node: str) -> str:
        # root is an Element
        root = self.xmldoc.getroot()

        for child in root:
            print(child.tag)

        elm = self.xmldoc.xpath(xml_node, namespaces={'cld:':'http://vler.va.gov/vler/schemas/health/clinicalDocuments/clinicalAssessments/cpExams/Claim/2.0',
            'cld':'http://vler.va.gov/vler/schemas/health/clinicalDocuments/clinicalAssessments/cpExams/Claim/2.0',
        	'nc':'http://niem.gov/niem/niem-core/2.0',
        	'vler':'http://va.gov/vler/schemas/vlerSupersetSchema/1.0/vler',
        	'niem-xsd':'http://niem.gov/niem/proxy/xsd/2.0',
        	's':'http://niem.gov/niem/structures/2.0',
        	'xsi':'http://www.w3.org/2001/XMLSchema-instance',
        	'pdshr':'http://vler.va.gov/vler/schemas/health/clinicalDocuments/clinicalAssessments/cpExams/PostDeploymentSeparationHealthReassessment/2.0'})
        #print(elm[0].tag)
        #print(elm[0].text)

        # To print the whole document:
        #print(etree.tostring(root, pretty_print=True))

        return elm[0].text
