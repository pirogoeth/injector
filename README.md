injector
========

Dynamic injector for tracers and other neat things.


Usage
-----

```
import injector

payload_a = {
    'a': 1,
    'b': 2,
}

gen_dec = injector.generate_injector(payload_a, as_name='example')

@gen_dec
def some_func():
    print example

@gen_dec
def other_func(arg1, arg2):
    print arg1
    print arg2
    print example

print 'some_func'
some_func()

# some_func
# {'a': 1, 'b': 2}

print 'other_func'
other_func('hello', 'world')
# other_func
# hello
# world
# {'a': 1, 'b': 2}
```
