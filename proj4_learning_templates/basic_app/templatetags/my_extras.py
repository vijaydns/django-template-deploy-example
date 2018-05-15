from django import template

register = template.Library()

def cut(value, arg):

    """
    This cuts out all values of 'arg' from the string
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, 'hi')


# first arg is the name by which this function will be called in the script
register.filter('cut', cut)

def newcut(value, arg):

    """
    This cuts out all values of 'arg' from the string
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, 'hi')


# first arg is the name by which this function will be called in the script
register.filter('newcut', newcut)

