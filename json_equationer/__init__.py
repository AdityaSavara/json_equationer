#Try to do things a bit like https://github.com/python/cpython/blob/master/Lib/collections/__init__.py
#Except instead of putting things here directly in __init__, we'll import them so they are accessible by importing the module.
try:
    from json_equationer.evaluator import *
    from json_equationer.creator import *
except:
    from evaluator import *
    from creator import *
