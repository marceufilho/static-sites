import unittest 
from htmlnode import HTMLnode

class testHTMLnode (unittest.TestCase):
    def test_two_props_to_html(self):
        prop = {
                 "href": "https://www.google.com", 
                 "target": "_blank",
        }
        prop_result =  ' href="https://www.google.com" target="_blank"'
        node = HTMLnode("<h1>", "Hello","<p>", prop)
        self.assertEqual(node.props_to_html(), prop_result)

    def test_three_props_to_html(self):
        prop = {
        "name": "viewport",
        "content": "width=device-width", 
        "initial-scale": "1.0",
        }
        prop_result = ' name="viewport" content="width=device-width" initial-scale="1.0"'
        node = HTMLnode("<h1>", "Hello","<p>", prop)
        self.assertEqual(node.props_to_html(), prop_result)

    
    def test_font_props_to_html(self):
        prop = {
         "rel": "preconnect",
         "href": "https://fonts.googleapis.com",
        }
        prop_result = ' rel="preconnect" href="https://fonts.googleapis.com"'
        node = HTMLnode("<h1>", "Hello","<p>", prop)
        self.assertEqual(node.props_to_html(), prop_result)    

def main():
    prop = {
            "href": "https://www.google.com", 
            "target": "_blank",
    }
    prop2 = {
        "name": "viewport",
        "content": "width=device-width", 
        "initial-scale": "1.0"
    }
    testHTMLnode.test_props_to_html(prop)
    testHTMLnode.test_props_to_html(prop2)


if __name__ == "__main__":
    unittest.main()