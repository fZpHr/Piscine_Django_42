from elem import *
from elements import *

class Page:
    def __init__(self, elem=Elem()):
        if not isinstance(elem, Elem):
            raise Elem.ValidationError
        else:
            self.elem = elem
            self.elem.tag = (Html, Head, Body)
    def __str__(self):
            for each in self.elem.content:
                if (each not in self.elem.tag):
                    self.is_valid(False)
                if (each is Html and len(each.content) != 2):
                    self.is_valid(False)
                if (each is Html and len(each.content) == 2):
                    if (each.content[0] is not Head and each.content[1] is not Body):
                        self.is_valid(False)
                    if (each.content[0].content[0] is not Title or len(each.content[0].content) != 1):
                        self.is_valid(False)
                    if (each.content[1].content is not (H1, H2, Div, Table, Ul, Ol, Span, Text)):
                        self.is_valid(False)
                    if (each.content[1].content[0].content is not (Li, H1, H2, P, Div, Table, Ul, Ol, Span, Text)):
                        self.is_valid(False)
                else:
                    self.is_valid(False)
                

                
    def is_valid(self, state):
        if (state == True):
            return True
        else:
            return False