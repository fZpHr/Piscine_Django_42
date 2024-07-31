from elem import *

class Html(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='html', content=content, attr=kwargs, tag_type='double')

class Head(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='head', content=content, attr=kwargs, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='body', content=content, attr=kwargs, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='title', content=content, attr=kwargs, tag_type='double')

class Meta(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='meta', content=content, attr=kwargs, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='img', content=content, attr=kwargs, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='table', content=content, attr=kwargs, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='th', content=content, attr=kwargs, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='tr', content=content, attr=kwargs, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='td', content=content, attr=kwargs, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='ul', content=content, attr=kwargs, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='ol', content=content, attr=kwargs, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='li', content=content, attr=kwargs, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='h1', content=content, attr=kwargs, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='h2', content=content, attr=kwargs, tag_type='double')

class P(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='p', content=content, attr=kwargs, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='div', content=content, attr=kwargs, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='span', content=content, attr=kwargs, tag_type='double')

class Hr(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='hr', content=content, attr=kwargs, tag_type='simple')

class Br(Elem):
    def __init__(self, content=None, **kwargs):
        super().__init__(tag='br', content=content, attr=kwargs, tag_type='simple')


if __name__ == '__main__':
    try:
        print(Html([Head(Title(Text("Hello ground!"))), Body([H1(Text("Oh no, not again!")), Img(src='http://i.imgur.com/pfp3T.jpg')])]))
    except Exception as e:
        print(e)