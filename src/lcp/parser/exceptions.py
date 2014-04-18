__author__ = 'Marcin'


class GrammarException(Exception):

    def __init__(self, value, msg):
        super(GrammarException, self).__init__(msg)
        self.value = value

    def get_error_msg(self):
        return "error: " + str(self.value) + ": " + self.message