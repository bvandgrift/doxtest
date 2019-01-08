class PyClass(object):
    """ brief desc of PyClass with docstring

    a somewhat longer desc of pyclass
    with a line break, and some _italics_ and **bold** stuff
    """

    ## this is a thing
    thing = None

    def __init__(self):
        """
        constructor docs

        what else?
        """
        self.thing = 3

        ## this is another thing
        # with a few extra docs
        #
        # maybe it matters
        self.other_thing = None
        pass

    def a_method(self, args):
        """ 
        a method with docstring dox comments (doxpypy)

        a longer description of a_method
        args:
            args: the args
        returns:
            nothing
        """
        pass

    def another_method(self, args):
        """ another method with docstring comments (first line)

        a longer description of another_method
        @param args the arguments
        @returns the string "return"
        """
        return "return"

    def yet_another_method(self, args):
        # not documented
        pass


class PySubClass(PyClass):

    def a_method(self, args):
        """ a brief method override """
        pass

    def yet_another_method(self, args):
        """ yet another method override """
        pass
