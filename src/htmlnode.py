class HTMLnode:
    def __init__(self, tag =None, value =None,
                  children =None, props =None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        atributes = ""
        for atribute in self.props:
            atributes+= f' {atribute}="{self.props[atribute]}"'
        return atributes
    
    def __repr__(self):
        print(f"Tag : {self.tag}")
        print(f"Value : {self.value}")
        print(f"Children : {self.children}")
        print(f"Prop : {self.props}")