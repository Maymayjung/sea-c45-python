#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    IND_LEVEL = "    "

    def __init__(self, name="", content="", **kwargs):
        self.name = name
        self.children = [content] if content else []
        self.attributes = kwargs

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent=""):
        if self.attributes != {}:
            file_out.write("%s<%s " % (indent, self.name))
            print(self.attributes)
            for key, value in self.attributes.items():
                file_out.write('%s="%s"' % (key, value))
            file_out.write(">\n")
        else:
            file_out.write("%s<%s>\n" % (indent, self.name))
        for child in self.children:
            if (type(child) == str):
                file_out.write(indent + Element.IND_LEVEL + child + "\n")
            else:
                child.render(file_out, indent + Element.IND_LEVEL)
        file_out.write("%s</%s>\n" % (indent, self.name))


class Html(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name="html", content="")

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, indent="")


class Body(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name="body", content=content)


class P(Element):

    def __init__(self, content="", **kwargs):
        Element.__init__(self, content=content, name="p", **kwargs)


class Head(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name="head", content=content)


class Title(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="title", content=content)

    def render(self, file_out, indent=""):
        OneLineTag.render(self, file_out, indent=indent)


class OneLineTag(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name=name, content=content)

    def render(self, file_out, indent=""):
        file_out.write("%s<%s>" % (indent, self.name))
        for child in self.children:
            if (type(child) == str):
                file_out.write(child)
            else:
                child.render(file_out, indent + Element.IND_LEVEL)
        file_out.write("</%s>\n" % (self.name))


class SelfClosingTag(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name=name, content=content)

    def render(self, file_out, indent=""):
        file_out.write("%s<%s />\n" % (indent, self.name))


class Hr(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="hr", content=content)

    def render(self, file_out, indent=""):
        SelfClosingTag.render(self, file_out, indent=indent)


class Br(Element):

    def __init__(self, content=""):
        Element.__init__(self, name="br", content=content)

    def render(self, file_out, indent=""):
        SelfClosingTag.render(self, file_out, indent=indent)


class A(Element):

    def __init__(self, link="", name=""):
        self.link = link
        self.name = name

    def render(self, file_out, indent=""):
        file_out.write('%s<a href="%s">%s</a>\n' % (indent,
                                                    self.link,
                                                    self.name))
