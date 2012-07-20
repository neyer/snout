__doc__ = """
generate routes for methods using inspection. 

given a view like this:

def a_method_like_this(request,some_arg,another_arg): pass


snout will generate a route like this:
    ^a-method-like-this/(?P<some_arg>[\w\-\.]+)/(?P<another_arg>[\w\-\.]+)/?$
"""
__version__ = "1.0.1"

import inspect
import unittest


def starts_with_underscore(s):
    "does this name start with an underscore? this is the default test for non-view methods."
    return s.startswith("_")

def underscores_to_dashes(s):
    "turn underscores to dashes, because dashes are just so much more dashing"
    return s.replace("_","-")


def make_url_pattern(for_method,name_cleaner=underscores_to_dashes):
    args, varargs, varkw, defaults = inspect.getargspec(for_method)
    route_name= name_cleaner(for_method.__name__)

    #we ignore the first argument, because it is always 'requests'
    argument_components = [ '(?P<%s>[\w\-\.]+)' % arg for arg in args[1:] ]

    return "/".join(["^" + route_name] + argument_components + [ "?$"])  
    

def generate_url_routes(module, private_tester=starts_with_underscore,
                                name_cleaner=underscores_to_dashes,
                                index_view="index"):
    """inspect all functions in `module` and create a url pattern for each one."""

    all_methods = inspect.getmembers(module,inspect.isfunction)

    views = [ (name_cleaner(name), method) for\
                     name,method in all_methods if not private_tester(name)]  

    #extract any parameters from this function and use them to build the url 
    for name, method in views:
        if name == index_view:
            yield "^$", method
        else:
            yield make_url_pattern(method,name_cleaner), method


def make_django_patterns(module, prefix='', private_tester=starts_with_underscore,
                        name_cleaner=underscores_to_dashes,add_index=True):

    from django.conf.urls import patterns, url
    routes = [ url(regex,method)  for regex,method in\
                     generate_url_routes(module,private_tester,name_cleaner)]
    return patterns(prefix,*routes)

def index(pants):
    pass

def _this_should_not_be_a_route(its_here_for_tests_ok): pass

class SnoutTest(unittest.TestCase):
    def test_all_routes(self):
        "ROUTECEPTION"
        snout = inspect.getmodule(SnoutTest)

        all_snout_functions = inspect.getmembers(snout,inspect.isfunction)
        should_have_routes = [ name for name,f in all_snout_functions if not\
                                starts_with_underscore(name)]

        all_routes = list(generate_url_routes(snout))
        self.assertEqual(len(should_have_routes),len(all_routes))
