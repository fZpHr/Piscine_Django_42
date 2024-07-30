from elem import Elem

class Html(Elem):
    def __init__(self, content=None):
        super().__init__(tag='html', attr={}, content=content, tag_type='double')
    
    def __str__(self): 
        return super().__str__()

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(tag='head', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(tag='body', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(tag='title', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Meta(Elem):
    def __init__(self, content=None):
        super().__init__(tag='meta', attr={}, content=content, tag_type='simple')
    def __str__(self):
        return super().__str__()
    
class Img(Elem):
    def __init__(self, content=None):
        super().__init__(tag='img', attr={}, content=content, tag_type='simple')
    def __str__(self):
        return super().__str__()

class Table(Elem):
    def __init__(self, content=None):
        super().__init__(tag='table', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Th(Elem):
    def __init__(self, content=None):
        super().__init__(tag='th', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(tag='tr', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(tag='td', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ul', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(tag='ol', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Li(Elem):
    def __init__(self, content=None):
        super().__init__(tag='li', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h1', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()
    
class H2(Elem):
    def __init__(self, content=None):
        super().__init__(tag='h2', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class P(Elem):
    def __init__(self, content=None):
        super().__init__(tag='p', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Div(Elem):
    def __init__(self, content=None):
        super().__init__(tag='div', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Span(Elem):
    def __init__(self, content=None):
        super().__init__(tag='span', attr={}, content=content, tag_type='double')
    def __str__(self):
        return super().__str__()

class Hr(Elem):
    def __init__(self, content=None):
        super().__init__(tag='hr', attr={}, content=content, tag_type='simple')
    def __str__(self):
        return super().__str__()

class Br(Elem):
    def __init__(self, content=None):
        super().__init__(tag='br', attr={}, content=content, tag_type='simple')
    def __str__(self):
        return super().__str__()



if __name__ == '__main__':
    try:
        print(Html( [Head([Title('Hello ground!')]), Body()] ))
    except Exception as e:
        print(e)    