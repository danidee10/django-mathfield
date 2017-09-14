__all__ = ['katex']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'r', 't'])
    pass
    @Js
    def PyJs_anonymous_2_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_v_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_3_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_3_)
        PyJsHoisted_v_.func_name = 'v'
        var.put('v', PyJsHoisted_v_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./src/ParseError')))
        var.put('n', var.get('v')(var.get('a')))
        var.put('i', var.get('e')(Js('./src/Settings')))
        var.put('l', var.get('v')(var.get('i')))
        var.put('s', var.get('e')(Js('./src/buildTree')))
        var.put('o', var.get('v')(var.get('s')))
        var.put('u', var.get('e')(Js('./src/parseTree')))
        var.put('c', var.get('v')(var.get('u')))
        var.put('f', var.get('e')(Js('./src/utils')))
        var.put('h', var.get('v')(var.get('f')))
        pass
        @Js
        def PyJs_e_4_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_4_}, var)
            var.registers(['i', 'r', 'n', 's', 'a', 't'])
            var.get('h').get('default').callprop('clearNode', var.get('r'))
            var.put('n', var.get('l').get('default').create(var.get('a')))
            var.put('i', PyJsComma(Js(0.0),var.get('c').get('default'))(var.get('t'), var.get('n')))
            var.put('s', PyJsComma(Js(0.0),var.get('o').get('default'))(var.get('i'), var.get('t'), var.get('n')).callprop('toNode'))
            var.get('r').callprop('appendChild', var.get('s'))
        PyJs_e_4_._set_name('e')
        var.put('d', PyJs_e_4_)
        if PyJsStrictNeq(var.get('document',throw=False).typeof(),Js('undefined')):
            if PyJsStrictNeq(var.get('document').get('compatMode'),Js('CSS1Compat')):
                (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', (Js("Warning: KaTeX doesn't work in quirks mode. Make sure your ")+Js('website has a suitable doctype.'))))
                @Js
                def PyJs_e_5_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_5_}, var)
                    var.registers([])
                    PyJsTempException = JsToPyException(var.get('n').get('default').create(Js("KaTeX doesn't work in quirks mode.")))
                    raise PyJsTempException
                PyJs_e_5_._set_name('e')
                var.put('d', PyJs_e_5_)
        @Js
        def PyJs_e_6_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_6_}, var)
            var.registers(['r', 'a', 'n', 't'])
            var.put('a', var.get('l').get('default').create(var.get('r')))
            var.put('n', PyJsComma(Js(0.0),var.get('c').get('default'))(var.get('t'), var.get('a')))
            return PyJsComma(Js(0.0),var.get('o').get('default'))(var.get('n'), var.get('t'), var.get('a')).callprop('toMarkup')
        PyJs_e_6_._set_name('e')
        var.put('p', PyJs_e_6_)
        @Js
        def PyJs_e_7_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_7_}, var)
            var.registers(['r', 'a', 't'])
            var.put('a', var.get('l').get('default').create(var.get('r')))
            return PyJsComma(Js(0.0),var.get('c').get('default'))(var.get('t'), var.get('a'))
        PyJs_e_7_._set_name('e')
        var.put('m', PyJs_e_7_)
        PyJs_Object_8_ = Js({'render':var.get('d'),'renderToString':var.get('p'),'__parse':var.get('m'),'ParseError':var.get('n').get('default')})
        var.get('t').put('exports', PyJs_Object_8_)
    PyJs_anonymous_2_._set_name('anonymous')
    PyJs_Object_9_ = Js({'./src/ParseError':Js(29.0),'./src/Settings':Js(32.0),'./src/buildTree':Js(37.0),'./src/parseTree':Js(46.0),'./src/utils':Js(51.0)})
    @Js
    def PyJs_anonymous_10_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        PyJs_Object_11_ = Js({'default':var.get('e')(Js('core-js/library/fn/json/stringify')),'__esModule':Js(True)})
        var.get('t').put('exports', PyJs_Object_11_)
    PyJs_anonymous_10_._set_name('anonymous')
    PyJs_Object_12_ = Js({'core-js/library/fn/json/stringify':Js(6.0)})
    @Js
    def PyJs_anonymous_13_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        PyJs_Object_14_ = Js({'default':var.get('e')(Js('core-js/library/fn/object/define-property')),'__esModule':Js(True)})
        var.get('t').put('exports', PyJs_Object_14_)
    PyJs_anonymous_13_._set_name('anonymous')
    PyJs_Object_15_ = Js({'core-js/library/fn/object/define-property':Js(7.0)})
    @Js
    def PyJs_anonymous_16_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        Js('use strict')
        var.get('r').put('__esModule', Js(True))
        @Js
        def PyJs_anonymous_17_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            if var.get('e').instanceof(var.get('t')).neg():
                PyJsTempException = JsToPyException(var.get('TypeError').create(Js('Cannot call a class as a function')))
                raise PyJsTempException
        PyJs_anonymous_17_._set_name('anonymous')
        var.get('r').put('default', PyJs_anonymous_17_)
    PyJs_anonymous_16_._set_name('anonymous')
    PyJs_Object_18_ = Js({})
    @Js
    def PyJs_anonymous_19_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_20_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_20_)
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        Js('use strict')
        var.get('r').put('__esModule', Js(True))
        var.put('a', var.get('e')(Js('../core-js/object/define-property')))
        var.put('n', var.get('i')(var.get('a')))
        pass
        @Js
        def PyJs_anonymous_21_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(e, t, this, arguments, var=var):
                var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['e', 'r', 'a', 't'])
                #for JS loop
                var.put('r', Js(0.0))
                while (var.get('r')<var.get('t').get('length')):
                    try:
                        var.put('a', var.get('t').get(var.get('r')))
                        var.get('a').put('enumerable', (var.get('a').get('enumerable') or Js(False)))
                        var.get('a').put('configurable', Js(True))
                        if var.get('a').contains(Js('value')):
                            var.get('a').put('writable', Js(True))
                        PyJsComma(Js(0.0),var.get('n').get('default'))(var.get('e'), var.get('a').get('key'), var.get('a'))
                    finally:
                            (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_anonymous_22_(t, r, a, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 'a', 't'])
                if var.get('r'):
                    var.get('e')(var.get('t').get('prototype'), var.get('r'))
                if var.get('a'):
                    var.get('e')(var.get('t'), var.get('a'))
                return var.get('t')
            PyJs_anonymous_22_._set_name('anonymous')
            return PyJs_anonymous_22_
        PyJs_anonymous_21_._set_name('anonymous')
        var.get('r').put('default', PyJs_anonymous_21_())
    PyJs_anonymous_19_._set_name('anonymous')
    PyJs_Object_23_ = Js({'../core-js/object/define-property':Js(3.0)})
    @Js
    def PyJs_anonymous_24_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'n', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('../../modules/_core')))
        PyJs_Object_25_ = Js({'stringify':var.get('JSON').get('stringify')})
        var.put('n', (var.get('a').get('JSON') or var.get('a').put('JSON', PyJs_Object_25_)))
        @Js
        def PyJs_e_26_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_26_}, var)
            var.registers(['t'])
            return var.get('n').get('stringify').callprop('apply', var.get('n'), var.get('arguments'))
        PyJs_e_26_._set_name('e')
        var.get('t').put('exports', PyJs_e_26_)
    PyJs_anonymous_24_._set_name('anonymous')
    PyJs_Object_27_ = Js({'../../modules/_core':Js(10.0)})
    @Js
    def PyJs_anonymous_28_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.get('e')(Js('../../modules/es6.object.define-property'))
        var.put('a', var.get('e')(Js('../../modules/_core')).get('Object'))
        @Js
        def PyJs_e_29_(t, r, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_29_}, var)
            var.registers(['r', 'n', 't'])
            return var.get('a').callprop('defineProperty', var.get('t'), var.get('r'), var.get('n'))
        PyJs_e_29_._set_name('e')
        var.get('t').put('exports', PyJs_e_29_)
    PyJs_anonymous_28_._set_name('anonymous')
    PyJs_Object_30_ = Js({'../../modules/_core':Js(10.0),'../../modules/es6.object.define-property':Js(23.0)})
    @Js
    def PyJs_anonymous_31_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_32_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            if (var.get('e',throw=False).typeof()!=Js('function')):
                PyJsTempException = JsToPyException(var.get('TypeError')((var.get('e')+Js(' is not a function!'))))
                raise PyJsTempException
            return var.get('e')
        PyJs_anonymous_32_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_32_)
    PyJs_anonymous_31_._set_name('anonymous')
    PyJs_Object_33_ = Js({})
    @Js
    def PyJs_anonymous_34_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_is-object')))
        @Js
        def PyJs_anonymous_35_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            if var.get('a')(var.get('e')).neg():
                PyJsTempException = JsToPyException(var.get('TypeError')((var.get('e')+Js(' is not an object!'))))
                raise PyJsTempException
            return var.get('e')
        PyJs_anonymous_35_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_35_)
    PyJs_anonymous_34_._set_name('anonymous')
    PyJs_Object_36_ = Js({'./_is-object':Js(19.0)})
    @Js
    def PyJs_anonymous_37_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        PyJs_Object_38_ = Js({'version':Js('2.4.0')})
        var.put('a', var.get('t').put('exports', PyJs_Object_38_))
        if (var.get('__e',throw=False).typeof()==Js('number')):
            var.put('__e', var.get('a'))
    PyJs_anonymous_37_._set_name('anonymous')
    PyJs_Object_39_ = Js({})
    @Js
    def PyJs_anonymous_40_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_a-function')))
        @Js
        def PyJs_anonymous_41_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.get('a')(var.get('e'))
            if PyJsStrictEq(var.get('t'),var.get('undefined')):
                return var.get('e')
            while 1:
                SWITCHED = False
                CONDITION = (var.get('r'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_42_(r, this, arguments, var=var):
                        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r'])
                        return var.get('e').callprop('call', var.get('t'), var.get('r'))
                    PyJs_anonymous_42_._set_name('anonymous')
                    return PyJs_anonymous_42_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_43_(r, a, this, arguments, var=var):
                        var = Scope({'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r', 'a'])
                        return var.get('e').callprop('call', var.get('t'), var.get('r'), var.get('a'))
                    PyJs_anonymous_43_._set_name('anonymous')
                    return PyJs_anonymous_43_
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    @Js
                    def PyJs_anonymous_44_(r, a, n, this, arguments, var=var):
                        var = Scope({'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r', 'a', 'n'])
                        return var.get('e').callprop('call', var.get('t'), var.get('r'), var.get('a'), var.get('n'))
                    PyJs_anonymous_44_._set_name('anonymous')
                    return PyJs_anonymous_44_
                SWITCHED = True
                break
            @Js
            def PyJs_anonymous_45_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return var.get('e').callprop('apply', var.get('t'), var.get('arguments'))
            PyJs_anonymous_45_._set_name('anonymous')
            return PyJs_anonymous_45_
        PyJs_anonymous_41_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_41_)
    PyJs_anonymous_40_._set_name('anonymous')
    PyJs_Object_46_ = Js({'./_a-function':Js(8.0)})
    @Js
    def PyJs_anonymous_47_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_48_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            PyJs_Object_49_ = Js({})
            @Js
            def PyJs_anonymous_51_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return Js(7.0)
            PyJs_anonymous_51_._set_name('anonymous')
            PyJs_Object_50_ = Js({'get':PyJs_anonymous_51_})
            return (var.get('Object').callprop('defineProperty', PyJs_Object_49_, Js('a'), PyJs_Object_50_).get('a')!=Js(7.0))
        PyJs_anonymous_48_._set_name('anonymous')
        var.get('t').put('exports', var.get('e')(Js('./_fails'))(PyJs_anonymous_48_).neg())
    PyJs_anonymous_47_._set_name('anonymous')
    PyJs_Object_52_ = Js({'./_fails':Js(15.0)})
    @Js
    def PyJs_anonymous_53_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r', 'n', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_is-object')))
        var.put('n', var.get('e')(Js('./_global')).get('document'))
        var.put('i', (var.get('a')(var.get('n')) and var.get('a')(var.get('n').get('createElement'))))
        @Js
        def PyJs_anonymous_54_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_55_ = Js({})
            return (var.get('n').callprop('createElement', var.get('e')) if var.get('i') else PyJs_Object_55_)
        PyJs_anonymous_54_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_54_)
    PyJs_anonymous_53_._set_name('anonymous')
    PyJs_Object_56_ = Js({'./_global':Js(16.0),'./_is-object':Js(19.0)})
    @Js
    def PyJs_anonymous_57_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'o', 'n', 's', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_global')))
        var.put('n', var.get('e')(Js('./_core')))
        var.put('i', var.get('e')(Js('./_ctx')))
        var.put('l', var.get('e')(Js('./_hide')))
        var.put('s', Js('prototype'))
        @Js
        def PyJs_anonymous_58_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'm', 'h', 'r', 'v', 'c', 'x', 'g', 'w', 'd', 'u', 'e', 'y', 'f', 't'])
            var.put('u', (var.get('e')&var.get('o').get('F')))
            var.put('c', (var.get('e')&var.get('o').get('G')))
            var.put('f', (var.get('e')&var.get('o').get('S')))
            var.put('h', (var.get('e')&var.get('o').get('P')))
            var.put('v', (var.get('e')&var.get('o').get('B')))
            var.put('d', (var.get('e')&var.get('o').get('W')))
            PyJs_Object_59_ = Js({})
            var.put('p', (var.get('n') if var.get('c') else (var.get('n').get(var.get('t')) or var.get('n').put(var.get('t'), PyJs_Object_59_))))
            var.put('m', var.get('p').get(var.get('s')))
            PyJs_Object_60_ = Js({})
            var.put('g', (var.get('a') if var.get('c') else (var.get('a').get(var.get('t')) if var.get('f') else (var.get('a').get(var.get('t')) or PyJs_Object_60_).get(var.get('s')))))
            if var.get('c'):
                var.put('r', var.get('t'))
            for PyJsTemp in var.get('r'):
                var.put('y', PyJsTemp)
                var.put('x', ((var.get('u').neg() and var.get('g')) and PyJsStrictNeq(var.get('g').get(var.get('y')),var.get('undefined'))))
                if (var.get('x') and var.get('p').contains(var.get('y'))):
                    continue
                var.put('w', (var.get('g').get(var.get('y')) if var.get('x') else var.get('r').get(var.get('y'))))
                def PyJs_LONG_63_(var=var):
                    @Js
                    def PyJs_anonymous_61_(e, this, arguments, var=var):
                        var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                        var.registers(['e', 't'])
                        @Js
                        def PyJs_anonymous_62_(t, r, a, this, arguments, var=var):
                            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
                            var.registers(['r', 'a', 't'])
                            if var.get(u"this").instanceof(var.get('e')):
                                while 1:
                                    SWITCHED = False
                                    CONDITION = (var.get('arguments').get('length'))
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                                        SWITCHED = True
                                        return var.get('e').create()
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                                        SWITCHED = True
                                        return var.get('e').create(var.get('t'))
                                    if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                                        SWITCHED = True
                                        return var.get('e').create(var.get('t'), var.get('r'))
                                    SWITCHED = True
                                    break
                                return var.get('e').create(var.get('t'), var.get('r'), var.get('a'))
                            return var.get('e').callprop('apply', var.get(u"this"), var.get('arguments'))
                        PyJs_anonymous_62_._set_name('anonymous')
                        var.put('t', PyJs_anonymous_62_)
                        var.get('t').put(var.get('s'), var.get('e').get(var.get('s')))
                        return var.get('t')
                    PyJs_anonymous_61_._set_name('anonymous')
                    return (var.get('r').get(var.get('y')) if (var.get('c') and (var.get('g').get(var.get('y')).typeof()!=Js('function'))) else (var.get('i')(var.get('w'), var.get('a')) if (var.get('v') and var.get('x')) else (PyJs_anonymous_61_(var.get('w')) if (var.get('d') and (var.get('g').get(var.get('y'))==var.get('w'))) else (var.get('i')(var.get('Function').get('call'), var.get('w')) if (var.get('h') and (var.get('w',throw=False).typeof()==Js('function'))) else var.get('w')))))
                var.get('p').put(var.get('y'), PyJs_LONG_63_())
                if var.get('h'):
                    PyJs_Object_64_ = Js({})
                    (var.get('p').get('virtual') or var.get('p').put('virtual', PyJs_Object_64_)).put(var.get('y'), var.get('w'))
                    if (((var.get('e')&var.get('o').get('R')) and var.get('m')) and var.get('m').get(var.get('y')).neg()):
                        var.get('l')(var.get('m'), var.get('y'), var.get('w'))
        PyJs_anonymous_58_._set_name('anonymous')
        var.put('o', PyJs_anonymous_58_)
        var.get('o').put('F', Js(1.0))
        var.get('o').put('G', Js(2.0))
        var.get('o').put('S', Js(4.0))
        var.get('o').put('P', Js(8.0))
        var.get('o').put('B', Js(16.0))
        var.get('o').put('W', Js(32.0))
        var.get('o').put('U', Js(64.0))
        var.get('o').put('R', Js(128.0))
        var.get('t').put('exports', var.get('o'))
    PyJs_anonymous_57_._set_name('anonymous')
    PyJs_Object_65_ = Js({'./_core':Js(10.0),'./_ctx':Js(11.0),'./_global':Js(16.0),'./_hide':Js(17.0)})
    @Js
    def PyJs_anonymous_66_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_67_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            try:
                return var.get('e')().neg().neg()
            except PyJsException as PyJsTempException:
                PyJsHolder_65_84632003 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(True)
                finally:
                    if PyJsHolder_65_84632003 is not None:
                        var.own['e'] = PyJsHolder_65_84632003
                    else:
                        del var.own['e']
                    del PyJsHolder_65_84632003
        PyJs_anonymous_67_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_67_)
    PyJs_anonymous_66_._set_name('anonymous')
    PyJs_Object_68_ = Js({})
    @Js
    def PyJs_anonymous_69_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.put('a', var.get('t').put('exports', (var.get('window') if ((var.get('window',throw=False).typeof()!=Js('undefined')) and (var.get('window').get('Math')==var.get('Math'))) else (var.get('self') if ((var.get('self',throw=False).typeof()!=Js('undefined')) and (var.get('self').get('Math')==var.get('Math'))) else var.get('Function')(Js('return this'))()))))
        if (var.get('__g',throw=False).typeof()==Js('number')):
            var.put('__g', var.get('a'))
    PyJs_anonymous_69_._set_name('anonymous')
    PyJs_Object_70_ = Js({})
    @Js
    def PyJs_anonymous_71_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'n', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_object-dp')))
        var.put('n', var.get('e')(Js('./_property-desc')))
        @Js
        def PyJs_anonymous_72_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            return var.get('a').callprop('f', var.get('e'), var.get('t'), var.get('n')(Js(1.0), var.get('r')))
        PyJs_anonymous_72_._set_name('anonymous')
        @Js
        def PyJs_anonymous_73_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.get('e').put(var.get('t'), var.get('r'))
            return var.get('e')
        PyJs_anonymous_73_._set_name('anonymous')
        var.get('t').put('exports', (PyJs_anonymous_72_ if var.get('e')(Js('./_descriptors')) else PyJs_anonymous_73_))
    PyJs_anonymous_71_._set_name('anonymous')
    PyJs_Object_74_ = Js({'./_descriptors':Js(12.0),'./_object-dp':Js(20.0),'./_property-desc':Js(21.0)})
    @Js
    def PyJs_anonymous_75_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_76_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            @Js
            def PyJs_anonymous_78_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                return Js(7.0)
            PyJs_anonymous_78_._set_name('anonymous')
            PyJs_Object_77_ = Js({'get':PyJs_anonymous_78_})
            return (var.get('Object').callprop('defineProperty', var.get('e')(Js('./_dom-create'))(Js('div')), Js('a'), PyJs_Object_77_).get('a')!=Js(7.0))
        PyJs_anonymous_76_._set_name('anonymous')
        var.get('t').put('exports', (var.get('e')(Js('./_descriptors')).neg() and var.get('e')(Js('./_fails'))(PyJs_anonymous_76_).neg()))
    PyJs_anonymous_75_._set_name('anonymous')
    PyJs_Object_79_ = Js({'./_descriptors':Js(12.0),'./_dom-create':Js(13.0),'./_fails':Js(15.0)})
    @Js
    def PyJs_anonymous_80_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_81_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            return (PyJsStrictNeq(var.get('e'),var.get(u"null")) if PyJsStrictEq(var.get('e',throw=False).typeof(),Js('object')) else PyJsStrictEq(var.get('e',throw=False).typeof(),Js('function')))
        PyJs_anonymous_81_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_81_)
    PyJs_anonymous_80_._set_name('anonymous')
    PyJs_Object_82_ = Js({})
    @Js
    def PyJs_anonymous_83_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_an-object')))
        var.put('n', var.get('e')(Js('./_ie8-dom-define')))
        var.put('i', var.get('e')(Js('./_to-primitive')))
        var.put('l', var.get('Object').get('defineProperty'))
        @Js
        def PyJs_e_84_(t, r, s, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 's':s, 'this':this, 'arguments':arguments, 'e':PyJs_e_84_}, var)
            var.registers(['r', 's', 't'])
            var.get('a')(var.get('t'))
            var.put('r', var.get('i')(var.get('r'), Js(True)))
            var.get('a')(var.get('s'))
            if var.get('n'):
                try:
                    return var.get('l')(var.get('t'), var.get('r'), var.get('s'))
                except PyJsException as PyJsTempException:
                    PyJsHolder_65_16727245 = var.own.get('e')
                    var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                    try:
                        pass
                    finally:
                        if PyJsHolder_65_16727245 is not None:
                            var.own['e'] = PyJsHolder_65_16727245
                        else:
                            del var.own['e']
                        del PyJsHolder_65_16727245
            if (var.get('s').contains(Js('get')) or var.get('s').contains(Js('set'))):
                PyJsTempException = JsToPyException(var.get('TypeError')(Js('Accessors not supported!')))
                raise PyJsTempException
            if var.get('s').contains(Js('value')):
                var.get('t').put(var.get('r'), var.get('s').get('value'))
            return var.get('t')
        PyJs_e_84_._set_name('e')
        var.get('r').put('f', (var.get('Object').get('defineProperty') if var.get('e')(Js('./_descriptors')) else PyJs_e_84_))
    PyJs_anonymous_83_._set_name('anonymous')
    PyJs_Object_85_ = Js({'./_an-object':Js(9.0),'./_descriptors':Js(12.0),'./_ie8-dom-define':Js(18.0),'./_to-primitive':Js(22.0)})
    @Js
    def PyJs_anonymous_86_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        @Js
        def PyJs_anonymous_87_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            PyJs_Object_88_ = Js({'enumerable':(var.get('e')&Js(1.0)).neg(),'configurable':(var.get('e')&Js(2.0)).neg(),'writable':(var.get('e')&Js(4.0)).neg(),'value':var.get('t')})
            return PyJs_Object_88_
        PyJs_anonymous_87_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_87_)
    PyJs_anonymous_86_._set_name('anonymous')
    PyJs_Object_89_ = Js({})
    @Js
    def PyJs_anonymous_90_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_is-object')))
        @Js
        def PyJs_anonymous_91_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'n', 't'])
            if var.get('a')(var.get('e')).neg():
                return var.get('e')
            pass
            if ((var.get('t') and (var.put('r', var.get('e').get('toString')).typeof()==Js('function'))) and var.get('a')(var.put('n', var.get('r').callprop('call', var.get('e')))).neg()):
                return var.get('n')
            if ((var.put('r', var.get('e').get('valueOf')).typeof()==Js('function')) and var.get('a')(var.put('n', var.get('r').callprop('call', var.get('e')))).neg()):
                return var.get('n')
            if ((var.get('t').neg() and (var.put('r', var.get('e').get('toString')).typeof()==Js('function'))) and var.get('a')(var.put('n', var.get('r').callprop('call', var.get('e')))).neg()):
                return var.get('n')
            PyJsTempException = JsToPyException(var.get('TypeError')(Js("Can't convert object to primitive value")))
            raise PyJsTempException
        PyJs_anonymous_91_._set_name('anonymous')
        var.get('t').put('exports', PyJs_anonymous_91_)
    PyJs_anonymous_90_._set_name('anonymous')
    PyJs_Object_92_ = Js({'./_is-object':Js(19.0)})
    @Js
    def PyJs_anonymous_93_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        var.put('a', var.get('e')(Js('./_export')))
        PyJs_Object_94_ = Js({'defineProperty':var.get('e')(Js('./_object-dp')).get('f')})
        var.get('a')((var.get('a').get('S')+(var.get('a').get('F')*var.get('e')(Js('./_descriptors')).neg())), Js('Object'), PyJs_Object_94_)
    PyJs_anonymous_93_._set_name('anonymous')
    PyJs_Object_95_ = Js({'./_descriptors':Js(12.0),'./_export':Js(14.0),'./_object-dp':Js(20.0)})
    @Js
    def PyJs_anonymous_96_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_a_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            if var.get('e').get('__matchAtRelocatable').neg():
                var.put('t', (var.get('e').get('source')+Js('|()')))
                var.put('r', (((Js('g')+(Js('i') if var.get('e').get('ignoreCase') else Js('')))+(Js('m') if var.get('e').get('multiline') else Js('')))+(Js('u') if var.get('e').get('unicode') else Js(''))))
                var.get('e').put('__matchAtRelocatable', var.get('RegExp').create(var.get('t'), var.get('r')))
            return var.get('e').get('__matchAtRelocatable')
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        @Js
        def PyJsHoisted_n_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 't'])
            if (var.get('e').get('global') or var.get('e').get('sticky')):
                PyJsTempException = JsToPyException(var.get('Error').create(Js('matchAt(...): Only non-global regexes are supported')))
                raise PyJsTempException
            var.put('n', var.get('a')(var.get('e')))
            var.get('n').put('lastIndex', var.get('r'))
            var.put('i', var.get('n').callprop('exec', var.get('t')))
            if (var.get('i').get((var.get('i').get('length')-Js(1.0)))==var.get(u"null")):
                var.get('i').put('length', (var.get('i').get('length')-Js(1.0)))
                return var.get('i')
            else:
                return var.get(u"null")
        PyJsHoisted_n_.func_name = 'n'
        var.put('n', PyJsHoisted_n_)
        Js('use strict')
        pass
        pass
        var.get('t').put('exports', var.get('n'))
    PyJs_anonymous_96_._set_name('anonymous')
    PyJs_Object_97_ = Js({})
    @Js
    def PyJs_anonymous_98_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            if (PyJsStrictEq(var.get('e'),var.get(u"null")) or PyJsStrictEq(var.get('e'),var.get('undefined'))):
                PyJsTempException = JsToPyException(var.get('TypeError').create(Js('Object.assign cannot be called with null or undefined')))
                raise PyJsTempException
            return var.get('Object')(var.get('e'))
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        @Js
        def PyJsHoisted_l_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            try:
                if var.get('Object').get('assign').neg():
                    return Js(False)
                var.put('e', var.get('String').create(Js('abc')))
                var.get('e').put('5', Js('de'))
                if PyJsStrictEq(var.get('Object').callprop('getOwnPropertyNames', var.get('e')).get('0'),Js('5')):
                    return Js(False)
                PyJs_Object_99_ = Js({})
                var.put('t', PyJs_Object_99_)
                #for JS loop
                var.put('r', Js(0.0))
                while (var.get('r')<Js(10.0)):
                    try:
                        var.get('t').put((Js('_')+var.get('String').callprop('fromCharCode', var.get('r'))), var.get('r'))
                    finally:
                            (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
                @Js
                def PyJs_anonymous_100_(e, this, arguments, var=var):
                    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                    var.registers(['e'])
                    return var.get('t').get(var.get('e'))
                PyJs_anonymous_100_._set_name('anonymous')
                var.put('a', var.get('Object').callprop('getOwnPropertyNames', var.get('t')).callprop('map', PyJs_anonymous_100_))
                if PyJsStrictNeq(var.get('a').callprop('join', Js('')),Js('0123456789')):
                    return Js(False)
                PyJs_Object_101_ = Js({})
                var.put('n', PyJs_Object_101_)
                @Js
                def PyJs_anonymous_102_(e, this, arguments, var=var):
                    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                    var.registers(['e'])
                    var.get('n').put(var.get('e'), var.get('e'))
                PyJs_anonymous_102_._set_name('anonymous')
                Js('abcdefghijklmnopqrst').callprop('split', Js('')).callprop('forEach', PyJs_anonymous_102_)
                PyJs_Object_103_ = Js({})
                if PyJsStrictNeq(var.get('Object').callprop('keys', var.get('Object').callprop('assign', PyJs_Object_103_, var.get('n'))).callprop('join', Js('')),Js('abcdefghijklmnopqrst')):
                    return Js(False)
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_65_7024415 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_65_7024415 is not None:
                        var.own['e'] = PyJsHolder_65_7024415
                    else:
                        del var.own['e']
                    del PyJsHolder_65_7024415
        PyJsHoisted_l_.func_name = 'l'
        var.put('l', PyJsHoisted_l_)
        Js('use strict')
        var.put('a', var.get('Object').get('prototype').get('hasOwnProperty'))
        var.put('n', var.get('Object').get('prototype').get('propertyIsEnumerable'))
        pass
        pass
        @Js
        def PyJs_anonymous_104_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'l', 'c', 'o', 'u', 's', 'e', 't'])
            pass
            var.put('l', var.get('i')(var.get('e')))
            pass
            #for JS loop
            var.put('o', Js(1.0))
            while (var.get('o')<var.get('arguments').get('length')):
                try:
                    var.put('r', var.get('Object')(var.get('arguments').get(var.get('o'))))
                    for PyJsTemp in var.get('r'):
                        var.put('u', PyJsTemp)
                        if var.get('a').callprop('call', var.get('r'), var.get('u')):
                            var.get('l').put(var.get('u'), var.get('r').get(var.get('u')))
                    if var.get('Object').get('getOwnPropertySymbols'):
                        var.put('s', var.get('Object').callprop('getOwnPropertySymbols', var.get('r')))
                        #for JS loop
                        var.put('c', Js(0.0))
                        while (var.get('c')<var.get('s').get('length')):
                            try:
                                if var.get('n').callprop('call', var.get('r'), var.get('s').get(var.get('c'))):
                                    var.get('l').put(var.get('s').get(var.get('c')), var.get('r').get(var.get('s').get(var.get('c'))))
                            finally:
                                    (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            return var.get('l')
        PyJs_anonymous_104_._set_name('anonymous')
        var.get('t').put('exports', (var.get('Object').get('assign') if var.get('l')() else PyJs_anonymous_104_))
    PyJs_anonymous_98_._set_name('anonymous')
    PyJs_Object_105_ = Js({})
    @Js
    def PyJs_anonymous_106_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_f_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_107_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_107_)
        PyJsHoisted_f_.func_name = 'f'
        var.put('f', PyJsHoisted_f_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('f')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('f')(var.get('i')))
        var.put('s', var.get('e')(Js('match-at')))
        var.put('o', var.get('f')(var.get('s')))
        var.put('u', var.get('e')(Js('./ParseError')))
        var.put('c', var.get('f')(var.get('u')))
        pass
        @Js
        def PyJs_anonymous_108_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, a, i, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'this':this, 'arguments':arguments}, var)
                var.registers(['i', 'r', 'a', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('text', var.get('t'))
                var.get(u"this").put('start', var.get('r'))
                var.get(u"this").put('end', var.get('a'))
                var.get(u"this").put('lexer', var.get('i'))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_t_110_(r, a, this, arguments, var=var):
                var = Scope({'r':r, 'a':a, 'this':this, 'arguments':arguments, 't':PyJs_t_110_}, var)
                var.registers(['r', 'a'])
                if PyJsStrictNeq(var.get('r').get('lexer'),var.get(u"this").get('lexer')):
                    return var.get('e').create(var.get('a'))
                return var.get('e').create(var.get('a'), var.get(u"this").get('start'), var.get('r').get('end'), var.get(u"this").get('lexer'))
            PyJs_t_110_._set_name('t')
            PyJs_Object_109_ = Js({'key':Js('range'),'value':PyJs_t_110_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_109_]))
            return var.get('e')
        PyJs_anonymous_108_._set_name('anonymous')
        var.put('h', PyJs_anonymous_108_())
        var.put('v', var.get('RegExp').create(((((Js('([ \r\n\t]+)|')+Js('([!-\\[\\]-‧\u202a-\ud7ff豈-\uffff]'))+Js('|[\ud800-\udbff][\udc00-\udfff]'))+Js('|\\\\(?:[a-zA-Z]+|[^\ud800-\udfff])'))+Js(')'))))
        @Js
        def PyJs_anonymous_111_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('input', var.get('t'))
                var.get(u"this").put('pos', Js(0.0))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_113_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_113_}, var)
                var.registers(['i', 'r', 'l', 'n', 'a', 't'])
                var.put('t', var.get(u"this").get('input'))
                var.put('r', var.get(u"this").get('pos'))
                if PyJsStrictEq(var.get('r'),var.get('t').get('length')):
                    return var.get('h').create(Js('EOF'), var.get('r'), var.get('r'), var.get(u"this"))
                var.put('a', PyJsComma(Js(0.0),var.get('o').get('default'))(var.get('v'), var.get('t'), var.get('r')))
                if PyJsStrictEq(var.get('a'),var.get(u"null")):
                    PyJsTempException = JsToPyException(var.get('c').get('default').create(((Js("Unexpected character: '")+var.get('t').get(var.get('r')))+Js("'")), var.get('h').create(var.get('t').get(var.get('r')), var.get('r'), (var.get('r')+Js(1.0)), var.get(u"this"))))
                    raise PyJsTempException
                var.put('n', (var.get('a').get('2') or Js(' ')))
                var.put('i', var.get(u"this").get('pos'))
                var.get(u"this").put('pos', var.get('a').get('0').get('length'), '+')
                var.put('l', var.get(u"this").get('pos'))
                return var.get('h').create(var.get('n'), var.get('i'), var.get('l'), var.get(u"this"))
            PyJs_e_113_._set_name('e')
            PyJs_Object_112_ = Js({'key':Js('lex'),'value':PyJs_e_113_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_112_]))
            return var.get('e')
        PyJs_anonymous_111_._set_name('anonymous')
        var.put('d', PyJs_anonymous_111_())
        var.get('t').put('exports', var.get('d'))
    PyJs_anonymous_106_._set_name('anonymous')
    PyJs_Object_114_ = Js({'./ParseError':Js(29.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0),'match-at':Js(24.0)})
    @Js
    def PyJs_anonymous_115_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_p_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_116_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_116_)
        PyJsHoisted_p_.func_name = 'p'
        var.put('p', PyJsHoisted_p_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('p')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('p')(var.get('i')))
        var.put('s', var.get('e')(Js('./Lexer')))
        var.put('o', var.get('p')(var.get('s')))
        var.put('u', var.get('e')(Js('./macros')))
        var.put('c', var.get('p')(var.get('u')))
        var.put('f', var.get('e')(Js('./ParseError')))
        var.put('h', var.get('p')(var.get('f')))
        var.put('v', var.get('e')(Js('object-assign')))
        var.put('d', var.get('p')(var.get('v')))
        pass
        @Js
        def PyJs_anonymous_117_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('lexer', var.get('o').get('default').create(var.get('t')))
                PyJs_Object_118_ = Js({})
                var.get(u"this").put('macros', PyJsComma(Js(0.0),var.get('d').get('default'))(PyJs_Object_118_, var.get('c').get('default'), var.get('r')))
                var.get(u"this").put('stack', Js([]))
                var.get(u"this").put('discardedWhiteSpace', Js([]))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_120_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_120_}, var)
                var.registers(['i', 'r', 'l', 'v', 'c', 'd', 'n', 'u', 's', 'a', 'f', 't'])
                #for JS loop
                
                while 1:
                    if PyJsStrictEq(var.get(u"this").get('stack').get('length'),Js(0.0)):
                        var.get(u"this").get('stack').callprop('push', var.get(u"this").get('lexer').callprop('lex'))
                    var.put('t', var.get(u"this").get('stack').callprop('pop'))
                    var.put('r', var.get('t').get('text'))
                    if (PyJsStrictEq(var.get('r').callprop('charAt', Js(0.0)),Js('\\')) and var.get(u"this").get('macros').callprop('hasOwnProperty', var.get('r'))).neg():
                        return var.get('t')
                    var.put('a', PyJsComma(Js(0.0), Js(None)))
                    var.put('n', var.get(u"this").get('macros').get(var.get('r')))
                    if PyJsStrictEq(var.get('n',throw=False).typeof(),Js('string')):
                        var.put('i', Js(0.0))
                        if PyJsStrictNeq(var.get('n').callprop('indexOf', Js('#')),(-Js(1.0))):
                            var.put('l', var.get('n').callprop('replace', JsRegExp('/##/g'), Js('')))
                            while PyJsStrictNeq(var.get('l').callprop('indexOf', (Js('#')+(var.get('i')+Js(1.0)))),(-Js(1.0))):
                                var.put('i',Js(var.get('i').to_number())+Js(1))
                        var.put('s', var.get('o').get('default').create(var.get('n')))
                        var.put('n', Js([]))
                        var.put('a', var.get('s').callprop('lex'))
                        while PyJsStrictNeq(var.get('a').get('text'),Js('EOF')):
                            var.get('n').callprop('push', var.get('a'))
                            var.put('a', var.get('s').callprop('lex'))
                        var.get('n').callprop('reverse')
                        var.get('n').put('numArgs', var.get('i'))
                        var.get(u"this").get('macros').put(var.get('r'), var.get('n'))
                    if var.get('n').get('numArgs'):
                        var.put('u', Js([]))
                        var.put('c', PyJsComma(Js(0.0), Js(None)))
                        #for JS loop
                        var.put('c', Js(0.0))
                        while (var.get('c')<var.get('n').get('numArgs')):
                            try:
                                var.put('f', var.get(u"this").callprop('get', Js(True)))
                                if PyJsStrictEq(var.get('f').get('text'),Js('{')):
                                    var.put('v', Js([]))
                                    var.put('d', Js(1.0))
                                    while PyJsStrictNeq(var.get('d'),Js(0.0)):
                                        var.put('a', var.get(u"this").callprop('get', Js(False)))
                                        var.get('v').callprop('push', var.get('a'))
                                        if PyJsStrictEq(var.get('a').get('text'),Js('{')):
                                            var.put('d',Js(var.get('d').to_number())+Js(1))
                                        else:
                                            if PyJsStrictEq(var.get('a').get('text'),Js('}')):
                                                var.put('d',Js(var.get('d').to_number())-Js(1))
                                            else:
                                                if PyJsStrictEq(var.get('a').get('text'),Js('EOF')):
                                                    PyJsTempException = JsToPyException(var.get('h').get('default').create(Js('End of input in macro argument'), var.get('f')))
                                                    raise PyJsTempException
                                    var.get('v').callprop('pop')
                                    var.get('v').callprop('reverse')
                                    var.get('u').put(var.get('c'), var.get('v'))
                                else:
                                    if PyJsStrictEq(var.get('f').get('text'),Js('EOF')):
                                        PyJsTempException = JsToPyException(var.get('h').get('default').create(Js('End of input expecting macro argument'), var.get('t')))
                                        raise PyJsTempException
                                    else:
                                        var.get('u').put(var.get('c'), Js([var.get('f')]))
                            finally:
                                    var.put('c',Js(var.get('c').to_number())+Js(1))
                        var.put('n', var.get('n').callprop('slice'))
                        #for JS loop
                        var.put('c', (var.get('n').get('length')-Js(1.0)))
                        while (var.get('c')>=Js(0.0)):
                            try:
                                var.put('a', var.get('n').get(var.get('c')))
                                if PyJsStrictEq(var.get('a').get('text'),Js('#')):
                                    if PyJsStrictEq(var.get('c'),Js(0.0)):
                                        PyJsTempException = JsToPyException(var.get('h').get('default').create(Js('Incomplete placeholder at end of macro body'), var.get('a')))
                                        raise PyJsTempException
                                    var.put('a', var.get('n').get(var.put('c',Js(var.get('c').to_number())-Js(1))))
                                    if PyJsStrictEq(var.get('a').get('text'),Js('#')):
                                        var.get('n').callprop('splice', (var.get('c')+Js(1.0)), Js(1.0))
                                    else:
                                        if JsRegExp('/^[1-9]$/').callprop('test', var.get('a').get('text')):
                                            var.get('n').get('splice').callprop('apply', var.get('n'), Js([var.get('c'), Js(2.0)]).callprop('concat', var.get('u').get((var.get('a').get('text')-Js(1.0)))))
                                        else:
                                            PyJsTempException = JsToPyException(var.get('h').get('default').create(Js('Not a valid argument number'), var.get('a')))
                                            raise PyJsTempException
                            finally:
                                    var.put('c',Js(var.get('c').to_number())-Js(1))
                    var.get(u"this").put('stack', var.get(u"this").get('stack').callprop('concat', var.get('n')))
                
            PyJs_e_120_._set_name('e')
            PyJs_Object_119_ = Js({'key':Js('nextToken'),'value':PyJs_e_120_})
            @Js
            def PyJs_e_122_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_122_}, var)
                var.registers(['r', 't'])
                var.get(u"this").put('discardedWhiteSpace', Js([]))
                var.put('r', var.get(u"this").callprop('nextToken'))
                if var.get('t'):
                    while PyJsStrictEq(var.get('r').get('text'),Js(' ')):
                        var.get(u"this").get('discardedWhiteSpace').callprop('push', var.get('r'))
                        var.put('r', var.get(u"this").callprop('nextToken'))
                return var.get('r')
            PyJs_e_122_._set_name('e')
            PyJs_Object_121_ = Js({'key':Js('get'),'value':PyJs_e_122_})
            @Js
            def PyJs_e_124_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_124_}, var)
                var.registers(['t'])
                var.get(u"this").get('stack').callprop('push', var.get('t'))
                while PyJsStrictNeq(var.get(u"this").get('discardedWhiteSpace').get('length'),Js(0.0)):
                    var.get(u"this").get('stack').callprop('push', var.get(u"this").get('discardedWhiteSpace').callprop('pop'))
            PyJs_e_124_._set_name('e')
            PyJs_Object_123_ = Js({'key':Js('unget'),'value':PyJs_e_124_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_119_, PyJs_Object_121_, PyJs_Object_123_]))
            return var.get('e')
        PyJs_anonymous_117_._set_name('anonymous')
        var.put('m', PyJs_anonymous_117_())
        var.get('t').put('exports', var.get('m'))
    PyJs_anonymous_115_._set_name('anonymous')
    PyJs_Object_125_ = Js({'./Lexer':Js(26.0),'./ParseError':Js(29.0),'./macros':Js(44.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0),'object-assign':Js(25.0)})
    @Js
    def PyJs_anonymous_126_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_u_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_127_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_127_)
        PyJsHoisted_u_.func_name = 'u'
        var.put('u', PyJsHoisted_u_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('u')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('u')(var.get('i')))
        var.put('s', var.get('e')(Js('./fontMetrics')))
        var.put('o', var.get('u')(var.get('s')))
        pass
        var.put('c', Js(6.0))
        var.put('f', Js([Js([Js(1.0), Js(1.0), Js(1.0)]), Js([Js(2.0), Js(1.0), Js(1.0)]), Js([Js(3.0), Js(1.0), Js(1.0)]), Js([Js(4.0), Js(2.0), Js(1.0)]), Js([Js(5.0), Js(2.0), Js(1.0)]), Js([Js(6.0), Js(3.0), Js(1.0)]), Js([Js(7.0), Js(4.0), Js(2.0)]), Js([Js(8.0), Js(6.0), Js(3.0)]), Js([Js(9.0), Js(7.0), Js(6.0)]), Js([Js(10.0), Js(8.0), Js(7.0)]), Js([Js(11.0), Js(10.0), Js(9.0)])]))
        var.put('h', Js([Js(0.5), Js(0.6), Js(0.7), Js(0.8), Js(0.9), Js(1.0), Js(1.2), Js(1.44), Js(1.728), Js(2.074), Js(2.488)]))
        @Js
        def PyJs_e_128_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_128_}, var)
            var.registers(['r', 't'])
            return (var.get('t') if (var.get('r').get('size')<Js(2.0)) else var.get('f').get((var.get('t')-Js(1.0))).get((var.get('r').get('size')-Js(1.0))))
        PyJs_e_128_._set_name('e')
        var.put('v', PyJs_e_128_)
        @Js
        def PyJs_anonymous_129_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('style', var.get('t').get('style'))
                var.get(u"this").put('color', var.get('t').get('color'))
                var.get(u"this").put('size', (var.get('t').get('size') or var.get('c')))
                var.get(u"this").put('textSize', (var.get('t').get('textSize') or var.get(u"this").get('size')))
                var.get(u"this").put('phantom', var.get('t').get('phantom'))
                var.get(u"this").put('font', var.get('t').get('font'))
                var.get(u"this").put('sizeMultiplier', var.get('h').get((var.get(u"this").get('size')-Js(1.0))))
                var.get(u"this").put('_fontMetrics', var.get(u"null"))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_t_131_(r, this, arguments, var=var):
                var = Scope({'r':r, 'this':this, 'arguments':arguments, 't':PyJs_t_131_}, var)
                var.registers(['a', 'n', 'r'])
                PyJs_Object_132_ = Js({'style':var.get(u"this").get('style'),'size':var.get(u"this").get('size'),'textSize':var.get(u"this").get('textSize'),'color':var.get(u"this").get('color'),'phantom':var.get(u"this").get('phantom'),'font':var.get(u"this").get('font')})
                var.put('a', PyJs_Object_132_)
                for PyJsTemp in var.get('r'):
                    var.put('n', PyJsTemp)
                    if var.get('r').callprop('hasOwnProperty', var.get('n')):
                        var.get('a').put(var.get('n'), var.get('r').get(var.get('n')))
                return var.get('e').create(var.get('a'))
            PyJs_t_131_._set_name('t')
            PyJs_Object_130_ = Js({'key':Js('extend'),'value':PyJs_t_131_})
            @Js
            def PyJs_e_134_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_134_}, var)
                var.registers(['t'])
                if PyJsStrictEq(var.get(u"this").get('style'),var.get('t')):
                    return var.get(u"this")
                else:
                    PyJs_Object_135_ = Js({'style':var.get('t'),'size':var.get('v')(var.get(u"this").get('textSize'), var.get('t'))})
                    return var.get(u"this").callprop('extend', PyJs_Object_135_)
            PyJs_e_134_._set_name('e')
            PyJs_Object_133_ = Js({'key':Js('havingStyle'),'value':PyJs_e_134_})
            @Js
            def PyJs_e_137_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_137_}, var)
                var.registers([])
                return var.get(u"this").callprop('havingStyle', var.get(u"this").get('style').callprop('cramp'))
            PyJs_e_137_._set_name('e')
            PyJs_Object_136_ = Js({'key':Js('havingCrampedStyle'),'value':PyJs_e_137_})
            @Js
            def PyJs_e_139_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_139_}, var)
                var.registers(['t'])
                if (PyJsStrictEq(var.get(u"this").get('size'),var.get('t')) and PyJsStrictEq(var.get(u"this").get('textSize'),var.get('t'))):
                    return var.get(u"this")
                else:
                    PyJs_Object_140_ = Js({'style':var.get(u"this").get('style').callprop('text'),'size':var.get('t'),'textSize':var.get('t')})
                    return var.get(u"this").callprop('extend', PyJs_Object_140_)
            PyJs_e_139_._set_name('e')
            PyJs_Object_138_ = Js({'key':Js('havingSize'),'value':PyJs_e_139_})
            @Js
            def PyJs_e_142_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_142_}, var)
                var.registers(['r', 't'])
                var.put('t', (var.get('t') or var.get(u"this").get('style').callprop('text')))
                var.put('r', var.get('v')(var.get('c'), var.get('t')))
                if ((PyJsStrictEq(var.get(u"this").get('size'),var.get('r')) and PyJsStrictEq(var.get(u"this").get('textSize'),var.get('c'))) and PyJsStrictEq(var.get(u"this").get('style'),var.get('t'))):
                    return var.get(u"this")
                else:
                    PyJs_Object_143_ = Js({'style':var.get('t'),'size':var.get('r'),'baseSize':var.get('c')})
                    return var.get(u"this").callprop('extend', PyJs_Object_143_)
            PyJs_e_142_._set_name('e')
            PyJs_Object_141_ = Js({'key':Js('havingBaseStyle'),'value':PyJs_e_142_})
            @Js
            def PyJs_e_145_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_145_}, var)
                var.registers(['t'])
                PyJs_Object_146_ = Js({'color':var.get('t')})
                return var.get(u"this").callprop('extend', PyJs_Object_146_)
            PyJs_e_145_._set_name('e')
            PyJs_Object_144_ = Js({'key':Js('withColor'),'value':PyJs_e_145_})
            @Js
            def PyJs_e_148_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_148_}, var)
                var.registers([])
                PyJs_Object_149_ = Js({'phantom':Js(True)})
                return var.get(u"this").callprop('extend', PyJs_Object_149_)
            PyJs_e_148_._set_name('e')
            PyJs_Object_147_ = Js({'key':Js('withPhantom'),'value':PyJs_e_148_})
            @Js
            def PyJs_e_151_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_151_}, var)
                var.registers(['t'])
                PyJs_Object_152_ = Js({'font':(var.get('t') or var.get(u"this").get('font'))})
                return var.get(u"this").callprop('extend', PyJs_Object_152_)
            PyJs_e_151_._set_name('e')
            PyJs_Object_150_ = Js({'key':Js('withFont'),'value':PyJs_e_151_})
            @Js
            def PyJs_e_154_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_154_}, var)
                var.registers(['t'])
                if PyJsStrictNeq(var.get('t').get('size'),var.get(u"this").get('size')):
                    return Js([Js('sizing'), (Js('reset-size')+var.get('t').get('size')), (Js('size')+var.get(u"this").get('size'))])
                else:
                    return Js([])
            PyJs_e_154_._set_name('e')
            PyJs_Object_153_ = Js({'key':Js('sizingClasses'),'value':PyJs_e_154_})
            @Js
            def PyJs_e_156_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_156_}, var)
                var.registers([])
                if PyJsStrictNeq(var.get(u"this").get('size'),var.get('c')):
                    return Js([Js('sizing'), (Js('reset-size')+var.get(u"this").get('size')), (Js('size')+var.get('c'))])
                else:
                    return Js([])
            PyJs_e_156_._set_name('e')
            PyJs_Object_155_ = Js({'key':Js('baseSizingClasses'),'value':PyJs_e_156_})
            @Js
            def PyJs_e_158_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_158_}, var)
                var.registers([])
                if var.get(u"this").get('_fontMetrics').neg():
                    var.get(u"this").put('_fontMetrics', var.get('o').get('default').callprop('getFontMetrics', var.get(u"this").get('size')))
                return var.get(u"this").get('_fontMetrics')
            PyJs_e_158_._set_name('e')
            PyJs_Object_157_ = Js({'key':Js('fontMetrics'),'value':PyJs_e_158_})
            @Js
            def PyJs_t_160_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 't':PyJs_t_160_}, var)
                var.registers([])
                if var.get(u"this").get('phantom'):
                    return Js('transparent')
                else:
                    return (var.get('e').get('colorMap').get(var.get(u"this").get('color')) or var.get(u"this").get('color'))
            PyJs_t_160_._set_name('t')
            PyJs_Object_159_ = Js({'key':Js('getColor'),'value':PyJs_t_160_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_130_, PyJs_Object_133_, PyJs_Object_136_, PyJs_Object_138_, PyJs_Object_141_, PyJs_Object_144_, PyJs_Object_147_, PyJs_Object_150_, PyJs_Object_153_, PyJs_Object_155_, PyJs_Object_157_, PyJs_Object_159_]))
            return var.get('e')
        PyJs_anonymous_129_._set_name('anonymous')
        var.put('d', PyJs_anonymous_129_())
        PyJs_Object_161_ = Js({'katex-blue':Js('#6495ed'),'katex-orange':Js('#ffa500'),'katex-pink':Js('#ff00af'),'katex-red':Js('#df0030'),'katex-green':Js('#28ae7b'),'katex-gray':Js('gray'),'katex-purple':Js('#9d38bd'),'katex-blueA':Js('#ccfaff'),'katex-blueB':Js('#80f6ff'),'katex-blueC':Js('#63d9ea'),'katex-blueD':Js('#11accd'),'katex-blueE':Js('#0c7f99'),'katex-tealA':Js('#94fff5'),'katex-tealB':Js('#26edd5'),'katex-tealC':Js('#01d1c1'),'katex-tealD':Js('#01a995'),'katex-tealE':Js('#208170'),'katex-greenA':Js('#b6ffb0'),'katex-greenB':Js('#8af281'),'katex-greenC':Js('#74cf70'),'katex-greenD':Js('#1fab54'),'katex-greenE':Js('#0d923f'),'katex-goldA':Js('#ffd0a9'),'katex-goldB':Js('#ffbb71'),'katex-goldC':Js('#ff9c39'),'katex-goldD':Js('#e07d10'),'katex-goldE':Js('#a75a05'),'katex-redA':Js('#fca9a9'),'katex-redB':Js('#ff8482'),'katex-redC':Js('#f9685d'),'katex-redD':Js('#e84d39'),'katex-redE':Js('#bc2612'),'katex-maroonA':Js('#ffbde0'),'katex-maroonB':Js('#ff92c6'),'katex-maroonC':Js('#ed5fa6'),'katex-maroonD':Js('#ca337c'),'katex-maroonE':Js('#9e034e'),'katex-purpleA':Js('#ddd7ff'),'katex-purpleB':Js('#c6b9fc'),'katex-purpleC':Js('#aa87ff'),'katex-purpleD':Js('#7854ab'),'katex-purpleE':Js('#543b78'),'katex-mintA':Js('#f5f9e8'),'katex-mintB':Js('#edf2df'),'katex-mintC':Js('#e0e5cc'),'katex-grayA':Js('#f6f7f7'),'katex-grayB':Js('#f0f1f2'),'katex-grayC':Js('#e3e5e6'),'katex-grayD':Js('#d6d8da'),'katex-grayE':Js('#babec2'),'katex-grayF':Js('#888d93'),'katex-grayG':Js('#626569'),'katex-grayH':Js('#3b3e40'),'katex-grayI':Js('#21242c'),'katex-kaBlue':Js('#314453'),'katex-kaGreen':Js('#71B307')})
        var.get('d').put('colorMap', PyJs_Object_161_)
        var.get('d').put('BASESIZE', var.get('c'))
        var.get('t').put('exports', var.get('d'))
    PyJs_anonymous_126_._set_name('anonymous')
    PyJs_Object_162_ = Js({'./fontMetrics':Js(41.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0)})
    @Js
    def PyJs_anonymous_163_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_164_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_164_)
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('i')(var.get('a')))
        pass
        @Js
        def PyJs_e_165_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_165_}, var)
            var.registers(['i', 'l', 'r', 'c', 'o', 'u', 's', 'a', 'f', 't'])
            PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
            var.put('a', (Js('KaTeX parse error: ')+var.get('t')))
            var.put('i', PyJsComma(Js(0.0), Js(None)))
            var.put('l', PyJsComma(Js(0.0), Js(None)))
            if ((var.get('r') and var.get('r').get('lexer')) and (var.get('r').get('start')<=var.get('r').get('end'))):
                var.put('s', var.get('r').get('lexer').get('input'))
                var.put('i', var.get('r').get('start'))
                var.put('l', var.get('r').get('end'))
                if PyJsStrictEq(var.get('i'),var.get('s').get('length')):
                    var.put('a', Js(' at end of input: '), '+')
                else:
                    var.put('a', ((Js(' at position ')+(var.get('i')+Js(1.0)))+Js(': ')), '+')
                var.put('o', var.get('s').callprop('slice', var.get('i'), var.get('l')).callprop('replace', JsRegExp('/[^]/g'), Js('$&̲')))
                var.put('u', PyJsComma(Js(0.0), Js(None)))
                if (var.get('i')>Js(15.0)):
                    var.put('u', (Js('…')+var.get('s').callprop('slice', (var.get('i')-Js(15.0)), var.get('i'))))
                else:
                    var.put('u', var.get('s').callprop('slice', Js(0.0), var.get('i')))
                var.put('c', PyJsComma(Js(0.0), Js(None)))
                if ((var.get('l')+Js(15.0))<var.get('s').get('length')):
                    var.put('c', (var.get('s').callprop('slice', var.get('l'), (var.get('l')+Js(15.0)))+Js('…')))
                else:
                    var.put('c', var.get('s').callprop('slice', var.get('l')))
                var.put('a', ((var.get('u')+var.get('o'))+var.get('c')), '+')
            var.put('f', var.get('Error').create(var.get('a')))
            var.get('f').put('name', Js('ParseError'))
            var.get('f').put('__proto__', var.get('e').get('prototype'))
            var.get('f').put('position', var.get('i'))
            return var.get('f')
        PyJs_e_165_._set_name('e')
        var.put('l', PyJs_e_165_)
        var.get('l').get('prototype').put('__proto__', var.get('Error').get('prototype'))
        var.get('t').put('exports', var.get('l'))
    PyJs_anonymous_163_._set_name('anonymous')
    PyJs_Object_166_ = Js({'babel-runtime/helpers/classCallCheck':Js(4.0)})
    @Js
    def PyJs_anonymous_167_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_169_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_169_)
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        Js('use strict')
        PyJs_Object_168_ = Js({'value':Js(True)})
        var.get('Object').callprop('defineProperty', var.get('r'), Js('__esModule'), PyJs_Object_168_)
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('i')(var.get('a')))
        pass
        @Js
        def PyJs_e_170_(t, r, a, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_170_}, var)
            var.registers(['i', 'r', 'l', 'a', 't'])
            PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
            var.get(u"this").put('type', var.get('t'))
            var.get(u"this").put('value', var.get('r'))
            var.get(u"this").put('mode', var.get('a'))
            if (var.get('i') and (var.get('l').neg() or PyJsStrictEq(var.get('l').get('lexer'),var.get('i').get('lexer')))):
                var.get(u"this").put('lexer', var.get('i').get('lexer'))
                var.get(u"this").put('start', var.get('i').get('start'))
                var.get(u"this").put('end', (var.get('l') or var.get('i')).get('end'))
        PyJs_e_170_._set_name('e')
        var.put('l', PyJs_e_170_)
        var.get('r').put('default', var.get('l'))
    PyJs_anonymous_167_._set_name('anonymous')
    PyJs_Object_171_ = Js({'babel-runtime/helpers/classCallCheck':Js(4.0)})
    @Js
    def PyJs_anonymous_172_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'b', 'l', 'c', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_z_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_173_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_173_)
        PyJsHoisted_z_.func_name = 'z'
        var.put('z', PyJsHoisted_z_)
        @Js
        def PyJsHoisted_S_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.get(u"this").put('result', var.get('e'))
            var.get(u"this").put('isFunction', var.get('t'))
            var.get(u"this").put('token', var.get('r'))
        PyJsHoisted_S_.func_name = 'S'
        var.put('S', PyJsHoisted_S_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('z')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('z')(var.get('i')))
        var.put('s', var.get('e')(Js('./functions')))
        var.put('o', var.get('z')(var.get('s')))
        var.put('u', var.get('e')(Js('./environments')))
        var.put('c', var.get('z')(var.get('u')))
        var.put('f', var.get('e')(Js('./MacroExpander')))
        var.put('h', var.get('z')(var.get('f')))
        var.put('v', var.get('e')(Js('./symbols')))
        var.put('d', var.get('z')(var.get('v')))
        var.put('p', var.get('e')(Js('./utils')))
        var.put('m', var.get('z')(var.get('p')))
        var.put('g', var.get('e')(Js('./units')))
        var.put('y', var.get('z')(var.get('g')))
        var.put('x', var.get('e')(Js('./unicodeRegexes')))
        var.put('w', var.get('e')(Js('./ParseNode')))
        var.put('b', var.get('z')(var.get('w')))
        var.put('k', var.get('e')(Js('./ParseError')))
        var.put('M', var.get('z')(var.get('k')))
        pass
        pass
        @Js
        def PyJs_anonymous_174_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('gullet', var.get('h').get('default').create(var.get('t'), var.get('r').get('macros')))
                if var.get('r').get('colorIsTextColor'):
                    var.get(u"this").get('gullet').get('macros').put('\\color', Js('\\textcolor'))
                var.get(u"this").put('settings', var.get('r'))
                var.get(u"this").put('leftrightDepth', Js(0.0))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            def PyJs_LONG_234_(var=var):
                @Js
                def PyJs_e_176_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_176_}, var)
                    var.registers(['r', 't'])
                    if PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),var.get('t')):
                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((((Js("Expected '")+var.get('t'))+Js("', got '"))+var.get(u"this").get('nextToken').get('text'))+Js("'")), var.get(u"this").get('nextToken')))
                        raise PyJsTempException
                    if PyJsStrictNeq(var.get('r'),Js(False)):
                        var.get(u"this").callprop('consume')
                PyJs_e_176_._set_name('e')
                PyJs_Object_175_ = Js({'key':Js('expect'),'value':PyJs_e_176_})
                @Js
                def PyJs_e_178_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_178_}, var)
                    var.registers([])
                    var.get(u"this").put('nextToken', var.get(u"this").get('gullet').callprop('get', PyJsStrictEq(var.get(u"this").get('mode'),Js('math'))))
                PyJs_e_178_._set_name('e')
                PyJs_Object_177_ = Js({'key':Js('consume'),'value':PyJs_e_178_})
                @Js
                def PyJs_e_180_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_180_}, var)
                    var.registers(['t'])
                    var.get(u"this").get('gullet').callprop('unget', var.get(u"this").get('nextToken'))
                    var.get(u"this").put('mode', var.get('t'))
                    var.get(u"this").callprop('consume')
                PyJs_e_180_._set_name('e')
                PyJs_Object_179_ = Js({'key':Js('switchMode'),'value':PyJs_e_180_})
                @Js
                def PyJs_e_182_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_182_}, var)
                    var.registers(['e'])
                    var.get(u"this").put('mode', Js('math'))
                    var.get(u"this").callprop('consume')
                    var.put('e', var.get(u"this").callprop('parseInput'))
                    return var.get('e')
                PyJs_e_182_._set_name('e')
                PyJs_Object_181_ = Js({'key':Js('parse'),'value':PyJs_e_182_})
                @Js
                def PyJs_e_184_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_184_}, var)
                    var.registers(['t'])
                    var.put('t', var.get(u"this").callprop('parseExpression', Js(False)))
                    var.get(u"this").callprop('expect', Js('EOF'), Js(False))
                    return var.get('t')
                PyJs_e_184_._set_name('e')
                PyJs_Object_183_ = Js({'key':Js('parseInput'),'value':PyJs_e_184_})
                @Js
                def PyJs_t_186_(r, a, this, arguments, var=var):
                    var = Scope({'r':r, 'a':a, 'this':this, 'arguments':arguments, 't':PyJs_t_186_}, var)
                    var.registers(['i', 'r', 'l', 'n', 's', 'a'])
                    var.put('n', Js([]))
                    while Js(True):
                        var.put('i', var.get(u"this").get('nextToken'))
                        if PyJsStrictNeq(var.get('e').get('endOfExpression').callprop('indexOf', var.get('i').get('text')),(-Js(1.0))):
                            break
                        if (var.get('a') and PyJsStrictEq(var.get('i').get('text'),var.get('a'))):
                            break
                        if ((var.get('r') and var.get('o').get('default').get(var.get('i').get('text'))) and var.get('o').get('default').get(var.get('i').get('text')).get('infix')):
                            break
                        var.put('l', var.get(u"this").callprop('parseAtom'))
                        if var.get('l').neg():
                            if (var.get(u"this").get('settings').get('throwOnError').neg() and PyJsStrictEq(var.get('i').get('text').get('0'),Js('\\'))):
                                var.put('s', var.get(u"this").callprop('handleUnsupportedCmd'))
                                var.get('n').callprop('push', var.get('s'))
                                continue
                            break
                        var.get('n').callprop('push', var.get('l'))
                    return var.get(u"this").callprop('handleInfixNodes', var.get('n'))
                PyJs_t_186_._set_name('t')
                PyJs_Object_185_ = Js({'key':Js('parseExpression'),'value':PyJs_t_186_})
                @Js
                def PyJs_e_188_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_188_}, var)
                    var.registers(['i', 'l', 'r', 'c', 'o', 'n', 'u', 's', 'a', 't'])
                    var.put('r', (-Js(1.0)))
                    var.put('a', PyJsComma(Js(0.0), Js(None)))
                    #for JS loop
                    var.put('n', Js(0.0))
                    while (var.get('n')<var.get('t').get('length')):
                        try:
                            var.put('i', var.get('t').get(var.get('n')))
                            if PyJsStrictEq(var.get('i').get('type'),Js('infix')):
                                if PyJsStrictNeq(var.get('r'),(-Js(1.0))):
                                    PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('only one infix operator per group'), var.get('i').get('value').get('token')))
                                    raise PyJsTempException
                                var.put('r', var.get('n'))
                                var.put('a', var.get('i').get('value').get('replaceWith'))
                        finally:
                                (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
                    if PyJsStrictNeq(var.get('r'),(-Js(1.0))):
                        var.put('l', PyJsComma(Js(0.0), Js(None)))
                        var.put('s', PyJsComma(Js(0.0), Js(None)))
                        var.put('o', var.get('t').callprop('slice', Js(0.0), var.get('r')))
                        var.put('u', var.get('t').callprop('slice', (var.get('r')+Js(1.0))))
                        if (PyJsStrictEq(var.get('o').get('length'),Js(1.0)) and PyJsStrictEq(var.get('o').get('0').get('type'),Js('ordgroup'))):
                            var.put('l', var.get('o').get('0'))
                        else:
                            var.put('l', var.get('b').get('default').create(Js('ordgroup'), var.get('o'), var.get(u"this").get('mode')))
                        if (PyJsStrictEq(var.get('u').get('length'),Js(1.0)) and PyJsStrictEq(var.get('u').get('0').get('type'),Js('ordgroup'))):
                            var.put('s', var.get('u').get('0'))
                        else:
                            var.put('s', var.get('b').get('default').create(Js('ordgroup'), var.get('u'), var.get(u"this").get('mode')))
                        var.put('c', var.get(u"this").callprop('callFunction', var.get('a'), Js([var.get('l'), var.get('s')]), var.get(u"null")))
                        return Js([var.get('b').get('default').create(var.get('c').get('type'), var.get('c'), var.get(u"this").get('mode'))])
                    else:
                        return var.get('t')
                PyJs_e_188_._set_name('e')
                PyJs_Object_187_ = Js({'key':Js('handleInfixNodes'),'value':PyJs_e_188_})
                @Js
                def PyJs_t_190_(r, this, arguments, var=var):
                    var = Scope({'r':r, 'this':this, 'arguments':arguments, 't':PyJs_t_190_}, var)
                    var.registers(['i', 'r', 'l', 'n', 'a'])
                    var.put('a', var.get(u"this").get('nextToken'))
                    var.put('n', var.get('a').get('text'))
                    var.get(u"this").callprop('consume')
                    var.put('i', var.get(u"this").callprop('parseGroup'))
                    if var.get('i').neg():
                        if (var.get(u"this").get('settings').get('throwOnError').neg() and PyJsStrictEq(var.get(u"this").get('nextToken').get('text').get('0'),Js('\\'))):
                            return var.get(u"this").callprop('handleUnsupportedCmd')
                        else:
                            PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Expected group after '")+var.get('n'))+Js("'")), var.get('a')))
                            raise PyJsTempException
                    else:
                        if var.get('i').get('isFunction'):
                            var.put('l', var.get('o').get('default').get(var.get('i').get('result')).get('greediness'))
                            if (var.get('l')>var.get('e').get('SUPSUB_GREEDINESS')):
                                return var.get(u"this").callprop('parseFunction', var.get('i'))
                            else:
                                PyJsTempException = JsToPyException(var.get('M').get('default').create(((((Js("Got function '")+var.get('i').get('result'))+Js("' with no arguments "))+Js('as '))+var.get('r')), var.get('a')))
                                raise PyJsTempException
                        else:
                            return var.get('i').get('result')
                PyJs_t_190_._set_name('t')
                PyJs_Object_189_ = Js({'key':Js('handleSupSubscript'),'value':PyJs_t_190_})
                @Js
                def PyJs_e_192_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_192_}, var)
                    var.registers(['i', 'r', 'n', 'a', 't'])
                    var.put('t', var.get(u"this").get('nextToken').get('text'))
                    var.put('r', Js([]))
                    #for JS loop
                    var.put('a', Js(0.0))
                    while (var.get('a')<var.get('t').get('length')):
                        try:
                            var.get('r').callprop('push', var.get('b').get('default').create(Js('textord'), var.get('t').get(var.get('a')), Js('text')))
                        finally:
                                (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
                    PyJs_Object_193_ = Js({'body':var.get('r'),'type':Js('text')})
                    var.put('n', var.get('b').get('default').create(Js('text'), PyJs_Object_193_, var.get(u"this").get('mode')))
                    PyJs_Object_194_ = Js({'color':var.get(u"this").get('settings').get('errorColor'),'value':Js([var.get('n')]),'type':Js('color')})
                    var.put('i', var.get('b').get('default').create(Js('color'), PyJs_Object_194_, var.get(u"this").get('mode')))
                    var.get(u"this").callprop('consume')
                    return var.get('i')
                PyJs_e_192_._set_name('e')
                PyJs_Object_191_ = Js({'key':Js('handleUnsupportedCmd'),'value':PyJs_e_192_})
                @Js
                def PyJs_e_196_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_196_}, var)
                    var.registers(['i', 'r', 'l', 'n', 's', 'a', 't'])
                    var.put('t', var.get(u"this").callprop('parseImplicitGroup'))
                    if PyJsStrictEq(var.get(u"this").get('mode'),Js('text')):
                        return var.get('t')
                    var.put('r', PyJsComma(Js(0.0), Js(None)))
                    var.put('a', PyJsComma(Js(0.0), Js(None)))
                    while Js(True):
                        var.put('n', var.get(u"this").get('nextToken'))
                        if (PyJsStrictEq(var.get('n').get('text'),Js('\\limits')) or PyJsStrictEq(var.get('n').get('text'),Js('\\nolimits'))):
                            if (var.get('t').neg() or PyJsStrictNeq(var.get('t').get('type'),Js('op'))):
                                PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('Limit controls must follow a math operator'), var.get('n')))
                                raise PyJsTempException
                            else:
                                var.put('i', PyJsStrictEq(var.get('n').get('text'),Js('\\limits')))
                                var.get('t').get('value').put('limits', var.get('i'))
                                var.get('t').get('value').put('alwaysHandleSupSub', Js(True))
                            var.get(u"this").callprop('consume')
                        else:
                            if PyJsStrictEq(var.get('n').get('text'),Js('^')):
                                if var.get('r'):
                                    PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('Double superscript'), var.get('n')))
                                    raise PyJsTempException
                                var.put('r', var.get(u"this").callprop('handleSupSubscript', Js('superscript')))
                            else:
                                if PyJsStrictEq(var.get('n').get('text'),Js('_')):
                                    if var.get('a'):
                                        PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('Double subscript'), var.get('n')))
                                        raise PyJsTempException
                                    var.put('a', var.get(u"this").callprop('handleSupSubscript', Js('subscript')))
                                else:
                                    if PyJsStrictEq(var.get('n').get('text'),Js("'")):
                                        if var.get('r'):
                                            PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('Double superscript'), var.get('n')))
                                            raise PyJsTempException
                                        var.put('l', var.get('b').get('default').create(Js('textord'), Js('\\prime'), var.get(u"this").get('mode')))
                                        var.put('s', Js([var.get('l')]))
                                        var.get(u"this").callprop('consume')
                                        while PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js("'")):
                                            var.get('s').callprop('push', var.get('l'))
                                            var.get(u"this").callprop('consume')
                                        if PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js('^')):
                                            var.get('s').callprop('push', var.get(u"this").callprop('handleSupSubscript', Js('superscript')))
                                        var.put('r', var.get('b').get('default').create(Js('ordgroup'), var.get('s'), var.get(u"this").get('mode')))
                                    else:
                                        break
                    if (var.get('r') or var.get('a')):
                        PyJs_Object_197_ = Js({'base':var.get('t'),'sup':var.get('r'),'sub':var.get('a')})
                        return var.get('b').get('default').create(Js('supsub'), PyJs_Object_197_, var.get(u"this").get('mode'))
                    else:
                        return var.get('t')
                PyJs_e_196_._set_name('e')
                PyJs_Object_195_ = Js({'key':Js('parseAtom'),'value':PyJs_e_196_})
                @Js
                def PyJs_t_199_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 't':PyJs_t_199_}, var)
                    var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'w', 'x', 'a', 'A', 'S', 'l', 'g', 'z', 'u', 'k', 'p', 'd', 'n', 's', 'f'])
                    var.put('r', var.get(u"this").callprop('parseSymbol'))
                    if (var.get('r')==var.get(u"null")):
                        return var.get(u"this").callprop('parseFunction')
                    var.put('a', var.get('r').get('result'))
                    if PyJsStrictEq(var.get('a'),Js('\\left')):
                        var.put('n', var.get(u"this").callprop('parseFunction', var.get('r')))
                        var.get(u"this").put('leftrightDepth',Js(var.get(u"this").get('leftrightDepth').to_number())+Js(1))
                        var.put('i', var.get(u"this").callprop('parseExpression', Js(False)))
                        var.get(u"this").put('leftrightDepth',Js(var.get(u"this").get('leftrightDepth').to_number())-Js(1))
                        var.get(u"this").callprop('expect', Js('\\right'), Js(False))
                        var.put('l', var.get(u"this").callprop('parseFunction'))
                        PyJs_Object_200_ = Js({'body':var.get('i'),'left':var.get('n').get('value').get('value'),'right':var.get('l').get('value').get('value')})
                        return var.get('b').get('default').create(Js('leftright'), PyJs_Object_200_, var.get(u"this").get('mode'))
                    else:
                        if PyJsStrictEq(var.get('a'),Js('\\begin')):
                            var.put('s', var.get(u"this").callprop('parseFunction', var.get('r')))
                            var.put('o', var.get('s').get('value').get('name'))
                            if var.get('c').get('default').callprop('hasOwnProperty', var.get('o')).neg():
                                PyJsTempException = JsToPyException(var.get('M').get('default').create((Js('No such environment: ')+var.get('o')), var.get('s').get('value').get('nameGroup')))
                                raise PyJsTempException
                            var.put('u', var.get('c').get('default').get(var.get('o')))
                            var.put('f', var.get(u"this").callprop('parseArguments', ((Js('\\begin{')+var.get('o'))+Js('}')), var.get('u')))
                            PyJs_Object_201_ = Js({'mode':var.get(u"this").get('mode'),'envName':var.get('o'),'parser':var.get(u"this"),'positions':var.get('f').callprop('pop')})
                            var.put('h', PyJs_Object_201_)
                            var.put('v', var.get('u').callprop('handler', var.get('h'), var.get('f')))
                            var.get(u"this").callprop('expect', Js('\\end'), Js(False))
                            var.put('d', var.get(u"this").get('nextToken'))
                            var.put('p', var.get(u"this").callprop('parseFunction'))
                            if PyJsStrictNeq(var.get('p').get('value').get('name'),var.get('o')):
                                PyJsTempException = JsToPyException(var.get('M').get('default').create((((((Js('Mismatch: \\begin{')+var.get('o'))+Js('} matched '))+Js('by \\end{'))+var.get('p').get('value').get('name'))+Js('}')), var.get('d')))
                                raise PyJsTempException
                            var.get('v').put('position', var.get('p').get('position'))
                            return var.get('v')
                        else:
                            if var.get('m').get('default').callprop('contains', var.get('e').get('sizeFuncs'), var.get('a')):
                                var.get(u"this").callprop('consumeSpaces')
                                var.put('g', var.get(u"this").callprop('parseExpression', Js(False)))
                                PyJs_Object_202_ = Js({'size':(var.get('m').get('default').callprop('indexOf', var.get('e').get('sizeFuncs'), var.get('a'))+Js(1.0)),'value':var.get('g')})
                                return var.get('b').get('default').create(Js('sizing'), PyJs_Object_202_, var.get(u"this").get('mode'))
                            else:
                                if var.get('m').get('default').callprop('contains', var.get('e').get('styleFuncs'), var.get('a')):
                                    var.get(u"this").callprop('consumeSpaces')
                                    var.put('y', var.get(u"this").callprop('parseExpression', Js(True)))
                                    PyJs_Object_203_ = Js({'style':var.get('a').callprop('slice', Js(1.0), (var.get('a').get('length')-Js(5.0))),'value':var.get('y')})
                                    return var.get('b').get('default').create(Js('styling'), PyJs_Object_203_, var.get(u"this").get('mode'))
                                else:
                                    if var.get('e').get('oldFontFuncs').contains(var.get('a')):
                                        var.put('x', var.get('e').get('oldFontFuncs').get(var.get('a')))
                                        var.get(u"this").callprop('consumeSpaces')
                                        var.put('w', var.get(u"this").callprop('parseExpression', Js(True)))
                                        if PyJsStrictEq(var.get('x').callprop('slice', Js(0.0), Js(4.0)),Js('text')):
                                            PyJs_Object_204_ = Js({'style':var.get('x'),'body':var.get('b').get('default').create(Js('ordgroup'), var.get('w'), var.get(u"this").get('mode'))})
                                            return var.get('b').get('default').create(Js('text'), PyJs_Object_204_, var.get(u"this").get('mode'))
                                        else:
                                            PyJs_Object_205_ = Js({'font':var.get('x'),'body':var.get('b').get('default').create(Js('ordgroup'), var.get('w'), var.get(u"this").get('mode'))})
                                            return var.get('b').get('default').create(Js('font'), PyJs_Object_205_, var.get(u"this").get('mode'))
                                    else:
                                        if PyJsStrictEq(var.get('a'),Js('\\color')):
                                            var.put('k', var.get(u"this").callprop('parseColorGroup', Js(False)))
                                            if var.get('k').neg():
                                                PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('\\color not followed by color')))
                                                raise PyJsTempException
                                            var.put('z', var.get(u"this").callprop('parseExpression', Js(True)))
                                            PyJs_Object_206_ = Js({'type':Js('color'),'color':var.get('k').get('result').get('value'),'value':var.get('z')})
                                            return var.get('b').get('default').create(Js('color'), PyJs_Object_206_, var.get(u"this").get('mode'))
                                        else:
                                            if PyJsStrictEq(var.get('a'),Js('$')):
                                                if PyJsStrictEq(var.get(u"this").get('mode'),Js('math')):
                                                    PyJsTempException = JsToPyException(var.get('M').get('default').create(Js('$ within math mode')))
                                                    raise PyJsTempException
                                                var.get(u"this").callprop('consume')
                                                var.put('S', var.get(u"this").get('mode'))
                                                var.get(u"this").callprop('switchMode', Js('math'))
                                                var.put('A', var.get(u"this").callprop('parseExpression', Js(False), Js('$')))
                                                var.get(u"this").callprop('expect', Js('$'), Js(True))
                                                var.get(u"this").callprop('switchMode', var.get('S'))
                                                PyJs_Object_207_ = Js({'style':Js('text'),'value':var.get('A')})
                                                return var.get('b').get('default').create(Js('styling'), PyJs_Object_207_, Js('math'))
                                            else:
                                                return var.get(u"this").callprop('parseFunction', var.get('r'))
                PyJs_t_199_._set_name('t')
                PyJs_Object_198_ = Js({'key':Js('parseImplicitGroup'),'value':PyJs_t_199_})
                @Js
                def PyJs_e_209_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_209_}, var)
                    var.registers(['i', 'l', 'r', 'n', 'a', 't'])
                    if var.get('t').neg():
                        var.put('t', var.get(u"this").callprop('parseGroup'))
                    if var.get('t'):
                        if var.get('t').get('isFunction'):
                            var.put('r', var.get('t').get('result'))
                            var.put('a', var.get('o').get('default').get(var.get('r')))
                            if (PyJsStrictEq(var.get(u"this").get('mode'),Js('text')) and var.get('a').get('allowedInText').neg()):
                                PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Can't use function '")+var.get('r'))+Js("' in text mode")), var.get('t').get('token')))
                                raise PyJsTempException
                            else:
                                if (PyJsStrictEq(var.get(u"this").get('mode'),Js('math')) and PyJsStrictEq(var.get('a').get('allowedInMath'),Js(False))):
                                    PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Can't use function '")+var.get('r'))+Js("' in math mode")), var.get('t').get('token')))
                                    raise PyJsTempException
                            var.put('n', var.get(u"this").callprop('parseArguments', var.get('r'), var.get('a')))
                            var.put('i', var.get('t').get('token'))
                            var.put('l', var.get(u"this").callprop('callFunction', var.get('r'), var.get('n'), var.get('n').callprop('pop'), var.get('i')))
                            return var.get('b').get('default').create(var.get('l').get('type'), var.get('l'), var.get(u"this").get('mode'))
                        else:
                            return var.get('t').get('result')
                    else:
                        return var.get(u"null")
                PyJs_e_209_._set_name('e')
                PyJs_Object_208_ = Js({'key':Js('parseFunction'),'value':PyJs_e_209_})
                @Js
                def PyJs_e_211_(t, r, a, n, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_211_}, var)
                    var.registers(['i', 'r', 'n', 'a', 't'])
                    PyJs_Object_212_ = Js({'funcName':var.get('t'),'parser':var.get(u"this"),'positions':var.get('a'),'token':var.get('n')})
                    var.put('i', PyJs_Object_212_)
                    return var.get('o').get('default').get(var.get('t')).callprop('handler', var.get('i'), var.get('r'))
                PyJs_e_211_._set_name('e')
                PyJs_Object_210_ = Js({'key':Js('callFunction'),'value':PyJs_e_211_})
                @Js
                def PyJs_e_214_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_214_}, var)
                    var.registers(['i', 'h', 'l', 'r', 'v', 'c', 'n', 'u', 's', 'a', 'f', 't'])
                    var.put('a', (var.get('r').get('numArgs')+var.get('r').get('numOptionalArgs')))
                    if PyJsStrictEq(var.get('a'),Js(0.0)):
                        return Js([Js([var.get(u"this").get('pos')])])
                    var.put('n', var.get('r').get('greediness'))
                    var.put('i', Js([var.get(u"this").get('pos')]))
                    var.put('l', Js([]))
                    #for JS loop
                    var.put('s', Js(0.0))
                    while (var.get('s')<var.get('a')):
                        try:
                            var.put('u', var.get(u"this").get('nextToken'))
                            var.put('c', (var.get('r').get('argTypes') and var.get('r').get('argTypes').get(var.get('s'))))
                            var.put('f', PyJsComma(Js(0.0), Js(None)))
                            if (var.get('s')<var.get('r').get('numOptionalArgs')):
                                if var.get('c'):
                                    var.put('f', var.get(u"this").callprop('parseGroupOfType', var.get('c'), Js(True)))
                                else:
                                    var.put('f', var.get(u"this").callprop('parseGroup', Js(True)))
                                if var.get('f').neg():
                                    var.get('l').callprop('push', var.get(u"null"))
                                    var.get('i').callprop('push', var.get(u"this").get('pos'))
                                    continue
                            else:
                                if var.get('c'):
                                    var.put('f', var.get(u"this").callprop('parseGroupOfType', var.get('c')))
                                else:
                                    var.put('f', var.get(u"this").callprop('parseGroup'))
                                if var.get('f').neg():
                                    if (var.get(u"this").get('settings').get('throwOnError').neg() and PyJsStrictEq(var.get(u"this").get('nextToken').get('text').get('0'),Js('\\'))):
                                        var.put('f', var.get('S').create(var.get(u"this").callprop('handleUnsupportedCmd', var.get(u"this").get('nextToken').get('text')), Js(False)))
                                    else:
                                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Expected group after '")+var.get('t'))+Js("'")), var.get('u')))
                                        raise PyJsTempException
                            var.put('h', PyJsComma(Js(0.0), Js(None)))
                            if var.get('f').get('isFunction'):
                                var.put('v', var.get('o').get('default').get(var.get('f').get('result')).get('greediness'))
                                if (var.get('v')>var.get('n')):
                                    var.put('h', var.get(u"this").callprop('parseFunction', var.get('f')))
                                else:
                                    PyJsTempException = JsToPyException(var.get('M').get('default').create((((((Js("Got function '")+var.get('f').get('result'))+Js("' as "))+Js("argument to '"))+var.get('t'))+Js("'")), var.get('u')))
                                    raise PyJsTempException
                            else:
                                var.put('h', var.get('f').get('result'))
                            var.get('l').callprop('push', var.get('h'))
                            var.get('i').callprop('push', var.get(u"this").get('pos'))
                        finally:
                                (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1))
                    var.get('l').callprop('push', var.get('i'))
                    return var.get('l')
                PyJs_e_214_._set_name('e')
                PyJs_Object_213_ = Js({'key':Js('parseArguments'),'value':PyJs_e_214_})
                @Js
                def PyJs_e_216_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_216_}, var)
                    var.registers(['r', 'a', 'n', 't'])
                    var.put('a', var.get(u"this").get('mode'))
                    if PyJsStrictEq(var.get('t'),Js('original')):
                        var.put('t', var.get('a'))
                    if PyJsStrictEq(var.get('t'),Js('color')):
                        return var.get(u"this").callprop('parseColorGroup', var.get('r'))
                    if PyJsStrictEq(var.get('t'),Js('size')):
                        return var.get(u"this").callprop('parseSizeGroup', var.get('r'))
                    var.get(u"this").callprop('switchMode', var.get('t'))
                    if PyJsStrictEq(var.get('t'),Js('text')):
                        var.get(u"this").callprop('consumeSpaces')
                    var.put('n', var.get(u"this").callprop('parseGroup', var.get('r')))
                    var.get(u"this").callprop('switchMode', var.get('a'))
                    return var.get('n')
                PyJs_e_216_._set_name('e')
                PyJs_Object_215_ = Js({'key':Js('parseGroupOfType'),'value':PyJs_e_216_})
                @Js
                def PyJs_e_218_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_218_}, var)
                    var.registers([])
                    while PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js(' ')):
                        var.get(u"this").callprop('consume')
                PyJs_e_218_._set_name('e')
                PyJs_Object_217_ = Js({'key':Js('consumeSpaces'),'value':PyJs_e_218_})
                @Js
                def PyJs_e_220_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_220_}, var)
                    var.registers(['i', 'l', 'r', 'n', 'a', 't'])
                    if (var.get('r') and PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),Js('['))):
                        return var.get(u"null")
                    var.put('a', var.get(u"this").get('mode'))
                    var.get(u"this").put('mode', Js('text'))
                    var.get(u"this").callprop('expect', (Js('[') if var.get('r') else Js('{')))
                    var.put('n', Js(''))
                    var.put('i', var.get(u"this").get('nextToken'))
                    var.put('l', var.get('i'))
                    while PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),(Js(']') if var.get('r') else Js('}'))):
                        if PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),Js('EOF')):
                            PyJsTempException = JsToPyException(var.get('M').get('default').create((Js('Unexpected end of input in ')+var.get('t')), var.get('i').callprop('range', var.get(u"this").get('nextToken'), var.get('n'))))
                            raise PyJsTempException
                        var.put('l', var.get(u"this").get('nextToken'))
                        var.put('n', var.get('l').get('text'), '+')
                        var.get(u"this").callprop('consume')
                    var.get(u"this").put('mode', var.get('a'))
                    var.get(u"this").callprop('expect', (Js(']') if var.get('r') else Js('}')))
                    return var.get('i').callprop('range', var.get('l'), var.get('n'))
                PyJs_e_220_._set_name('e')
                PyJs_Object_219_ = Js({'key':Js('parseStringGroup'),'value':PyJs_e_220_})
                @Js
                def PyJs_e_222_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_222_}, var)
                    var.registers(['i', 'l', 'r', 'n', 'a', 't'])
                    var.put('a', var.get(u"this").get('mode'))
                    var.get(u"this").put('mode', Js('text'))
                    var.put('n', var.get(u"this").get('nextToken'))
                    var.put('i', var.get('n'))
                    var.put('l', Js(''))
                    while (PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),Js('EOF')) and var.get('t').callprop('test', (var.get('l')+var.get(u"this").get('nextToken').get('text')))):
                        var.put('i', var.get(u"this").get('nextToken'))
                        var.put('l', var.get('i').get('text'), '+')
                        var.get(u"this").callprop('consume')
                    if PyJsStrictEq(var.get('l'),Js('')):
                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((((Js('Invalid ')+var.get('r'))+Js(": '"))+var.get('n').get('text'))+Js("'")), var.get('n')))
                        raise PyJsTempException
                    var.get(u"this").put('mode', var.get('a'))
                    return var.get('n').callprop('range', var.get('i'), var.get('l'))
                PyJs_e_222_._set_name('e')
                PyJs_Object_221_ = Js({'key':Js('parseRegexGroup'),'value':PyJs_e_222_})
                @Js
                def PyJs_e_224_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_224_}, var)
                    var.registers(['r', 'a', 't'])
                    var.put('r', var.get(u"this").callprop('parseStringGroup', Js('color'), var.get('t')))
                    if var.get('r').neg():
                        return var.get(u"null")
                    var.put('a', JsRegExp('/^(#[a-z0-9]+|[a-z]+)$/i').callprop('exec', var.get('r').get('text')))
                    if var.get('a').neg():
                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Invalid color: '")+var.get('r').get('text'))+Js("'")), var.get('r')))
                        raise PyJsTempException
                    return var.get('S').create(var.get('b').get('default').create(Js('color'), var.get('a').get('0'), var.get(u"this").get('mode')), Js(False))
                PyJs_e_224_._set_name('e')
                PyJs_Object_223_ = Js({'key':Js('parseColorGroup'),'value':PyJs_e_224_})
                @Js
                def PyJs_e_226_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_226_}, var)
                    var.registers(['r', 'a', 'n', 't'])
                    var.put('r', PyJsComma(Js(0.0), Js(None)))
                    if (var.get('t').neg() and PyJsStrictNeq(var.get(u"this").get('nextToken').get('text'),Js('{'))):
                        var.put('r', var.get(u"this").callprop('parseRegexGroup', JsRegExp('/^[-+]? *(?:$|\\d+|\\d+\\.\\d*|\\.\\d*) *[a-z]{0,2} *$/'), Js('size')))
                    else:
                        var.put('r', var.get(u"this").callprop('parseStringGroup', Js('size'), var.get('t')))
                    if var.get('r').neg():
                        return var.get(u"null")
                    var.put('a', JsRegExp('/([-+]?) *(\\d+(?:\\.\\d*)?|\\.\\d+) *([a-z]{2})/').callprop('exec', var.get('r').get('text')))
                    if var.get('a').neg():
                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Invalid size: '")+var.get('r').get('text'))+Js("'")), var.get('r')))
                        raise PyJsTempException
                    PyJs_Object_227_ = Js({'number':(+(var.get('a').get('1')+var.get('a').get('2'))),'unit':var.get('a').get('3')})
                    var.put('n', PyJs_Object_227_)
                    if var.get('y').get('default').callprop('validUnit', var.get('n')).neg():
                        PyJsTempException = JsToPyException(var.get('M').get('default').create(((Js("Invalid unit: '")+var.get('n').get('unit'))+Js("'")), var.get('r')))
                        raise PyJsTempException
                    return var.get('S').create(var.get('b').get('default').create(Js('size'), var.get('n'), var.get(u"this").get('mode')), Js(False))
                PyJs_e_226_._set_name('e')
                PyJs_Object_225_ = Js({'key':Js('parseSizeGroup'),'value':PyJs_e_226_})
                @Js
                def PyJs_e_229_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_229_}, var)
                    var.registers(['r', 'a', 'n', 't'])
                    var.put('r', var.get(u"this").get('nextToken'))
                    if PyJsStrictEq(var.get(u"this").get('nextToken').get('text'),(Js('[') if var.get('t') else Js('{'))):
                        var.get(u"this").callprop('consume')
                        var.put('a', var.get(u"this").callprop('parseExpression', Js(False), (Js(']') if var.get('t') else var.get(u"null"))))
                        var.put('n', var.get(u"this").get('nextToken'))
                        var.get(u"this").callprop('expect', (Js(']') if var.get('t') else Js('}')))
                        if PyJsStrictEq(var.get(u"this").get('mode'),Js('text')):
                            var.get(u"this").callprop('formLigatures', var.get('a'))
                        return var.get('S').create(var.get('b').get('default').create(Js('ordgroup'), var.get('a'), var.get(u"this").get('mode'), var.get('r'), var.get('n')), Js(False))
                    else:
                        return (var.get(u"null") if var.get('t') else var.get(u"this").callprop('parseSymbol'))
                PyJs_e_229_._set_name('e')
                PyJs_Object_228_ = Js({'key':Js('parseGroup'),'value':PyJs_e_229_})
                @Js
                def PyJs_e_231_(t, this, arguments, var=var):
                    var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_231_}, var)
                    var.registers(['i', 'r', 'n', 'a', 't'])
                    var.put('r', (var.get('t').get('length')-Js(1.0)))
                    #for JS loop
                    var.put('a', Js(0.0))
                    while (var.get('a')<var.get('r')):
                        try:
                            var.put('n', var.get('t').get(var.get('a')))
                            var.put('i', var.get('n').get('value'))
                            if (PyJsStrictEq(var.get('i'),Js('-')) and PyJsStrictEq(var.get('t').get((var.get('a')+Js(1.0))).get('value'),Js('-'))):
                                if (((var.get('a')+Js(1.0))<var.get('r')) and PyJsStrictEq(var.get('t').get((var.get('a')+Js(2.0))).get('value'),Js('-'))):
                                    var.get('t').callprop('splice', var.get('a'), Js(3.0), var.get('b').get('default').create(Js('textord'), Js('---'), Js('text'), var.get('n'), var.get('t').get((var.get('a')+Js(2.0)))))
                                    var.put('r', Js(2.0), '-')
                                else:
                                    var.get('t').callprop('splice', var.get('a'), Js(2.0), var.get('b').get('default').create(Js('textord'), Js('--'), Js('text'), var.get('n'), var.get('t').get((var.get('a')+Js(1.0)))))
                                    var.put('r', Js(1.0), '-')
                            if ((PyJsStrictEq(var.get('i'),Js("'")) or PyJsStrictEq(var.get('i'),Js('`'))) and PyJsStrictEq(var.get('t').get((var.get('a')+Js(1.0))).get('value'),var.get('i'))):
                                var.get('t').callprop('splice', var.get('a'), Js(2.0), var.get('b').get('default').create(Js('textord'), (var.get('i')+var.get('i')), Js('text'), var.get('n'), var.get('t').get((var.get('a')+Js(1.0)))))
                                var.put('r', Js(1.0), '-')
                        finally:
                                var.put('a',Js(var.get('a').to_number())+Js(1))
                PyJs_e_231_._set_name('e')
                PyJs_Object_230_ = Js({'key':Js('formLigatures'),'value':PyJs_e_231_})
                @Js
                def PyJs_e_233_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_233_}, var)
                    var.registers(['t'])
                    var.put('t', var.get(u"this").get('nextToken'))
                    if var.get('o').get('default').get(var.get('t').get('text')):
                        var.get(u"this").callprop('consume')
                        return var.get('S').create(var.get('t').get('text'), Js(True), var.get('t'))
                    else:
                        if var.get('d').get('default').get(var.get(u"this").get('mode')).get(var.get('t').get('text')):
                            var.get(u"this").callprop('consume')
                            return var.get('S').create(var.get('b').get('default').create(var.get('d').get('default').get(var.get(u"this").get('mode')).get(var.get('t').get('text')).get('group'), var.get('t').get('text'), var.get(u"this").get('mode'), var.get('t')), Js(False), var.get('t'))
                        else:
                            if (PyJsStrictEq(var.get(u"this").get('mode'),Js('text')) and var.get('x').get('cjkRegex').callprop('test', var.get('t').get('text'))):
                                var.get(u"this").callprop('consume')
                                return var.get('S').create(var.get('b').get('default').create(Js('textord'), var.get('t').get('text'), var.get(u"this").get('mode'), var.get('t')), Js(False), var.get('t'))
                            else:
                                if PyJsStrictEq(var.get('t').get('text'),Js('$')):
                                    return var.get('S').create(var.get('t').get('text'), Js(False), var.get('t'))
                                else:
                                    return var.get(u"null")
                PyJs_e_233_._set_name('e')
                PyJs_Object_232_ = Js({'key':Js('parseSymbol'),'value':PyJs_e_233_})
                return PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_175_, PyJs_Object_177_, PyJs_Object_179_, PyJs_Object_181_, PyJs_Object_183_, PyJs_Object_185_, PyJs_Object_187_, PyJs_Object_189_, PyJs_Object_191_, PyJs_Object_195_, PyJs_Object_198_, PyJs_Object_208_, PyJs_Object_210_, PyJs_Object_213_, PyJs_Object_215_, PyJs_Object_217_, PyJs_Object_219_, PyJs_Object_221_, PyJs_Object_223_, PyJs_Object_225_, PyJs_Object_228_, PyJs_Object_230_, PyJs_Object_232_]))
            PyJs_LONG_234_()
            return var.get('e')
        PyJs_anonymous_174_._set_name('anonymous')
        var.put('A', PyJs_anonymous_174_())
        var.get('A').put('endOfExpression', Js([Js('}'), Js('\\end'), Js('\\right'), Js('&'), Js('\\\\'), Js('\\cr')]))
        var.get('A').put('SUPSUB_GREEDINESS', Js(1.0))
        var.get('A').put('sizeFuncs', Js([Js('\\tiny'), Js('\\sixptsize'), Js('\\scriptsize'), Js('\\footnotesize'), Js('\\small'), Js('\\normalsize'), Js('\\large'), Js('\\Large'), Js('\\LARGE'), Js('\\huge'), Js('\\Huge')]))
        var.get('A').put('styleFuncs', Js([Js('\\displaystyle'), Js('\\textstyle'), Js('\\scriptstyle'), Js('\\scriptscriptstyle')]))
        PyJs_Object_235_ = Js({'\\rm':Js('mathrm'),'\\sf':Js('mathsf'),'\\tt':Js('mathtt'),'\\bf':Js('mathbf'),'\\it':Js('mathit')})
        var.get('A').put('oldFontFuncs', PyJs_Object_235_)
        var.get('A').get('prototype').put('ParseNode', var.get('b').get('default'))
        var.get('t').put('exports', var.get('A'))
    PyJs_anonymous_172_._set_name('anonymous')
    PyJs_Object_236_ = Js({'./MacroExpander':Js(27.0),'./ParseError':Js(29.0),'./ParseNode':Js(30.0),'./environments':Js(40.0),'./functions':Js(43.0),'./symbols':Js(48.0),'./unicodeRegexes':Js(49.0),'./units':Js(50.0),'./utils':Js(51.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0)})
    @Js
    def PyJs_anonymous_237_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'o', 'n', 's', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_s_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_238_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_238_)
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('s')(var.get('a')))
        var.put('i', var.get('e')(Js('./utils')))
        var.put('l', var.get('s')(var.get('i')))
        pass
        @Js
        def PyJs_e_239_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_239_}, var)
            var.registers(['t'])
            PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
            PyJs_Object_240_ = Js({})
            var.put('t', (var.get('t') or PyJs_Object_240_))
            var.get(u"this").put('displayMode', var.get('l').get('default').callprop('deflt', var.get('t').get('displayMode'), Js(False)))
            var.get(u"this").put('throwOnError', var.get('l').get('default').callprop('deflt', var.get('t').get('throwOnError'), Js(True)))
            var.get(u"this").put('errorColor', var.get('l').get('default').callprop('deflt', var.get('t').get('errorColor'), Js('#cc0000')))
            PyJs_Object_241_ = Js({})
            var.get(u"this").put('macros', (var.get('t').get('macros') or PyJs_Object_241_))
            var.get(u"this").put('colorIsTextColor', var.get('l').get('default').callprop('deflt', var.get('t').get('colorIsTextColor'), Js(False)))
        PyJs_e_239_._set_name('e')
        var.put('o', PyJs_e_239_)
        var.get('t').put('exports', var.get('o'))
    PyJs_anonymous_237_._set_name('anonymous')
    PyJs_Object_242_ = Js({'./utils':Js(51.0),'babel-runtime/helpers/classCallCheck':Js(4.0)})
    @Js
    def PyJs_anonymous_243_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'b', 'l', 'c', 'g', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_s_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_244_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_244_)
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('s')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('s')(var.get('i')))
        pass
        @Js
        def PyJs_anonymous_245_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, a, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 'a', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('id', var.get('t'))
                var.get(u"this").put('size', var.get('r'))
                var.get(u"this").put('cramped', var.get('a'))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_247_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_247_}, var)
                var.registers([])
                return var.get('g').get(var.get('y').get(var.get(u"this").get('id')))
            PyJs_e_247_._set_name('e')
            PyJs_Object_246_ = Js({'key':Js('sup'),'value':PyJs_e_247_})
            @Js
            def PyJs_e_249_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_249_}, var)
                var.registers([])
                return var.get('g').get(var.get('x').get(var.get(u"this").get('id')))
            PyJs_e_249_._set_name('e')
            PyJs_Object_248_ = Js({'key':Js('sub'),'value':PyJs_e_249_})
            @Js
            def PyJs_e_251_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_251_}, var)
                var.registers([])
                return var.get('g').get(var.get('w').get(var.get(u"this").get('id')))
            PyJs_e_251_._set_name('e')
            PyJs_Object_250_ = Js({'key':Js('fracNum'),'value':PyJs_e_251_})
            @Js
            def PyJs_e_253_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_253_}, var)
                var.registers([])
                return var.get('g').get(var.get('b').get(var.get(u"this").get('id')))
            PyJs_e_253_._set_name('e')
            PyJs_Object_252_ = Js({'key':Js('fracDen'),'value':PyJs_e_253_})
            @Js
            def PyJs_e_255_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_255_}, var)
                var.registers([])
                return var.get('g').get(var.get('k').get(var.get(u"this").get('id')))
            PyJs_e_255_._set_name('e')
            PyJs_Object_254_ = Js({'key':Js('cramp'),'value':PyJs_e_255_})
            @Js
            def PyJs_e_257_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_257_}, var)
                var.registers([])
                return var.get('g').get(var.get('M').get(var.get(u"this").get('id')))
            PyJs_e_257_._set_name('e')
            PyJs_Object_256_ = Js({'key':Js('text'),'value':PyJs_e_257_})
            @Js
            def PyJs_e_259_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_259_}, var)
                var.registers([])
                return (var.get(u"this").get('size')>=Js(2.0))
            PyJs_e_259_._set_name('e')
            PyJs_Object_258_ = Js({'key':Js('isTight'),'value':PyJs_e_259_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_246_, PyJs_Object_248_, PyJs_Object_250_, PyJs_Object_252_, PyJs_Object_254_, PyJs_Object_256_, PyJs_Object_258_]))
            return var.get('e')
        PyJs_anonymous_245_._set_name('anonymous')
        var.put('o', PyJs_anonymous_245_())
        var.put('u', Js(0.0))
        var.put('c', Js(1.0))
        var.put('f', Js(2.0))
        var.put('h', Js(3.0))
        var.put('v', Js(4.0))
        var.put('d', Js(5.0))
        var.put('p', Js(6.0))
        var.put('m', Js(7.0))
        var.put('g', Js([var.get('o').create(var.get('u'), Js(0.0), Js(False)), var.get('o').create(var.get('c'), Js(0.0), Js(True)), var.get('o').create(var.get('f'), Js(1.0), Js(False)), var.get('o').create(var.get('h'), Js(1.0), Js(True)), var.get('o').create(var.get('v'), Js(2.0), Js(False)), var.get('o').create(var.get('d'), Js(2.0), Js(True)), var.get('o').create(var.get('p'), Js(3.0), Js(False)), var.get('o').create(var.get('m'), Js(3.0), Js(True))]))
        var.put('y', Js([var.get('v'), var.get('d'), var.get('v'), var.get('d'), var.get('p'), var.get('m'), var.get('p'), var.get('m')]))
        var.put('x', Js([var.get('d'), var.get('d'), var.get('d'), var.get('d'), var.get('m'), var.get('m'), var.get('m'), var.get('m')]))
        var.put('w', Js([var.get('f'), var.get('h'), var.get('v'), var.get('d'), var.get('p'), var.get('m'), var.get('p'), var.get('m')]))
        var.put('b', Js([var.get('h'), var.get('h'), var.get('d'), var.get('d'), var.get('m'), var.get('m'), var.get('m'), var.get('m')]))
        var.put('k', Js([var.get('c'), var.get('c'), var.get('h'), var.get('h'), var.get('d'), var.get('d'), var.get('m'), var.get('m')]))
        var.put('M', Js([var.get('u'), var.get('c'), var.get('f'), var.get('h'), var.get('f'), var.get('h'), var.get('f'), var.get('h')]))
        PyJs_Object_260_ = Js({'DISPLAY':var.get('g').get(var.get('u')),'TEXT':var.get('g').get(var.get('f')),'SCRIPT':var.get('g').get(var.get('v')),'SCRIPTSCRIPT':var.get('g').get(var.get('p'))})
        var.get('t').put('exports', PyJs_Object_260_)
    PyJs_anonymous_243_._set_name('anonymous')
    PyJs_Object_261_ = Js({'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0)})
    @Js
    def PyJs_anonymous_262_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'S', 'b', 'l', 'c', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_f_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_263_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_263_)
        PyJsHoisted_f_.func_name = 'f'
        var.put('f', PyJsHoisted_f_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./domTree')))
        var.put('n', var.get('f')(var.get('a')))
        var.put('i', var.get('e')(Js('./fontMetrics')))
        var.put('l', var.get('f')(var.get('i')))
        var.put('s', var.get('e')(Js('./symbols')))
        var.put('o', var.get('f')(var.get('s')))
        var.put('u', var.get('e')(Js('./utils')))
        var.put('c', var.get('f')(var.get('u')))
        pass
        var.put('h', Js([Js('\\imath'), Js('\\jmath'), Js('\\pounds')]))
        @Js
        def PyJs_e_264_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_264_}, var)
            var.registers(['r', 'a', 't'])
            if (var.get('o').get('default').get(var.get('a')).get(var.get('t')) and var.get('o').get('default').get(var.get('a')).get(var.get('t')).get('replace')):
                var.put('t', var.get('o').get('default').get(var.get('a')).get(var.get('t')).get('replace'))
            PyJs_Object_265_ = Js({'value':var.get('t'),'metrics':var.get('l').get('default').callprop('getCharacterMetrics', var.get('t'), var.get('r'))})
            return PyJs_Object_265_
        PyJs_e_264_._set_name('e')
        var.put('v', PyJs_e_264_)
        @Js
        def PyJs_e_266_(t, r, a, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_266_}, var)
            var.registers(['i', 'r', 'l', 'c', 'o', 'u', 's', 'a', 't'])
            var.put('s', var.get('v')(var.get('t'), var.get('r'), var.get('a')))
            var.put('o', var.get('s').get('metrics'))
            var.put('t', var.get('s').get('value'))
            var.put('u', PyJsComma(Js(0.0), Js(None)))
            if var.get('o'):
                var.put('c', var.get('o').get('italic'))
                if PyJsStrictEq(var.get('a'),Js('text')):
                    var.put('c', Js(0.0))
                var.put('u', var.get('n').get('default').get('symbolNode').create(var.get('t'), var.get('o').get('height'), var.get('o').get('depth'), var.get('c'), var.get('o').get('skew'), var.get('l')))
            else:
                (PyJsStrictNeq(var.get('console',throw=False).typeof(),Js('undefined')) and var.get('console').callprop('warn', ((((Js("No character metrics for '")+var.get('t'))+Js("' in style '"))+var.get('r'))+Js("'"))))
                var.put('u', var.get('n').get('default').get('symbolNode').create(var.get('t'), Js(0.0), Js(0.0), Js(0.0), Js(0.0), var.get('l')))
            if var.get('i'):
                var.get('u').put('maxFontSize', var.get('i').get('sizeMultiplier'))
                if var.get('i').get('style').callprop('isTight'):
                    var.get('u').get('classes').callprop('push', Js('mtight'))
                if var.get('i').callprop('getColor'):
                    var.get('u').get('style').put('color', var.get('i').callprop('getColor'))
            return var.get('u')
        PyJs_e_266_._set_name('e')
        var.put('d', PyJs_e_266_)
        @Js
        def PyJs_e_267_(t, r, a, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_267_}, var)
            var.registers(['r', 'a', 'n', 't'])
            if (PyJsStrictEq(var.get('t'),Js('\\')) or PyJsStrictEq(var.get('o').get('default').get(var.get('r')).get(var.get('t')).get('font'),Js('main'))):
                return var.get('d')(var.get('t'), Js('Main-Regular'), var.get('r'), var.get('a'), var.get('n'))
            else:
                return var.get('d')(var.get('t'), Js('AMS-Regular'), var.get('r'), var.get('a'), var.get('n').callprop('concat', Js([Js('amsrm')])))
        PyJs_e_267_._set_name('e')
        var.put('p', PyJs_e_267_)
        @Js
        def PyJs_e_268_(t, r, a, n, i, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'this':this, 'arguments':arguments, 'e':PyJs_e_268_}, var)
            var.registers(['i', 'r', 'l', 'n', 's', 'a', 't'])
            if PyJsStrictEq(var.get('i'),Js('mathord')):
                var.put('l', var.get('g')(var.get('t'), var.get('r'), var.get('a'), var.get('n')))
                return var.get('d')(var.get('t'), var.get('l').get('fontName'), var.get('r'), var.get('a'), var.get('n').callprop('concat', Js([var.get('l').get('fontClass')])))
            else:
                if PyJsStrictEq(var.get('i'),Js('textord')):
                    var.put('s', (var.get('o').get('default').get(var.get('r')).get(var.get('t')) and var.get('o').get('default').get(var.get('r')).get(var.get('t')).get('font')))
                    if PyJsStrictEq(var.get('s'),Js('ams')):
                        return var.get('d')(var.get('t'), Js('AMS-Regular'), var.get('r'), var.get('a'), var.get('n').callprop('concat', Js([Js('amsrm')])))
                    else:
                        return var.get('d')(var.get('t'), Js('Main-Regular'), var.get('r'), var.get('a'), var.get('n').callprop('concat', Js([Js('mathrm')])))
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(((Js('unexpected type: ')+var.get('i'))+Js(' in mathDefault'))))
                    raise PyJsTempException
        PyJs_e_268_._set_name('e')
        var.put('m', PyJs_e_268_)
        @Js
        def PyJs_e_269_(t, r, a, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_269_}, var)
            var.registers(['r', 'a', 'n', 't'])
            if (JsRegExp('/[0-9]/').callprop('test', var.get('t').callprop('charAt', Js(0.0))) or var.get('c').get('default').callprop('contains', var.get('h'), var.get('t'))):
                PyJs_Object_270_ = Js({'fontName':Js('Main-Italic'),'fontClass':Js('mainit')})
                return PyJs_Object_270_
            else:
                PyJs_Object_271_ = Js({'fontName':Js('Math-Italic'),'fontClass':Js('mathit')})
                return PyJs_Object_271_
        PyJs_e_269_._set_name('e')
        var.put('g', PyJs_e_269_)
        @Js
        def PyJs_e_272_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_272_}, var)
            var.registers(['i', 'l', 'r', 'o', 'n', 's', 'a', 't'])
            var.put('n', var.get('t').get('mode'))
            var.put('i', var.get('t').get('value'))
            var.put('l', Js([Js('mord')]))
            var.put('s', var.get('r').get('font'))
            if var.get('s'):
                var.put('o', PyJsComma(Js(0.0), Js(None)))
                if (PyJsStrictEq(var.get('s'),Js('mathit')) or var.get('c').get('default').callprop('contains', var.get('h'), var.get('i'))):
                    var.put('o', var.get('g')(var.get('i'), var.get('n'), var.get('r'), var.get('l')))
                else:
                    var.put('o', var.get('S').get(var.get('s')))
                if var.get('v')(var.get('i'), var.get('o').get('fontName'), var.get('n')).get('metrics'):
                    return var.get('d')(var.get('i'), var.get('o').get('fontName'), var.get('n'), var.get('r'), var.get('l').callprop('concat', Js([(var.get('o').get('fontClass') or var.get('s'))])))
                else:
                    return var.get('m')(var.get('i'), var.get('n'), var.get('r'), var.get('l'), var.get('a'))
            else:
                return var.get('m')(var.get('i'), var.get('n'), var.get('r'), var.get('l'), var.get('a'))
        PyJs_e_272_._set_name('e')
        var.put('y', PyJs_e_272_)
        @Js
        def PyJs_e_273_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_273_}, var)
            var.registers(['i', 'r', 'n', 'a', 't'])
            var.put('r', Js(0.0))
            var.put('a', Js(0.0))
            var.put('n', Js(0.0))
            if var.get('t').get('children'):
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('t').get('children').get('length')):
                    try:
                        if (var.get('t').get('children').get(var.get('i')).get('height')>var.get('r')):
                            var.put('r', var.get('t').get('children').get(var.get('i')).get('height'))
                        if (var.get('t').get('children').get(var.get('i')).get('depth')>var.get('a')):
                            var.put('a', var.get('t').get('children').get(var.get('i')).get('depth'))
                        if (var.get('t').get('children').get(var.get('i')).get('maxFontSize')>var.get('n')):
                            var.put('n', var.get('t').get('children').get(var.get('i')).get('maxFontSize'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get('t').put('height', var.get('r'))
            var.get('t').put('depth', var.get('a'))
            var.get('t').put('maxFontSize', var.get('n'))
        PyJs_e_273_._set_name('e')
        var.put('x', PyJs_e_273_)
        @Js
        def PyJs_e_274_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_274_}, var)
            var.registers(['r', 't', 'a', 'i'])
            var.put('i', var.get('n').get('default').get('span').create(var.get('t'), var.get('r'), var.get('a')))
            var.get('x')(var.get('i'))
            return var.get('i')
        PyJs_e_274_._set_name('e')
        var.put('w', PyJs_e_274_)
        @Js
        def PyJs_e_275_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_275_}, var)
            var.registers(['r', 't'])
            var.get('t').put('children', var.get('r').callprop('concat', var.get('t').get('children')))
            var.get('x')(var.get('t'))
        PyJs_e_275_._set_name('e')
        var.put('b', PyJs_e_275_)
        @Js
        def PyJs_e_276_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_276_}, var)
            var.registers(['r', 't'])
            var.put('r', var.get('n').get('default').get('documentFragment').create(var.get('t')))
            var.get('x')(var.get('r'))
            return var.get('r')
        PyJs_e_276_._set_name('e')
        var.put('k', PyJs_e_276_)
        @Js
        def PyJs_e_277_(t, r, a, i, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'this':this, 'arguments':arguments, 'e':PyJs_e_277_}, var)
            var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'x', 'a', 'A', 'S', 'b', 'l', 'c', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 's', 'f'])
            var.put('l', PyJsComma(Js(0.0), Js(None)))
            var.put('s', PyJsComma(Js(0.0), Js(None)))
            var.put('o', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('r'),Js('individualShift')):
                var.put('u', var.get('t'))
                var.put('t', Js([var.get('u').get('0')]))
                var.put('l', ((-var.get('u').get('0').get('shift'))-var.get('u').get('0').get('elem').get('depth')))
                var.put('s', var.get('l'))
                #for JS loop
                var.put('o', Js(1.0))
                while (var.get('o')<var.get('u').get('length')):
                    try:
                        var.put('c', (((-var.get('u').get(var.get('o')).get('shift'))-var.get('s'))-var.get('u').get(var.get('o')).get('elem').get('depth')))
                        var.put('f', (var.get('c')-(var.get('u').get((var.get('o')-Js(1.0))).get('elem').get('height')+var.get('u').get((var.get('o')-Js(1.0))).get('elem').get('depth'))))
                        var.put('s', (var.get('s')+var.get('c')))
                        PyJs_Object_278_ = Js({'type':Js('kern'),'size':var.get('f')})
                        var.get('t').callprop('push', PyJs_Object_278_)
                        var.get('t').callprop('push', var.get('u').get(var.get('o')))
                    finally:
                            (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            else:
                if PyJsStrictEq(var.get('r'),Js('top')):
                    var.put('h', var.get('a'))
                    #for JS loop
                    var.put('o', Js(0.0))
                    while (var.get('o')<var.get('t').get('length')):
                        try:
                            if PyJsStrictEq(var.get('t').get(var.get('o')).get('type'),Js('kern')):
                                var.put('h', var.get('t').get(var.get('o')).get('size'), '-')
                            else:
                                var.put('h', (var.get('t').get(var.get('o')).get('elem').get('height')+var.get('t').get(var.get('o')).get('elem').get('depth')), '-')
                        finally:
                                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
                    var.put('l', var.get('h'))
                else:
                    if PyJsStrictEq(var.get('r'),Js('bottom')):
                        var.put('l', (-var.get('a')))
                    else:
                        if PyJsStrictEq(var.get('r'),Js('shift')):
                            var.put('l', ((-var.get('t').get('0').get('elem').get('depth'))-var.get('a')))
                        else:
                            if PyJsStrictEq(var.get('r'),Js('firstBaseline')):
                                var.put('l', (-var.get('t').get('0').get('elem').get('depth')))
                            else:
                                var.put('l', Js(0.0))
            var.put('v', Js(0.0))
            #for JS loop
            var.put('o', Js(0.0))
            while (var.get('o')<var.get('t').get('length')):
                try:
                    if PyJsStrictEq(var.get('t').get(var.get('o')).get('type'),Js('elem')):
                        var.put('d', var.get('t').get(var.get('o')).get('elem'))
                        var.put('v', var.get('Math').callprop('max', var.get('v'), var.get('d').get('maxFontSize'), var.get('d').get('height')))
                finally:
                        (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            var.put('v', Js(2.0), '+')
            var.put('p', var.get('w')(Js([Js('pstrut')]), Js([])))
            var.get('p').get('style').put('height', (var.get('v')+Js('em')))
            var.put('m', Js([]))
            var.put('g', var.get('l'))
            var.put('y', var.get('l'))
            var.put('s', var.get('l'))
            #for JS loop
            var.put('o', Js(0.0))
            while (var.get('o')<var.get('t').get('length')):
                try:
                    if PyJsStrictEq(var.get('t').get(var.get('o')).get('type'),Js('kern')):
                        var.put('s', var.get('t').get(var.get('o')).get('size'), '+')
                    else:
                        var.put('x', var.get('t').get(var.get('o')).get('elem'))
                        var.put('b', var.get('w')(Js([]), Js([var.get('p'), var.get('x')])))
                        var.get('b').get('style').put('top', ((((-var.get('v'))-var.get('s'))-var.get('x').get('depth'))+Js('em')))
                        if var.get('t').get(var.get('o')).get('marginLeft'):
                            var.get('b').get('style').put('marginLeft', var.get('t').get(var.get('o')).get('marginLeft'))
                        if var.get('t').get(var.get('o')).get('marginRight'):
                            var.get('b').get('style').put('marginRight', var.get('t').get(var.get('o')).get('marginRight'))
                        var.get('m').callprop('push', var.get('b'))
                        var.put('s', (var.get('x').get('height')+var.get('x').get('depth')), '+')
                    var.put('g', var.get('Math').callprop('min', var.get('g'), var.get('s')))
                    var.put('y', var.get('Math').callprop('max', var.get('y'), var.get('s')))
                finally:
                        (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            var.put('k', var.get('w')(Js([Js('vlist')]), var.get('m')))
            var.get('k').get('style').put('height', (var.get('y')+Js('em')))
            var.put('M', PyJsComma(Js(0.0), Js(None)))
            if (var.get('g')<Js(0.0)):
                var.put('z', var.get('w')(Js([Js('vlist')]), Js([])))
                var.get('z').get('style').put('height', ((-var.get('g'))+Js('em')))
                var.put('S', var.get('w')(Js([Js('vlist-s')]), Js([var.get('n').get('default').get('symbolNode').create(Js('\u200b'))])))
                var.put('M', Js([var.get('w')(Js([Js('vlist-r')]), Js([var.get('k'), var.get('S')])), var.get('w')(Js([Js('vlist-r')]), Js([var.get('z')]))]))
            else:
                var.put('M', Js([var.get('w')(Js([Js('vlist-r')]), Js([var.get('k')]))]))
            var.put('A', var.get('w')(Js([Js('vlist-t')]), var.get('M')))
            if PyJsStrictEq(var.get('M').get('length'),Js(2.0)):
                var.get('A').get('classes').callprop('push', Js('vlist-t2'))
            var.get('A').put('height', var.get('y'))
            var.get('A').put('depth', (-var.get('g')))
            return var.get('A')
        PyJs_e_277_._set_name('e')
        var.put('M', PyJs_e_277_)
        PyJs_Object_280_ = Js({'size':Js('2em'),'className':Js('qquad')})
        PyJs_Object_281_ = Js({'size':Js('1em'),'className':Js('quad')})
        PyJs_Object_282_ = Js({'size':Js('0.5em'),'className':Js('enspace')})
        PyJs_Object_283_ = Js({'size':Js('0.277778em'),'className':Js('thickspace')})
        PyJs_Object_284_ = Js({'size':Js('0.22222em'),'className':Js('mediumspace')})
        PyJs_Object_285_ = Js({'size':Js('0.16667em'),'className':Js('thinspace')})
        PyJs_Object_286_ = Js({'size':Js('-0.16667em'),'className':Js('negativethinspace')})
        PyJs_Object_279_ = Js({'\\qquad':PyJs_Object_280_,'\\quad':PyJs_Object_281_,'\\enspace':PyJs_Object_282_,'\\;':PyJs_Object_283_,'\\:':PyJs_Object_284_,'\\,':PyJs_Object_285_,'\\!':PyJs_Object_286_})
        var.put('z', PyJs_Object_279_)
        PyJs_Object_288_ = Js({'variant':Js('bold'),'fontName':Js('Main-Bold')})
        PyJs_Object_289_ = Js({'variant':Js('normal'),'fontName':Js('Main-Regular')})
        PyJs_Object_290_ = Js({'variant':Js('italic'),'fontName':Js('Main-Italic')})
        PyJs_Object_291_ = Js({'variant':Js('double-struck'),'fontName':Js('AMS-Regular')})
        PyJs_Object_292_ = Js({'variant':Js('script'),'fontName':Js('Caligraphic-Regular')})
        PyJs_Object_293_ = Js({'variant':Js('fraktur'),'fontName':Js('Fraktur-Regular')})
        PyJs_Object_294_ = Js({'variant':Js('script'),'fontName':Js('Script-Regular')})
        PyJs_Object_295_ = Js({'variant':Js('sans-serif'),'fontName':Js('SansSerif-Regular')})
        PyJs_Object_296_ = Js({'variant':Js('monospace'),'fontName':Js('Typewriter-Regular')})
        PyJs_Object_287_ = Js({'mathbf':PyJs_Object_288_,'mathrm':PyJs_Object_289_,'textit':PyJs_Object_290_,'mathbb':PyJs_Object_291_,'mathcal':PyJs_Object_292_,'mathfrak':PyJs_Object_293_,'mathscr':PyJs_Object_294_,'mathsf':PyJs_Object_295_,'mathtt':PyJs_Object_296_})
        var.put('S', PyJs_Object_287_)
        PyJs_Object_297_ = Js({'fontMap':var.get('S'),'makeSymbol':var.get('d'),'mathsym':var.get('p'),'makeSpan':var.get('w'),'makeFragment':var.get('k'),'makeVList':var.get('M'),'makeOrd':var.get('y'),'prependChildren':var.get('b'),'spacingFunctions':var.get('z')})
        var.get('t').put('exports', PyJs_Object_297_)
    PyJs_anonymous_262_._set_name('anonymous')
    PyJs_Object_298_ = Js({'./domTree':Js(39.0),'./fontMetrics':Js(41.0),'./symbols':Js(48.0),'./utils':Js(51.0)})
    @Js
    def PyJs_anonymous_299_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['B', 'R', 'q', 'E', 'r', 'o', 'y', 'T', 'N', 'L', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'O', '_', 'b', 'P', 'l', 'c', 'C', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_b_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_300_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_300_)
        PyJsHoisted_b_.func_name = 'b'
        var.put('b', PyJsHoisted_b_)
        @Js
        def PyJsHoisted_O_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
            var.put('a', var.get('C')(var.get('e'), var.get('t'), Js(False)))
            var.put('n', (var.get('t').get('sizeMultiplier')/var.get('r').get('sizeMultiplier')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('a').get('length')):
                try:
                    var.put('l', var.get('y').get('default').callprop('indexOf', var.get('a').get(var.get('i')).get('classes'), Js('sizing')))
                    if (var.get('l')<Js(0.0)):
                        var.get('Array').get('prototype').get('push').callprop('apply', var.get('a').get(var.get('i')).get('classes'), var.get('t').callprop('sizingClasses', var.get('r')))
                    else:
                        if PyJsStrictEq(var.get('a').get(var.get('i')).get('classes').get((var.get('l')+Js(1.0))),(Js('reset-size')+var.get('t').get('size'))):
                            var.get('a').get(var.get('i')).get('classes').put((var.get('l')+Js(1.0)), (Js('reset-size')+var.get('r').get('size')))
                    var.get('a').get(var.get('i')).put('height', var.get('n'), '*')
                    var.get('a').get(var.get('i')).put('depth', var.get('n'), '*')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('c').get('default').callprop('makeFragment', var.get('a'))
        PyJsHoisted_O_.func_name = 'O'
        var.put('O', PyJsHoisted_O_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/core-js/json/stringify')))
        var.put('n', var.get('b')(var.get('a')))
        var.put('i', var.get('e')(Js('./ParseError')))
        var.put('l', var.get('b')(var.get('i')))
        var.put('s', var.get('e')(Js('./Style')))
        var.put('o', var.get('b')(var.get('s')))
        var.put('u', var.get('e')(Js('./buildCommon')))
        var.put('c', var.get('b')(var.get('u')))
        var.put('f', var.get('e')(Js('./delimiter')))
        var.put('h', var.get('b')(var.get('f')))
        var.put('v', var.get('e')(Js('./domTree')))
        var.put('d', var.get('b')(var.get('v')))
        var.put('p', var.get('e')(Js('./units')))
        var.put('m', var.get('b')(var.get('p')))
        var.put('g', var.get('e')(Js('./utils')))
        var.put('y', var.get('b')(var.get('g')))
        var.put('x', var.get('e')(Js('./stretchy')))
        var.put('w', var.get('b')(var.get('x')))
        pass
        @Js
        def PyJs_e_301_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_301_}, var)
            var.registers(['t'])
            return (var.get('t').instanceof(var.get('d').get('default').get('span')) and PyJsStrictEq(var.get('t').get('classes').get('0'),Js('mspace')))
        PyJs_e_301_._set_name('e')
        var.put('k', PyJs_e_301_)
        @Js
        def PyJs_e_302_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_302_}, var)
            var.registers(['t'])
            return (var.get('t') and PyJsStrictEq(var.get('t').get('classes').get('0'),Js('mbin')))
        PyJs_e_302_._set_name('e')
        var.put('M', PyJs_e_302_)
        @Js
        def PyJs_e_303_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_303_}, var)
            var.registers(['r', 't'])
            if var.get('t'):
                return var.get('y').get('default').callprop('contains', Js([Js('mbin'), Js('mopen'), Js('mrel'), Js('mop'), Js('mpunct')]), var.get('t').get('classes').get('0'))
            else:
                return var.get('r')
        PyJs_e_303_._set_name('e')
        var.put('z', PyJs_e_303_)
        @Js
        def PyJs_e_304_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_304_}, var)
            var.registers(['r', 't'])
            if var.get('t'):
                return var.get('y').get('default').callprop('contains', Js([Js('mrel'), Js('mclose'), Js('mpunct')]), var.get('t').get('classes').get('0'))
            else:
                return var.get('r')
        PyJs_e_304_._set_name('e')
        var.put('S', PyJs_e_304_)
        @Js
        def PyJs_e_305_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_305_}, var)
            var.registers(['r', 'a', 't'])
            var.put('a', var.get('r'))
            while ((var.get('a')<var.get('t').get('length')) and var.get('k')(var.get('t').get(var.get('a')))):
                (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
            if PyJsStrictEq(var.get('a'),var.get('r')):
                return var.get(u"null")
            else:
                return var.get('t').callprop('splice', var.get('r'), (var.get('a')-var.get('r')))
        PyJs_e_305_._set_name('e')
        var.put('A', PyJs_e_305_)
        @Js
        def PyJs_e_306_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_306_}, var)
            var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'g', 'o', 'n', 's', 'a', 'f', 't'])
            var.put('n', Js([]))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('t').get('length')):
                try:
                    var.put('l', var.get('t').get(var.get('i')))
                    var.put('s', var.get('L')(var.get('l'), var.get('r')))
                    if var.get('s').instanceof(var.get('d').get('default').get('documentFragment')):
                        var.get('Array').get('prototype').get('push').callprop('apply', var.get('n'), var.get('s').get('children'))
                    else:
                        var.get('n').callprop('push', var.get('s'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('o', Js(0.0))
            while (var.get('o')<var.get('n').get('length')):
                try:
                    var.put('f', var.get('A')(var.get('n'), var.get('o')))
                    if var.get('f'):
                        if (var.get('o')<var.get('n').get('length')):
                            if var.get('n').get(var.get('o')).instanceof(var.get('d').get('default').get('symbolNode')):
                                var.get('n').put(var.get('o'), PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([]).callprop('concat', var.get('n').get(var.get('o')).get('classes')), Js([var.get('n').get(var.get('o'))])))
                            var.get('c').get('default').callprop('prependChildren', var.get('n').get(var.get('o')), var.get('f'))
                        else:
                            var.get('Array').get('prototype').get('push').callprop('apply', var.get('n'), var.get('f'))
                            break
                finally:
                        (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('h', Js(0.0))
            while (var.get('h')<var.get('n').get('length')):
                try:
                    if (var.get('M')(var.get('n').get(var.get('h'))) and (var.get('z')(var.get('n').get((var.get('h')-Js(1.0))), var.get('a')) or var.get('S')(var.get('n').get((var.get('h')+Js(1.0))), var.get('a')))):
                        var.get('n').get(var.get('h')).get('classes').put('0', Js('mord'))
                finally:
                        (var.put('h',Js(var.get('h').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('v', Js(0.0))
            while (var.get('v')<var.get('n').get('length')):
                try:
                    if (PyJsStrictEq(var.get('n').get(var.get('v')).get('value'),Js('̸')) and ((var.get('v')+Js(1.0))<var.get('n').get('length'))):
                        var.put('p', var.get('n').callprop('slice', var.get('v'), (var.get('v')+Js(2.0))))
                        var.get('p').get('0').put('classes', Js([Js('mainrm')]))
                        var.get('p').get('0').get('style').put('position', Js('absolute'))
                        var.get('p').get('0').get('style').put('right', Js('0'))
                        var.put('m', var.get('n').get((var.get('v')+Js(1.0))).get('classes'))
                        var.put('g', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(var.get('m'), var.get('p')))
                        if PyJsStrictNeq(var.get('m').callprop('indexOf', Js('mord')),(-Js(1.0))):
                            var.get('g').get('style').put('paddingLeft', Js('0.277771em'))
                        var.get('g').get('style').put('position', Js('relative'))
                        var.get('n').callprop('splice', var.get('v'), Js(2.0), var.get('g'))
                finally:
                        (var.put('v',Js(var.get('v').to_number())+Js(1))-Js(1))
            return var.get('n')
        PyJs_e_306_._set_name('e')
        var.put('C', PyJs_e_306_)
        @Js
        def PyJs_e_307_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_307_}, var)
            var.registers(['t'])
            if var.get('t').instanceof(var.get('d').get('default').get('documentFragment')):
                if var.get('t').get('children').get('length'):
                    return var.get('e')(var.get('t').get('children').get((var.get('t').get('children').get('length')-Js(1.0))))
            else:
                if var.get('y').get('default').callprop('contains', Js([Js('mord'), Js('mop'), Js('mbin'), Js('mrel'), Js('mopen'), Js('mclose'), Js('mpunct'), Js('minner')]), var.get('t').get('classes').get('0')):
                    return var.get('t').get('classes').get('0')
            return var.get(u"null")
        PyJs_e_307_._set_name('e')
        var.put('T', PyJs_e_307_)
        @Js
        def PyJs_e_308_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_308_}, var)
            var.registers(['r', 'a', 'n', 't'])
            if var.get('t').get('value').get('base').neg():
                return Js(False)
            else:
                var.put('a', var.get('t').get('value').get('base'))
                if PyJsStrictEq(var.get('a').get('type'),Js('op')):
                    return (var.get('a').get('value').get('limits') and (PyJsStrictEq(var.get('r').get('style').get('size'),var.get('o').get('default').get('DISPLAY').get('size')) or var.get('a').get('value').get('alwaysHandleSupSub')))
                else:
                    if PyJsStrictEq(var.get('a').get('type'),Js('accent')):
                        return var.get('q')(var.get('a').get('value').get('base'))
                    else:
                        if PyJsStrictEq(var.get('a').get('type'),Js('horizBrace')):
                            var.put('n', (Js(False) if var.get('t').get('value').get('sub') else Js(True)))
                            return PyJsStrictEq(var.get('n'),var.get('a').get('value').get('isOver'))
                        else:
                            return var.get(u"null")
        PyJs_e_308_._set_name('e')
        var.put('N', PyJs_e_308_)
        @Js
        def PyJs_e_309_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_309_}, var)
            var.registers(['t'])
            if var.get('t').neg():
                return Js(False)
            else:
                if PyJsStrictEq(var.get('t').get('type'),Js('ordgroup')):
                    if PyJsStrictEq(var.get('t').get('value').get('length'),Js(1.0)):
                        return var.get('e')(var.get('t').get('value').get('0'))
                    else:
                        return var.get('t')
                else:
                    if PyJsStrictEq(var.get('t').get('type'),Js('color')):
                        if PyJsStrictEq(var.get('t').get('value').get('value').get('length'),Js(1.0)):
                            return var.get('e')(var.get('t').get('value').get('value').get('0'))
                        else:
                            return var.get('t')
                    else:
                        if PyJsStrictEq(var.get('t').get('type'),Js('font')):
                            return var.get('e')(var.get('t').get('value').get('body'))
                        else:
                            return var.get('t')
        PyJs_e_309_._set_name('e')
        var.put('R', PyJs_e_309_)
        @Js
        def PyJs_e_310_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_310_}, var)
            var.registers(['r', 't'])
            var.put('r', var.get('R')(var.get('t')))
            def PyJs_LONG_311_(var=var):
                return (((((((PyJsStrictEq(var.get('r').get('type'),Js('mathord')) or PyJsStrictEq(var.get('r').get('type'),Js('textord'))) or PyJsStrictEq(var.get('r').get('type'),Js('bin'))) or PyJsStrictEq(var.get('r').get('type'),Js('rel'))) or PyJsStrictEq(var.get('r').get('type'),Js('inner'))) or PyJsStrictEq(var.get('r').get('type'),Js('open'))) or PyJsStrictEq(var.get('r').get('type'),Js('close'))) or PyJsStrictEq(var.get('r').get('type'),Js('punct')))
            return PyJs_LONG_311_()
        PyJs_e_310_._set_name('e')
        var.put('q', PyJs_e_310_)
        @Js
        def PyJs_e_312_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_312_}, var)
            var.registers(['r', 'a', 't'])
            var.put('a', Js([Js('nulldelimiter')]).callprop('concat', var.get('t').callprop('baseSizingClasses')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(var.get('r').callprop('concat', var.get('a')))
        PyJs_e_312_._set_name('e')
        var.put('_', PyJs_e_312_)
        PyJs_Object_313_ = Js({})
        var.put('E', PyJs_Object_313_)
        @Js
        def PyJs_anonymous_314_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('makeOrd', var.get('e'), var.get('t'), Js('mathord'))
        PyJs_anonymous_314_._set_name('anonymous')
        var.get('E').put('mathord', PyJs_anonymous_314_)
        @Js
        def PyJs_anonymous_315_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('makeOrd', var.get('e'), var.get('t'), Js('textord'))
        PyJs_anonymous_315_._set_name('anonymous')
        var.get('E').put('textord', PyJs_anonymous_315_)
        @Js
        def PyJs_anonymous_316_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('mbin')]))
        PyJs_anonymous_316_._set_name('anonymous')
        var.get('E').put('bin', PyJs_anonymous_316_)
        @Js
        def PyJs_anonymous_317_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('mrel')]))
        PyJs_anonymous_317_._set_name('anonymous')
        var.get('E').put('rel', PyJs_anonymous_317_)
        @Js
        def PyJs_anonymous_318_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('mopen')]))
        PyJs_anonymous_318_._set_name('anonymous')
        var.get('E').put('open', PyJs_anonymous_318_)
        @Js
        def PyJs_anonymous_319_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('mclose')]))
        PyJs_anonymous_319_._set_name('anonymous')
        var.get('E').put('close', PyJs_anonymous_319_)
        @Js
        def PyJs_anonymous_320_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('minner')]))
        PyJs_anonymous_320_._set_name('anonymous')
        var.get('E').put('inner', PyJs_anonymous_320_)
        @Js
        def PyJs_anonymous_321_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'), Js([Js('mpunct')]))
        PyJs_anonymous_321_._set_name('anonymous')
        var.get('E').put('punct', PyJs_anonymous_321_)
        @Js
        def PyJs_anonymous_322_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord')]), var.get('C')(var.get('e').get('value'), var.get('t'), Js(True)), var.get('t'))
        PyJs_anonymous_322_._set_name('anonymous')
        var.get('E').put('ordgroup', PyJs_anonymous_322_)
        @Js
        def PyJs_anonymous_323_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').callprop('withFont', var.get('e').get('value').get('style')))
            var.put('a', var.get('C')(var.get('e').get('value').get('body'), var.get('r'), Js(True)))
            #for JS loop
            var.put('n', Js(0.0))
            while (var.get('n')<(var.get('a').get('length')-Js(1.0))):
                try:
                    if var.get('a').get(var.get('n')).callprop('tryCombine', var.get('a').get((var.get('n')+Js(1.0)))):
                        var.get('a').callprop('splice', (var.get('n')+Js(1.0)), Js(1.0))
                        (var.put('n',Js(var.get('n').to_number())-Js(1))+Js(1))
                finally:
                        (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('text')]), var.get('a'), var.get('r'))
        PyJs_anonymous_323_._set_name('anonymous')
        var.get('E').put('text', PyJs_anonymous_323_)
        @Js
        def PyJs_anonymous_324_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('C')(var.get('e').get('value').get('value'), var.get('t').callprop('withColor', var.get('e').get('value').get('color')), Js(False)))
            return var.get('c').get('default').get('makeFragment').create(var.get('r'))
        PyJs_anonymous_324_._set_name('anonymous')
        var.get('E').put('color', PyJs_anonymous_324_)
        @Js
        def PyJs_anonymous_325_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'm', 'b', 'i', 'h', 'l', 'r', 'v', 'w', 'x', 'g', 'n', 's', 'e', 'a', 'y', 'f', 't'])
            if var.get('N')(var.get('e'), var.get('t')):
                return var.get('E').callprop(var.get('e').get('value').get('base').get('type'), var.get('e'), var.get('t'))
            var.put('r', var.get('L')(var.get('e').get('value').get('base'), var.get('t')))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            var.put('i', var.get('t').callprop('fontMetrics'))
            var.put('l', PyJsComma(Js(0.0), Js(None)))
            var.put('s', Js(0.0))
            var.put('f', Js(0.0))
            if var.get('e').get('value').get('sup'):
                var.put('l', var.get('t').callprop('havingStyle', var.get('t').get('style').callprop('sup')))
                var.put('a', var.get('L')(var.get('e').get('value').get('sup'), var.get('l'), var.get('t')))
                if var.get('q')(var.get('e').get('value').get('base')).neg():
                    var.put('s', (var.get('r').get('height')-((var.get('l').callprop('fontMetrics').get('supDrop')*var.get('l').get('sizeMultiplier'))/var.get('t').get('sizeMultiplier'))))
            if var.get('e').get('value').get('sub'):
                var.put('l', var.get('t').callprop('havingStyle', var.get('t').get('style').callprop('sub')))
                var.put('n', var.get('L')(var.get('e').get('value').get('sub'), var.get('l'), var.get('t')))
                if var.get('q')(var.get('e').get('value').get('base')).neg():
                    var.put('f', (var.get('r').get('depth')+((var.get('l').callprop('fontMetrics').get('subDrop')*var.get('l').get('sizeMultiplier'))/var.get('t').get('sizeMultiplier'))))
            var.put('h', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('t').get('style'),var.get('o').get('default').get('DISPLAY')):
                var.put('h', var.get('i').get('sup1'))
            else:
                if var.get('t').get('style').get('cramped'):
                    var.put('h', var.get('i').get('sup3'))
                else:
                    var.put('h', var.get('i').get('sup2'))
            var.put('v', var.get('t').get('sizeMultiplier'))
            var.put('p', (((Js(0.5)/var.get('i').get('ptPerEm'))/var.get('v'))+Js('em')))
            var.put('m', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('sup').neg():
                var.put('f', var.get('Math').callprop('max', var.get('f'), var.get('i').get('sub1'), (var.get('n').get('height')-(Js(0.8)*var.get('i').get('xHeight')))))
                PyJs_Object_326_ = Js({'type':Js('elem'),'elem':var.get('n'),'marginRight':var.get('p')})
                var.put('g', Js([PyJs_Object_326_]))
                if var.get('r').instanceof(var.get('d').get('default').get('symbolNode')):
                    var.get('g').get('0').put('marginLeft', ((-var.get('r').get('italic'))+Js('em')))
                var.put('m', var.get('c').get('default').callprop('makeVList', var.get('g'), Js('shift'), var.get('f'), var.get('t')))
            else:
                if var.get('e').get('value').get('sub').neg():
                    var.put('s', var.get('Math').callprop('max', var.get('s'), var.get('h'), (var.get('a').get('depth')+(Js(0.25)*var.get('i').get('xHeight')))))
                    PyJs_Object_327_ = Js({'type':Js('elem'),'elem':var.get('a'),'marginRight':var.get('p')})
                    var.put('m', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_327_]), Js('shift'), (-var.get('s')), var.get('t')))
                else:
                    var.put('s', var.get('Math').callprop('max', var.get('s'), var.get('h'), (var.get('a').get('depth')+(Js(0.25)*var.get('i').get('xHeight')))))
                    var.put('f', var.get('Math').callprop('max', var.get('f'), var.get('i').get('sub2')))
                    var.put('y', var.get('i').get('defaultRuleThickness'))
                    if (((var.get('s')-var.get('a').get('depth'))-(var.get('n').get('height')-var.get('f')))<(Js(4.0)*var.get('y'))):
                        var.put('f', (((Js(4.0)*var.get('y'))-(var.get('s')-var.get('a').get('depth')))+var.get('n').get('height')))
                        var.put('x', ((Js(0.8)*var.get('i').get('xHeight'))-(var.get('s')-var.get('a').get('depth'))))
                        if (var.get('x')>Js(0.0)):
                            var.put('s', var.get('x'), '+')
                            var.put('f', var.get('x'), '-')
                    PyJs_Object_328_ = Js({'type':Js('elem'),'elem':var.get('n'),'shift':var.get('f'),'marginRight':var.get('p')})
                    PyJs_Object_329_ = Js({'type':Js('elem'),'elem':var.get('a'),'shift':(-var.get('s')),'marginRight':var.get('p')})
                    var.put('w', Js([PyJs_Object_328_, PyJs_Object_329_]))
                    if var.get('r').instanceof(var.get('d').get('default').get('symbolNode')):
                        var.get('w').get('0').put('marginLeft', ((-var.get('r').get('italic'))+Js('em')))
                    var.put('m', var.get('c').get('default').callprop('makeVList', var.get('w'), Js('individualShift'), var.get(u"null"), var.get('t')))
            var.put('b', (var.get('T')(var.get('r')) or Js('mord')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([var.get('b')]), Js([var.get('r'), PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('msupsub')]), Js([var.get('m')]))]), var.get('t'))
        PyJs_anonymous_325_._set_name('anonymous')
        var.get('E').put('supsub', PyJs_anonymous_325_)
        @Js
        def PyJs_anonymous_330_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'y', 'i', 'v', 'w', 'x', 'e', 'a', 'b', 'l', 'g', 'z', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
            var.put('r', var.get('t').get('style'))
            if PyJsStrictEq(var.get('e').get('value').get('size'),Js('display')):
                var.put('r', var.get('o').get('default').get('DISPLAY'))
            else:
                if PyJsStrictEq(var.get('e').get('value').get('size'),Js('text')):
                    var.put('r', var.get('o').get('default').get('TEXT'))
            var.put('a', var.get('r').callprop('fracNum'))
            var.put('n', var.get('r').callprop('fracDen'))
            var.put('i', PyJsComma(Js(0.0), Js(None)))
            var.put('i', var.get('t').callprop('havingStyle', var.get('a')))
            var.put('l', var.get('L')(var.get('e').get('value').get('numer'), var.get('i'), var.get('t')))
            var.put('i', var.get('t').callprop('havingStyle', var.get('n')))
            var.put('s', var.get('L')(var.get('e').get('value').get('denom'), var.get('i'), var.get('t')))
            var.put('f', PyJsComma(Js(0.0), Js(None)))
            var.put('v', PyJsComma(Js(0.0), Js(None)))
            var.put('d', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('hasBarLine'):
                var.put('f', var.get('B')(Js('frac-line'), var.get('t')))
                var.put('v', var.get('f').get('height'))
                var.put('d', var.get('f').get('height'))
            else:
                var.put('f', var.get(u"null"))
                var.put('v', Js(0.0))
                var.put('d', var.get('t').callprop('fontMetrics').get('defaultRuleThickness'))
            var.put('p', PyJsComma(Js(0.0), Js(None)))
            var.put('m', PyJsComma(Js(0.0), Js(None)))
            var.put('g', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('r').get('size'),var.get('o').get('default').get('DISPLAY').get('size')):
                var.put('p', var.get('t').callprop('fontMetrics').get('num1'))
                if (var.get('v')>Js(0.0)):
                    var.put('m', (Js(3.0)*var.get('d')))
                else:
                    var.put('m', (Js(7.0)*var.get('d')))
                var.put('g', var.get('t').callprop('fontMetrics').get('denom1'))
            else:
                if (var.get('v')>Js(0.0)):
                    var.put('p', var.get('t').callprop('fontMetrics').get('num2'))
                    var.put('m', var.get('d'))
                else:
                    var.put('p', var.get('t').callprop('fontMetrics').get('num3'))
                    var.put('m', (Js(3.0)*var.get('d')))
                var.put('g', var.get('t').callprop('fontMetrics').get('denom2'))
            var.put('y', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('v'),Js(0.0)):
                var.put('x', ((var.get('p')-var.get('l').get('depth'))-(var.get('s').get('height')-var.get('g'))))
                if (var.get('x')<var.get('m')):
                    var.put('p', (Js(0.5)*(var.get('m')-var.get('x'))), '+')
                    var.put('g', (Js(0.5)*(var.get('m')-var.get('x'))), '+')
                PyJs_Object_331_ = Js({'type':Js('elem'),'elem':var.get('s'),'shift':var.get('g')})
                PyJs_Object_332_ = Js({'type':Js('elem'),'elem':var.get('l'),'shift':(-var.get('p'))})
                var.put('y', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_331_, PyJs_Object_332_]), Js('individualShift'), var.get(u"null"), var.get('t')))
            else:
                var.put('w', var.get('t').callprop('fontMetrics').get('axisHeight'))
                if (((var.get('p')-var.get('l').get('depth'))-(var.get('w')+(Js(0.5)*var.get('v'))))<var.get('m')):
                    var.put('p', (var.get('m')-((var.get('p')-var.get('l').get('depth'))-(var.get('w')+(Js(0.5)*var.get('v'))))), '+')
                if (((var.get('w')-(Js(0.5)*var.get('v')))-(var.get('s').get('height')-var.get('g')))<var.get('m')):
                    var.put('g', (var.get('m')-((var.get('w')-(Js(0.5)*var.get('v')))-(var.get('s').get('height')-var.get('g')))), '+')
                var.put('b', (-(var.get('w')-(Js(0.5)*var.get('v')))))
                PyJs_Object_333_ = Js({'type':Js('elem'),'elem':var.get('s'),'shift':var.get('g')})
                PyJs_Object_334_ = Js({'type':Js('elem'),'elem':var.get('f'),'shift':var.get('b')})
                PyJs_Object_335_ = Js({'type':Js('elem'),'elem':var.get('l'),'shift':(-var.get('p'))})
                var.put('y', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_333_, PyJs_Object_334_, PyJs_Object_335_]), Js('individualShift'), var.get(u"null"), var.get('t')))
            var.put('i', var.get('t').callprop('havingStyle', var.get('r')))
            var.get('y').put('height', (var.get('i').get('sizeMultiplier')/var.get('t').get('sizeMultiplier')), '*')
            var.get('y').put('depth', (var.get('i').get('sizeMultiplier')/var.get('t').get('sizeMultiplier')), '*')
            var.put('k', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('r').get('size'),var.get('o').get('default').get('DISPLAY').get('size')):
                var.put('k', var.get('t').callprop('fontMetrics').get('delim1'))
            else:
                var.put('k', var.get('t').callprop('fontMetrics').get('delim2'))
            var.put('M', PyJsComma(Js(0.0), Js(None)))
            var.put('z', PyJsComma(Js(0.0), Js(None)))
            if (var.get('e').get('value').get('leftDelim')==var.get(u"null")):
                var.put('M', var.get('_')(var.get('t'), Js([Js('mopen')])))
            else:
                var.put('M', var.get('h').get('default').callprop('customSizedDelim', var.get('e').get('value').get('leftDelim'), var.get('k'), Js(True), var.get('t').callprop('havingStyle', var.get('r')), var.get('e').get('mode'), Js([Js('mopen')])))
            if (var.get('e').get('value').get('rightDelim')==var.get(u"null")):
                var.put('z', var.get('_')(var.get('t'), Js([Js('mclose')])))
            else:
                var.put('z', var.get('h').get('default').callprop('customSizedDelim', var.get('e').get('value').get('rightDelim'), var.get('k'), Js(True), var.get('t').callprop('havingStyle', var.get('r')), var.get('e').get('mode'), Js([Js('mclose')])))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord')]).callprop('concat', var.get('i').callprop('sizingClasses', var.get('t'))), Js([var.get('M'), PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mfrac')]), Js([var.get('y')])), var.get('z')]), var.get('t'))
        PyJs_anonymous_330_._set_name('anonymous')
        var.get('E').put('genfrac', PyJs_anonymous_330_)
        @Js
        def PyJs_anonymous_336_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['B', 'R', 'q', 'E', 'r', 'D', 'o', 'T', 'N', 'H', 'i', 'h', 'v', 'w', 'x', 'F', 'e', 'a', 'A', 'S', 'O', '_', 'b', 'P', 'C', 'g', 'z', 'M', 'k', 't', 'p', 'd', 'n', 's', 'f'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            var.put('n', var.get('e').get('value').get('body').get('length'))
            var.put('i', Js(0.0))
            var.put('s', var.get('Array').create(var.get('n')))
            var.put('o', (Js(1.0)/var.get('t').callprop('fontMetrics').get('ptPerEm')))
            var.put('f', (Js(5.0)*var.get('o')))
            var.put('h', (Js(12.0)*var.get('o')))
            var.put('v', (Js(3.0)*var.get('o')))
            var.put('d', var.get('y').get('default').callprop('deflt', var.get('e').get('value').get('arraystretch'), Js(1.0)))
            var.put('p', (var.get('d')*var.get('h')))
            var.put('g', (Js(0.7)*var.get('p')))
            var.put('x', (Js(0.3)*var.get('p')))
            var.put('w', Js(0.0))
            #for JS loop
            var.put('r', Js(0.0))
            while (var.get('r')<var.get('e').get('value').get('body').get('length')):
                try:
                    var.put('b', var.get('e').get('value').get('body').get(var.get('r')))
                    var.put('k', var.get('g'))
                    var.put('M', var.get('x'))
                    if (var.get('i')<var.get('b').get('length')):
                        var.put('i', var.get('b').get('length'))
                    var.put('z', var.get('Array').create(var.get('b').get('length')))
                    #for JS loop
                    var.put('a', Js(0.0))
                    while (var.get('a')<var.get('b').get('length')):
                        try:
                            var.put('S', var.get('L')(var.get('b').get(var.get('a')), var.get('t')))
                            if (var.get('M')<var.get('S').get('depth')):
                                var.put('M', var.get('S').get('depth'))
                            if (var.get('k')<var.get('S').get('height')):
                                var.put('k', var.get('S').get('height'))
                            var.get('z').put(var.get('a'), var.get('S'))
                        finally:
                                var.put('a',Js(var.get('a').to_number())+Js(1))
                    var.put('A', Js(0.0))
                    if var.get('e').get('value').get('rowGaps').get(var.get('r')):
                        var.put('A', var.get('m').get('default').callprop('calculateSize', var.get('e').get('value').get('rowGaps').get(var.get('r')).get('value'), var.get('t')))
                        if (var.get('A')>Js(0.0)):
                            var.put('A', var.get('x'), '+')
                            if (var.get('M')<var.get('A')):
                                var.put('M', var.get('A'))
                            var.put('A', Js(0.0))
                    if var.get('e').get('value').get('addJot'):
                        var.put('M', var.get('v'), '+')
                    var.get('z').put('height', var.get('k'))
                    var.get('z').put('depth', var.get('M'))
                    var.put('w', var.get('k'), '+')
                    var.get('z').put('pos', var.get('w'))
                    var.put('w', (var.get('M')+var.get('A')), '+')
                    var.get('s').put(var.get('r'), var.get('z'))
                finally:
                        var.put('r',Js(var.get('r').to_number())+Js(1))
            var.put('C', ((var.get('w')/Js(2.0))+var.get('t').callprop('fontMetrics').get('axisHeight')))
            var.put('T', (var.get('e').get('value').get('cols') or Js([])))
            var.put('N', Js([]))
            var.put('R', PyJsComma(Js(0.0), Js(None)))
            var.put('q', PyJsComma(Js(0.0), Js(None)))
            #for JS loop
            PyJsComma(var.put('a', Js(0.0)),var.put('q', Js(0.0)))
            while ((var.get('a')<var.get('i')) or (var.get('q')<var.get('T').get('length'))):
                try:
                    PyJs_Object_337_ = Js({})
                    var.put('_', (var.get('T').get(var.get('q')) or PyJs_Object_337_))
                    var.put('E', Js(True))
                    while PyJsStrictEq(var.get('_').get('type'),Js('separator')):
                        if var.get('E').neg():
                            var.put('R', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('arraycolsep')]), Js([])))
                            var.get('R').get('style').put('width', (var.get('t').callprop('fontMetrics').get('doubleRuleSep')+Js('em')))
                            var.get('N').callprop('push', var.get('R'))
                        if PyJsStrictEq(var.get('_').get('separator'),Js('|')):
                            var.put('B', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('vertical-separator')]), Js([])))
                            var.get('B').get('style').put('height', (var.get('w')+Js('em')))
                            var.get('B').get('style').put('verticalAlign', ((-(var.get('w')-var.get('C')))+Js('em')))
                            var.get('N').callprop('push', var.get('B'))
                        else:
                            PyJsTempException = JsToPyException(var.get('l').get('default').create((Js('Invalid separator type: ')+var.get('_').get('separator'))))
                            raise PyJsTempException
                        (var.put('q',Js(var.get('q').to_number())+Js(1))-Js(1))
                        PyJs_Object_338_ = Js({})
                        var.put('_', (var.get('T').get(var.get('q')) or PyJs_Object_338_))
                        var.put('E', Js(False))
                    if (var.get('a')>=var.get('i')):
                        continue
                    var.put('O', PyJsComma(Js(0.0), Js(None)))
                    if ((var.get('a')>Js(0.0)) or var.get('e').get('value').get('hskipBeforeAndAfter')):
                        var.put('O', var.get('y').get('default').callprop('deflt', var.get('_').get('pregap'), var.get('f')))
                        if PyJsStrictNeq(var.get('O'),Js(0.0)):
                            var.put('R', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('arraycolsep')]), Js([])))
                            var.get('R').get('style').put('width', (var.get('O')+Js('em')))
                            var.get('N').callprop('push', var.get('R'))
                    var.put('P', Js([]))
                    #for JS loop
                    var.put('r', Js(0.0))
                    while (var.get('r')<var.get('n')):
                        try:
                            var.put('F', var.get('s').get(var.get('r')))
                            var.put('H', var.get('F').get(var.get('a')))
                            if var.get('H').neg():
                                continue
                            var.put('D', (var.get('F').get('pos')-var.get('C')))
                            var.get('H').put('depth', var.get('F').get('depth'))
                            var.get('H').put('height', var.get('F').get('height'))
                            PyJs_Object_339_ = Js({'type':Js('elem'),'elem':var.get('H'),'shift':var.get('D')})
                            var.get('P').callprop('push', PyJs_Object_339_)
                        finally:
                                var.put('r',Js(var.get('r').to_number())+Js(1))
                    var.put('P', var.get('c').get('default').callprop('makeVList', var.get('P'), Js('individualShift'), var.get(u"null"), var.get('t')))
                    var.put('P', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([(Js('col-align-')+(var.get('_').get('align') or Js('c')))]), Js([var.get('P')])))
                    var.get('N').callprop('push', var.get('P'))
                    if ((var.get('a')<(var.get('i')-Js(1.0))) or var.get('e').get('value').get('hskipBeforeAndAfter')):
                        var.put('O', var.get('y').get('default').callprop('deflt', var.get('_').get('postgap'), var.get('f')))
                        if PyJsStrictNeq(var.get('O'),Js(0.0)):
                            var.put('R', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('arraycolsep')]), Js([])))
                            var.get('R').get('style').put('width', (var.get('O')+Js('em')))
                            var.get('N').callprop('push', var.get('R'))
                finally:
                        PyJsComma(var.put('a',Js(var.get('a').to_number())+Js(1)),var.put('q',Js(var.get('q').to_number())+Js(1)))
            var.put('s', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mtable')]), var.get('N')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord')]), Js([var.get('s')]), var.get('t'))
        PyJs_anonymous_336_._set_name('anonymous')
        var.get('E').put('array', PyJs_anonymous_336_)
        @Js
        def PyJs_anonymous_340_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            if (((PyJsStrictEq(var.get('e').get('value'),Js('\\ ')) or PyJsStrictEq(var.get('e').get('value'),Js('\\space'))) or PyJsStrictEq(var.get('e').get('value'),Js(' '))) or PyJsStrictEq(var.get('e').get('value'),Js('~'))):
                if PyJsStrictEq(var.get('e').get('mode'),Js('text')):
                    return var.get('c').get('default').callprop('makeOrd', var.get('e'), var.get('t'), Js('textord'))
                else:
                    return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace')]), Js([var.get('c').get('default').callprop('mathsym', var.get('e').get('value'), var.get('e').get('mode'), var.get('t'))]), var.get('t'))
            else:
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), var.get('c').get('default').get('spacingFunctions').get(var.get('e').get('value')).get('className')]), Js([]), var.get('t'))
        PyJs_anonymous_340_._set_name('anonymous')
        var.get('E').put('spacing', PyJs_anonymous_340_)
        @Js
        def PyJs_anonymous_341_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('inner')]), Js([var.get('L')(var.get('e').get('value').get('body'), var.get('t'))])))
            var.put('a', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('fix')]), Js([])))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('llap')]), Js([var.get('r'), var.get('a')]), var.get('t'))
        PyJs_anonymous_341_._set_name('anonymous')
        var.get('E').put('llap', PyJs_anonymous_341_)
        @Js
        def PyJs_anonymous_342_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('inner')]), Js([var.get('L')(var.get('e').get('value').get('body'), var.get('t'))])))
            var.put('a', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('fix')]), Js([])))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('rlap')]), Js([var.get('r'), var.get('a')]), var.get('t'))
        PyJs_anonymous_342_._set_name('anonymous')
        var.get('E').put('rlap', PyJs_anonymous_342_)
        @Js
        def PyJs_anonymous_343_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'T', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'b', 'l', 'g', 'z', 'M', 'k', 't', 'p', 'm', 'n', 's', 'f'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            var.put('n', Js(False))
            if PyJsStrictEq(var.get('e').get('type'),Js('supsub')):
                var.put('r', var.get('e').get('value').get('sup'))
                var.put('a', var.get('e').get('value').get('sub'))
                var.put('e', var.get('e').get('value').get('base'))
                var.put('n', Js(True))
            var.put('i', var.get('t').get('style'))
            var.put('l', Js([Js('\\smallint')]))
            var.put('s', Js(False))
            if ((PyJsStrictEq(var.get('i').get('size'),var.get('o').get('default').get('DISPLAY').get('size')) and var.get('e').get('value').get('symbol')) and var.get('y').get('default').callprop('contains', var.get('l'), var.get('e').get('value').get('body')).neg()):
                var.put('s', Js(True))
            var.put('f', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('symbol'):
                var.put('h', (Js('Size2-Regular') if var.get('s') else Js('Size1-Regular')))
                var.put('f', var.get('c').get('default').callprop('makeSymbol', var.get('e').get('value').get('body'), var.get('h'), Js('math'), var.get('t'), Js([Js('mop'), Js('op-symbol'), (Js('large-op') if var.get('s') else Js('small-op'))])))
            else:
                if var.get('e').get('value').get('value'):
                    var.put('v', var.get('C')(var.get('e').get('value').get('value'), var.get('t'), Js(True)))
                    if (PyJsStrictEq(var.get('v').get('length'),Js(1.0)) and var.get('v').get('0').instanceof(var.get('d').get('default').get('symbolNode'))):
                        var.put('f', var.get('v').get('0'))
                        var.get('f').get('classes').put('0', Js('mop'))
                    else:
                        var.put('f', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mop')]), var.get('v'), var.get('t')))
                else:
                    var.put('p', Js([]))
                    #for JS loop
                    var.put('m', Js(1.0))
                    while (var.get('m')<var.get('e').get('value').get('body').get('length')):
                        try:
                            var.get('p').callprop('push', var.get('c').get('default').callprop('mathsym', var.get('e').get('value').get('body').get(var.get('m')), var.get('e').get('mode')))
                        finally:
                                (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))
                    var.put('f', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mop')]), var.get('p'), var.get('t')))
            var.put('g', Js(0.0))
            var.put('x', Js(0.0))
            if var.get('f').instanceof(var.get('d').get('default').get('symbolNode')):
                var.put('g', (((var.get('f').get('height')-var.get('f').get('depth'))/Js(2.0))-var.get('t').callprop('fontMetrics').get('axisHeight')))
                var.put('x', var.get('f').get('italic'))
            if var.get('n'):
                var.put('f', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([]), Js([var.get('f')])))
                var.put('w', PyJsComma(Js(0.0), Js(None)))
                var.put('b', PyJsComma(Js(0.0), Js(None)))
                var.put('k', PyJsComma(Js(0.0), Js(None)))
                var.put('M', PyJsComma(Js(0.0), Js(None)))
                var.put('z', PyJsComma(Js(0.0), Js(None)))
                if var.get('r'):
                    var.put('z', var.get('t').callprop('havingStyle', var.get('i').callprop('sup')))
                    var.put('w', var.get('L')(var.get('r'), var.get('z'), var.get('t')))
                    var.put('b', var.get('Math').callprop('max', var.get('t').callprop('fontMetrics').get('bigOpSpacing1'), (var.get('t').callprop('fontMetrics').get('bigOpSpacing3')-var.get('w').get('depth'))))
                if var.get('a'):
                    var.put('z', var.get('t').callprop('havingStyle', var.get('i').callprop('sub')))
                    var.put('k', var.get('L')(var.get('a'), var.get('z'), var.get('t')))
                    var.put('M', var.get('Math').callprop('max', var.get('t').callprop('fontMetrics').get('bigOpSpacing2'), (var.get('t').callprop('fontMetrics').get('bigOpSpacing4')-var.get('k').get('height'))))
                var.put('S', PyJsComma(Js(0.0), Js(None)))
                var.put('A', PyJsComma(Js(0.0), Js(None)))
                var.put('T', PyJsComma(Js(0.0), Js(None)))
                if var.get('r').neg():
                    var.put('A', (var.get('f').get('height')-var.get('g')))
                    PyJs_Object_344_ = Js({'type':Js('kern'),'size':var.get('t').callprop('fontMetrics').get('bigOpSpacing5')})
                    PyJs_Object_345_ = Js({'type':Js('elem'),'elem':var.get('k'),'marginLeft':((-var.get('x'))+Js('em'))})
                    PyJs_Object_346_ = Js({'type':Js('kern'),'size':var.get('M')})
                    PyJs_Object_347_ = Js({'type':Js('elem'),'elem':var.get('f')})
                    var.put('S', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_344_, PyJs_Object_345_, PyJs_Object_346_, PyJs_Object_347_]), Js('top'), var.get('A'), var.get('t')))
                else:
                    if var.get('a').neg():
                        var.put('T', (var.get('f').get('depth')+var.get('g')))
                        PyJs_Object_348_ = Js({'type':Js('elem'),'elem':var.get('f')})
                        PyJs_Object_349_ = Js({'type':Js('kern'),'size':var.get('b')})
                        PyJs_Object_350_ = Js({'type':Js('elem'),'elem':var.get('w'),'marginLeft':(var.get('x')+Js('em'))})
                        PyJs_Object_351_ = Js({'type':Js('kern'),'size':var.get('t').callprop('fontMetrics').get('bigOpSpacing5')})
                        var.put('S', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_348_, PyJs_Object_349_, PyJs_Object_350_, PyJs_Object_351_]), Js('bottom'), var.get('T'), var.get('t')))
                    else:
                        if (var.get('r').neg() and var.get('a').neg()):
                            return var.get('f')
                        else:
                            var.put('T', (((((var.get('t').callprop('fontMetrics').get('bigOpSpacing5')+var.get('k').get('height'))+var.get('k').get('depth'))+var.get('M'))+var.get('f').get('depth'))+var.get('g')))
                            PyJs_Object_352_ = Js({'type':Js('kern'),'size':var.get('t').callprop('fontMetrics').get('bigOpSpacing5')})
                            PyJs_Object_353_ = Js({'type':Js('elem'),'elem':var.get('k'),'marginLeft':((-var.get('x'))+Js('em'))})
                            PyJs_Object_354_ = Js({'type':Js('kern'),'size':var.get('M')})
                            PyJs_Object_355_ = Js({'type':Js('elem'),'elem':var.get('f')})
                            PyJs_Object_356_ = Js({'type':Js('kern'),'size':var.get('b')})
                            PyJs_Object_357_ = Js({'type':Js('elem'),'elem':var.get('w'),'marginLeft':(var.get('x')+Js('em'))})
                            PyJs_Object_358_ = Js({'type':Js('kern'),'size':var.get('t').callprop('fontMetrics').get('bigOpSpacing5')})
                            var.put('S', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_352_, PyJs_Object_353_, PyJs_Object_354_, PyJs_Object_355_, PyJs_Object_356_, PyJs_Object_357_, PyJs_Object_358_]), Js('bottom'), var.get('T'), var.get('t')))
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mop'), Js('op-limits')]), Js([var.get('S')]), var.get('t'))
            else:
                if var.get('g'):
                    var.get('f').get('style').put('position', Js('relative'))
                    var.get('f').get('style').put('top', (var.get('g')+Js('em')))
                return var.get('f')
        PyJs_anonymous_343_._set_name('anonymous')
        var.get('E').put('op', PyJs_anonymous_343_)
        @Js
        def PyJs_anonymous_359_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', Js([]))
            if PyJsStrictEq(var.get('e').get('value').get('modType'),Js('bmod')):
                if var.get('t').get('style').callprop('isTight').neg():
                    var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('negativemediumspace')]), Js([]), var.get('t')))
                var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('thickspace')]), Js([]), var.get('t')))
            else:
                if PyJsStrictEq(var.get('t').get('style').get('size'),var.get('o').get('default').get('DISPLAY').get('size')):
                    var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('quad')]), Js([]), var.get('t')))
                else:
                    if PyJsStrictEq(var.get('e').get('value').get('modType'),Js('mod')):
                        var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('twelvemuspace')]), Js([]), var.get('t')))
                    else:
                        var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('eightmuspace')]), Js([]), var.get('t')))
            if (PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pod')) or PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pmod'))):
                var.get('r').callprop('push', var.get('c').get('default').callprop('mathsym', Js('('), var.get('e').get('mode')))
            if PyJsStrictNeq(var.get('e').get('value').get('modType'),Js('pod')):
                var.put('a', Js([var.get('c').get('default').callprop('mathsym', Js('m'), var.get('e').get('mode')), var.get('c').get('default').callprop('mathsym', Js('o'), var.get('e').get('mode')), var.get('c').get('default').callprop('mathsym', Js('d'), var.get('e').get('mode'))]))
                if PyJsStrictEq(var.get('e').get('value').get('modType'),Js('bmod')):
                    var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mbin')]), var.get('a'), var.get('t')))
                    var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('thickspace')]), Js([]), var.get('t')))
                    if var.get('t').get('style').callprop('isTight').neg():
                        var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('negativemediumspace')]), Js([]), var.get('t')))
                else:
                    var.get('Array').get('prototype').get('push').callprop('apply', var.get('r'), var.get('a'))
                    var.get('r').callprop('push', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mspace'), Js('sixmuspace')]), Js([]), var.get('t')))
            if var.get('e').get('value').get('value'):
                var.get('Array').get('prototype').get('push').callprop('apply', var.get('r'), var.get('C')(var.get('e').get('value').get('value'), var.get('t'), Js(False)))
            if (PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pod')) or PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pmod'))):
                var.get('r').callprop('push', var.get('c').get('default').callprop('mathsym', Js(')'), var.get('e').get('mode')))
            return var.get('c').get('default').callprop('makeFragment', var.get('r'))
        PyJs_anonymous_359_._set_name('anonymous')
        var.get('E').put('mod', PyJs_anonymous_359_)
        @Js
        def PyJs_anonymous_360_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('k')]), Js([var.get('c').get('default').callprop('mathsym', Js('K'), var.get('e').get('mode'))]), var.get('t')))
            var.put('a', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('a')]), Js([var.get('c').get('default').callprop('mathsym', Js('A'), var.get('e').get('mode'))]), var.get('t')))
            var.get('a').put('height', ((var.get('a').get('height')+Js(0.2))*Js(0.75)))
            var.get('a').put('depth', ((var.get('a').get('height')-Js(0.2))*Js(0.75)))
            var.put('n', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('t')]), Js([var.get('c').get('default').callprop('mathsym', Js('T'), var.get('e').get('mode'))]), var.get('t')))
            var.put('i', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('e')]), Js([var.get('c').get('default').callprop('mathsym', Js('E'), var.get('e').get('mode'))]), var.get('t')))
            var.get('i').put('height', (var.get('i').get('height')-Js(0.2155)))
            var.get('i').put('depth', (var.get('i').get('depth')+Js(0.2155)))
            var.put('l', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('x')]), Js([var.get('c').get('default').callprop('mathsym', Js('X'), var.get('e').get('mode'))]), var.get('t')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('katex-logo')]), Js([var.get('r'), var.get('a'), var.get('n'), var.get('i'), var.get('l')]), var.get('t'))
        PyJs_anonymous_360_._set_name('anonymous')
        var.get('E').put('katex', PyJs_anonymous_360_)
        @Js
        def PyJs_e_361_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_361_}, var)
            var.registers(['r', 'a', 'n', 't'])
            var.put('n', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([var.get('t')]), Js([]), var.get('r')))
            var.get('n').put('height', (var.get('a') or var.get('r').callprop('fontMetrics').get('defaultRuleThickness')))
            var.get('n').get('style').put('borderBottomWidth', (var.get('n').get('height')+Js('em')))
            var.get('n').put('maxFontSize', Js(1.0))
            return var.get('n')
        PyJs_e_361_._set_name('e')
        var.put('B', PyJs_e_361_)
        @Js
        def PyJs_anonymous_362_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('L')(var.get('e').get('value').get('body'), var.get('t').callprop('havingCrampedStyle')))
            var.put('a', var.get('B')(Js('overline-line'), var.get('t')))
            PyJs_Object_363_ = Js({'type':Js('elem'),'elem':var.get('r')})
            PyJs_Object_364_ = Js({'type':Js('kern'),'size':(Js(3.0)*var.get('a').get('height'))})
            PyJs_Object_365_ = Js({'type':Js('elem'),'elem':var.get('a')})
            PyJs_Object_366_ = Js({'type':Js('kern'),'size':var.get('a').get('height')})
            var.put('n', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_363_, PyJs_Object_364_, PyJs_Object_365_, PyJs_Object_366_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('overline')]), Js([var.get('n')]), var.get('t'))
        PyJs_anonymous_362_._set_name('anonymous')
        var.get('E').put('overline', PyJs_anonymous_362_)
        @Js
        def PyJs_anonymous_367_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('L')(var.get('e').get('value').get('body'), var.get('t')))
            var.put('a', var.get('B')(Js('underline-line'), var.get('t')))
            PyJs_Object_368_ = Js({'type':Js('kern'),'size':var.get('a').get('height')})
            PyJs_Object_369_ = Js({'type':Js('elem'),'elem':var.get('a')})
            PyJs_Object_370_ = Js({'type':Js('kern'),'size':(Js(3.0)*var.get('a').get('height'))})
            PyJs_Object_371_ = Js({'type':Js('elem'),'elem':var.get('r')})
            var.put('n', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_368_, PyJs_Object_369_, PyJs_Object_370_, PyJs_Object_371_]), Js('top'), var.get('r').get('height'), var.get('t')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('underline')]), Js([var.get('n')]), var.get('t'))
        PyJs_anonymous_367_._set_name('anonymous')
        var.get('E').put('underline', PyJs_anonymous_367_)
        @Js
        def PyJs_anonymous_372_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'm', 'b', 'i', 'l', 'r', 'v', 'w', 'x', 'g', 'n', 's', 'e', 'a', 'k', 'y', 'f', 't'])
            var.put('r', var.get('L')(var.get('e').get('value').get('body'), var.get('t').callprop('havingCrampedStyle')))
            if var.get('r').instanceof(var.get('d').get('default').get('documentFragment')):
                var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([]), Js([var.get('r')]), var.get('t')))
            var.put('a', var.get('t').callprop('fontMetrics'))
            var.put('n', var.get('a').get('defaultRuleThickness'))
            var.put('i', var.get('n'))
            if (var.get('t').get('style').get('id')<var.get('o').get('default').get('TEXT').get('id')):
                var.put('i', var.get('t').callprop('fontMetrics').get('xHeight'))
            var.put('l', (var.get('n')+(var.get('i')/Js(4.0))))
            var.put('s', ((((var.get('r').get('height')+var.get('r').get('depth'))+var.get('l'))+var.get('n'))*var.get('t').get('sizeMultiplier')))
            var.put('f', var.get('h').get('default').callprop('customSizedDelim', Js('\\surd'), var.get('s'), Js(False), var.get('t'), var.get('e').get('mode')))
            var.put('v', (var.get('t').callprop('fontMetrics').get('sqrtRuleThickness')*var.get('f').get('sizeMultiplier')))
            var.put('p', (var.get('f').get('height')-var.get('v')))
            if (var.get('p')>((var.get('r').get('height')+var.get('r').get('depth'))+var.get('l'))):
                var.put('l', ((((var.get('l')+var.get('p'))-var.get('r').get('height'))-var.get('r').get('depth'))/Js(2.0)))
            var.put('m', (((var.get('f').get('height')-var.get('r').get('height'))-var.get('l'))-var.get('v')))
            var.put('g', PyJsComma(Js(0.0), Js(None)))
            if (PyJsStrictEq(var.get('r').get('height'),Js(0.0)) and PyJsStrictEq(var.get('r').get('depth'),Js(0.0))):
                var.put('g', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))())
            else:
                var.get('r').get('style').put('paddingLeft', (var.get('f').get('surdWidth')+Js('em')))
                PyJs_Object_373_ = Js({'type':Js('elem'),'elem':var.get('r')})
                PyJs_Object_374_ = Js({'type':Js('kern'),'size':(-(var.get('r').get('height')+var.get('m')))})
                PyJs_Object_375_ = Js({'type':Js('elem'),'elem':var.get('f')})
                PyJs_Object_376_ = Js({'type':Js('kern'),'size':var.get('v')})
                var.put('g', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_373_, PyJs_Object_374_, PyJs_Object_375_, PyJs_Object_376_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
                var.get('g').get('children').get('0').get('children').get('0').get('classes').callprop('push', Js('svg-align'))
            if var.get('e').get('value').get('index').neg():
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('sqrt')]), Js([var.get('g')]), var.get('t'))
            else:
                var.put('y', var.get('t').callprop('havingStyle', var.get('o').get('default').get('SCRIPTSCRIPT')))
                var.put('x', var.get('L')(var.get('e').get('value').get('index'), var.get('y'), var.get('t')))
                var.put('w', (Js(0.6)*(var.get('g').get('height')-var.get('g').get('depth'))))
                PyJs_Object_377_ = Js({'type':Js('elem'),'elem':var.get('x')})
                var.put('b', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_377_]), Js('shift'), (-var.get('w')), var.get('t')))
                var.put('k', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('root')]), Js([var.get('b')])))
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('sqrt')]), Js([var.get('k'), var.get('g')]), var.get('t'))
        PyJs_anonymous_372_._set_name('anonymous')
        var.get('E').put('sqrt', PyJs_anonymous_372_)
        pass
        @Js
        def PyJs_anonymous_378_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').callprop('havingSize', var.get('e').get('value').get('size')))
            return var.get('O')(var.get('e').get('value').get('value'), var.get('r'), var.get('t'))
        PyJs_anonymous_378_._set_name('anonymous')
        var.get('E').put('sizing', PyJs_anonymous_378_)
        @Js
        def PyJs_anonymous_379_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            PyJs_Object_380_ = Js({'display':var.get('o').get('default').get('DISPLAY'),'text':var.get('o').get('default').get('TEXT'),'script':var.get('o').get('default').get('SCRIPT'),'scriptscript':var.get('o').get('default').get('SCRIPTSCRIPT')})
            var.put('r', PyJs_Object_380_)
            var.put('a', var.get('r').get(var.get('e').get('value').get('style')))
            var.put('n', var.get('t').callprop('havingStyle', var.get('a')))
            return var.get('O')(var.get('e').get('value').get('value'), var.get('n'), var.get('t'))
        PyJs_anonymous_379_._set_name('anonymous')
        var.get('E').put('styling', PyJs_anonymous_379_)
        @Js
        def PyJs_anonymous_381_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('e').get('value').get('font'))
            return var.get('L')(var.get('e').get('value').get('body'), var.get('t').callprop('withFont', var.get('r')))
        PyJs_anonymous_381_._set_name('anonymous')
        var.get('E').put('font', PyJs_anonymous_381_)
        @Js
        def PyJs_anonymous_382_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('e').get('value').get('value'))
            if PyJsStrictEq(var.get('r'),Js('.')):
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([var.get('e').get('value').get('mclass')]))
            return var.get('h').get('default').callprop('sizedDelim', var.get('r'), var.get('e').get('value').get('size'), var.get('t'), var.get('e').get('mode'), Js([var.get('e').get('value').get('mclass')]))
        PyJs_anonymous_382_._set_name('anonymous')
        var.get('E').put('delimsizing', PyJs_anonymous_382_)
        @Js
        def PyJs_anonymous_383_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'v', 'o', 'd', 'n', 's', 'e', 'a', 'f', 't'])
            var.put('r', var.get('C')(var.get('e').get('value').get('body'), var.get('t'), Js(True)))
            var.put('a', Js(0.0))
            var.put('n', Js(0.0))
            var.put('i', Js(False))
            #for JS loop
            var.put('l', Js(0.0))
            while (var.get('l')<var.get('r').get('length')):
                try:
                    if var.get('r').get(var.get('l')).get('isMiddle'):
                        var.put('i', Js(True))
                    else:
                        var.put('a', var.get('Math').callprop('max', var.get('r').get(var.get('l')).get('height'), var.get('a')))
                        var.put('n', var.get('Math').callprop('max', var.get('r').get(var.get('l')).get('depth'), var.get('n')))
                finally:
                        (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
            var.put('a', var.get('t').get('sizeMultiplier'), '*')
            var.put('n', var.get('t').get('sizeMultiplier'), '*')
            var.put('s', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('e').get('value').get('left'),Js('.')):
                var.put('s', var.get('_')(var.get('t'), Js([Js('mopen')])))
            else:
                var.put('s', var.get('h').get('default').callprop('leftRightDelim', var.get('e').get('value').get('left'), var.get('a'), var.get('n'), var.get('t'), var.get('e').get('mode'), Js([Js('mopen')])))
            var.get('r').callprop('unshift', var.get('s'))
            if var.get('i'):
                #for JS loop
                var.put('o', Js(1.0))
                while (var.get('o')<var.get('r').get('length')):
                    try:
                        var.put('f', var.get('r').get(var.get('o')))
                        if var.get('f').get('isMiddle'):
                            var.get('r').put(var.get('o'), var.get('h').get('default').callprop('leftRightDelim', var.get('f').get('isMiddle').get('value'), var.get('a'), var.get('n'), var.get('f').get('isMiddle').get('options'), var.get('e').get('mode'), Js([])))
                            var.put('v', var.get('A')(var.get('f').get('children'), Js(0.0)))
                            if var.get('v'):
                                var.get('c').get('default').callprop('prependChildren', var.get('r').get(var.get('o')), var.get('v'))
                    finally:
                            (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
            var.put('d', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('e').get('value').get('right'),Js('.')):
                var.put('d', var.get('_')(var.get('t'), Js([Js('mclose')])))
            else:
                var.put('d', var.get('h').get('default').callprop('leftRightDelim', var.get('e').get('value').get('right'), var.get('a'), var.get('n'), var.get('t'), var.get('e').get('mode'), Js([Js('mclose')])))
            var.get('r').callprop('push', var.get('d'))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('minner')]), var.get('r'), var.get('t'))
        PyJs_anonymous_383_._set_name('anonymous')
        var.get('E').put('leftright', PyJs_anonymous_383_)
        @Js
        def PyJs_anonymous_384_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('e').get('value').get('value'),Js('.')):
                var.put('r', var.get('_')(var.get('t'), Js([])))
            else:
                var.put('r', var.get('h').get('default').callprop('sizedDelim', var.get('e').get('value').get('value'), Js(1.0), var.get('t'), var.get('e').get('mode'), Js([])))
                PyJs_Object_385_ = Js({'value':var.get('e').get('value').get('value'),'options':var.get('t')})
                var.get('r').put('isMiddle', PyJs_Object_385_)
            return var.get('r')
        PyJs_anonymous_384_._set_name('anonymous')
        var.get('E').put('middle', PyJs_anonymous_384_)
        @Js
        def PyJs_anonymous_386_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('rule')]), Js([]), var.get('t')))
            var.put('a', Js(0.0))
            if var.get('e').get('value').get('shift'):
                var.put('a', var.get('m').get('default').callprop('calculateSize', var.get('e').get('value').get('shift'), var.get('t')))
            var.put('n', var.get('m').get('default').callprop('calculateSize', var.get('e').get('value').get('width'), var.get('t')))
            var.put('i', var.get('m').get('default').callprop('calculateSize', var.get('e').get('value').get('height'), var.get('t')))
            var.get('r').get('style').put('borderRightWidth', (var.get('n')+Js('em')))
            var.get('r').get('style').put('borderTopWidth', (var.get('i')+Js('em')))
            var.get('r').get('style').put('bottom', (var.get('a')+Js('em')))
            var.get('r').put('width', var.get('n'))
            var.get('r').put('height', (var.get('i')+var.get('a')))
            var.get('r').put('depth', (-var.get('a')))
            var.get('r').put('maxFontSize', ((var.get('i')*Js(1.125))*var.get('t').get('sizeMultiplier')))
            return var.get('r')
        PyJs_anonymous_386_._set_name('anonymous')
        var.get('E').put('rule', PyJs_anonymous_386_)
        @Js
        def PyJs_anonymous_387_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('rule')]), Js([]), var.get('t')))
            if var.get('e').get('value').get('dimension'):
                var.put('a', var.get('m').get('default').callprop('calculateSize', var.get('e').get('value').get('dimension'), var.get('t')))
                var.get('r').get('style').put('marginLeft', (var.get('a')+Js('em')))
            return var.get('r')
        PyJs_anonymous_387_._set_name('anonymous')
        var.get('E').put('kern', PyJs_anonymous_387_)
        @Js
        def PyJs_anonymous_388_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'g', 'o', 'd', 'n', 's', 'e', 'a', 'f', 't'])
            var.put('r', var.get('e').get('value').get('base'))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('e').get('type'),Js('supsub')):
                var.put('n', var.get('e'))
                var.put('e', var.get('n').get('value').get('base'))
                var.put('r', var.get('e').get('value').get('base'))
                var.get('n').get('value').put('base', var.get('r'))
                var.put('a', var.get('L')(var.get('n'), var.get('t')))
            var.put('i', var.get('L')(var.get('r'), var.get('t').callprop('havingCrampedStyle')))
            var.put('l', (var.get('e').get('value').get('isShifty') and var.get('q')(var.get('r'))))
            var.put('s', Js(0.0))
            if var.get('l'):
                var.put('o', var.get('R')(var.get('r')))
                var.put('f', var.get('L')(var.get('o'), var.get('t').callprop('havingCrampedStyle')))
                var.put('s', var.get('f').get('skew'))
            var.put('h', var.get('Math').callprop('min', var.get('i').get('height'), var.get('t').callprop('fontMetrics').get('xHeight')))
            var.put('v', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('isStretchy').neg():
                var.put('d', var.get('c').get('default').callprop('makeSymbol', var.get('e').get('value').get('label'), Js('Main-Regular'), var.get('e').get('mode'), var.get('t')))
                var.get('d').put('italic', Js(0.0))
                var.put('p', var.get(u"null"))
                if PyJsStrictEq(var.get('e').get('value').get('label'),Js('\\vec')):
                    var.put('p', Js('accent-vec'))
                else:
                    if PyJsStrictEq(var.get('e').get('value').get('label'),Js('\\H')):
                        var.put('p', Js('accent-hungarian'))
                var.put('v', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([]), Js([var.get('d')])))
                var.put('v', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('accent-body'), var.get('p')]), Js([var.get('v')])))
                var.get('v').get('style').put('marginLeft', ((Js(2.0)*var.get('s'))+Js('em')))
                PyJs_Object_389_ = Js({'type':Js('elem'),'elem':var.get('i')})
                PyJs_Object_390_ = Js({'type':Js('kern'),'size':(-var.get('h'))})
                PyJs_Object_391_ = Js({'type':Js('elem'),'elem':var.get('v')})
                var.put('v', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_389_, PyJs_Object_390_, PyJs_Object_391_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
            else:
                var.put('v', var.get('w').get('default').callprop('svgSpan', var.get('e'), var.get('t')))
                PyJs_Object_392_ = Js({'type':Js('elem'),'elem':var.get('i')})
                PyJs_Object_393_ = Js({'type':Js('elem'),'elem':var.get('v')})
                var.put('v', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_392_, PyJs_Object_393_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
                var.put('m', var.get('v').get('children').get('0').get('children').get('0').get('children').get('1'))
                var.get('m').get('classes').callprop('push', Js('svg-align'))
                if (var.get('s')>Js(0.0)):
                    var.get('m').get('style').put('width', ((Js('calc(100% - ')+(Js(2.0)*var.get('s')))+Js('em)')))
                    var.get('m').get('style').put('marginLeft', ((Js(2.0)*var.get('s'))+Js('em')))
            var.put('g', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('accent')]), Js([var.get('v')]), var.get('t')))
            if var.get('a'):
                var.get('a').get('children').put('0', var.get('g'))
                var.get('a').put('height', var.get('Math').callprop('max', var.get('g').get('height'), var.get('a').get('height')))
                var.get('a').get('classes').put('0', Js('mord'))
                return var.get('a')
            else:
                return var.get('g')
        PyJs_anonymous_388_._set_name('anonymous')
        var.get('E').put('accent', PyJs_anonymous_388_)
        @Js
        def PyJs_anonymous_394_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'h', 'l', 'r', 'n', 's', 'e', 'a', 'f', 't'])
            var.put('r', var.get('t').get('style'))
            var.put('a', PyJsStrictEq(var.get('e').get('type'),Js('supsub')))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            var.put('i', PyJsComma(Js(0.0), Js(None)))
            if var.get('a'):
                if var.get('e').get('value').get('sup'):
                    var.put('i', var.get('t').callprop('havingStyle', var.get('r').callprop('sup')))
                    var.put('n', var.get('L')(var.get('e').get('value').get('sup'), var.get('i'), var.get('t')))
                else:
                    var.put('i', var.get('t').callprop('havingStyle', var.get('r').callprop('sub')))
                    var.put('n', var.get('L')(var.get('e').get('value').get('sub'), var.get('i'), var.get('t')))
                var.put('e', var.get('e').get('value').get('base'))
            var.put('l', var.get('L')(var.get('e').get('value').get('base'), var.get('t').callprop('havingBaseStyle', var.get('o').get('default').get('DISPLAY'))))
            var.put('s', var.get('w').get('default').callprop('svgSpan', var.get('e'), var.get('t')))
            var.put('f', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('isOver'):
                PyJs_Object_395_ = Js({'type':Js('elem'),'elem':var.get('l')})
                PyJs_Object_396_ = Js({'type':Js('kern'),'size':Js(0.1)})
                PyJs_Object_397_ = Js({'type':Js('elem'),'elem':var.get('s')})
                var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_395_, PyJs_Object_396_, PyJs_Object_397_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
                var.get('f').get('children').get('0').get('children').get('0').get('children').get('1').get('classes').callprop('push', Js('svg-align'))
            else:
                PyJs_Object_398_ = Js({'type':Js('elem'),'elem':var.get('s')})
                PyJs_Object_399_ = Js({'type':Js('kern'),'size':Js(0.1)})
                PyJs_Object_400_ = Js({'type':Js('elem'),'elem':var.get('l')})
                var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_398_, PyJs_Object_399_, PyJs_Object_400_]), Js('bottom'), ((var.get('l').get('depth')+Js(0.1))+var.get('s').get('height')), var.get('t')))
                var.get('f').get('children').get('0').get('children').get('0').get('children').get('0').get('classes').callprop('push', Js('svg-align'))
            if var.get('a'):
                var.put('h', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), (Js('mover') if var.get('e').get('value').get('isOver') else Js('munder'))]), Js([var.get('f')]), var.get('t')))
                if var.get('e').get('value').get('isOver'):
                    PyJs_Object_401_ = Js({'type':Js('elem'),'elem':var.get('h')})
                    PyJs_Object_402_ = Js({'type':Js('kern'),'size':Js(0.2)})
                    PyJs_Object_403_ = Js({'type':Js('elem'),'elem':var.get('n')})
                    var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_401_, PyJs_Object_402_, PyJs_Object_403_]), Js('firstBaseline'), var.get(u"null"), var.get('t')))
                else:
                    PyJs_Object_404_ = Js({'type':Js('elem'),'elem':var.get('n')})
                    PyJs_Object_405_ = Js({'type':Js('kern'),'size':Js(0.2)})
                    PyJs_Object_406_ = Js({'type':Js('elem'),'elem':var.get('h')})
                    var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_404_, PyJs_Object_405_, PyJs_Object_406_]), Js('bottom'), ((var.get('h').get('depth')+Js(0.2))+var.get('n').get('height')), var.get('t')))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), (Js('mover') if var.get('e').get('value').get('isOver') else Js('munder'))]), Js([var.get('f')]), var.get('t'))
        PyJs_anonymous_394_._set_name('anonymous')
        var.get('E').put('horizBrace', PyJs_anonymous_394_)
        @Js
        def PyJs_anonymous_407_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('L')(var.get('e').get('value').get('body'), var.get('t')))
            var.put('a', var.get('w').get('default').callprop('svgSpan', var.get('e'), var.get('t')))
            var.put('n', (Js(0.12) if JsRegExp('/tilde/').callprop('test', var.get('e').get('value').get('label')) else Js(0.0)))
            PyJs_Object_408_ = Js({'type':Js('elem'),'elem':var.get('a')})
            PyJs_Object_409_ = Js({'type':Js('kern'),'size':var.get('n')})
            PyJs_Object_410_ = Js({'type':Js('elem'),'elem':var.get('r')})
            var.put('i', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_408_, PyJs_Object_409_, PyJs_Object_410_]), Js('bottom'), (var.get('a').get('height')+var.get('n')), var.get('t')))
            var.get('i').get('children').get('0').get('children').get('0').get('children').get('0').get('classes').callprop('push', Js('svg-align'))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('accentunder')]), Js([var.get('i')]), var.get('t'))
        PyJs_anonymous_407_._set_name('anonymous')
        var.get('E').put('accentUnder', PyJs_anonymous_407_)
        @Js
        def PyJs_anonymous_411_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'o', 'n', 's', 'e', 'a', 'f', 't'])
            var.put('r', var.get('L')(var.get('e').get('value').get('body'), var.get('t')))
            var.put('a', var.get('e').get('value').get('label').callprop('substr', Js(1.0)))
            var.put('n', var.get('t').get('sizeMultiplier'))
            var.put('i', PyJsComma(Js(0.0), Js(None)))
            var.put('l', Js(0.0))
            var.put('s', Js(0.0))
            if PyJsStrictEq(var.get('a'),Js('sout')):
                var.put('i', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('stretchy'), Js('sout')])))
                var.get('i').put('height', (var.get('t').callprop('fontMetrics').get('defaultRuleThickness')/var.get('n')))
                var.put('s', ((-Js(0.5))*var.get('t').callprop('fontMetrics').get('xHeight')))
            else:
                var.get('r').get('classes').callprop('push', (Js('boxpad') if PyJsStrictEq(var.get('a'),Js('fbox')) else Js('cancel-pad')))
                var.put('o', var.get('q')(var.get('e').get('value').get('body')))
                var.put('l', (Js(0.34) if PyJsStrictEq(var.get('a'),Js('fbox')) else (Js(0.2) if var.get('o') else Js(0.0))))
                var.put('s', (var.get('r').get('depth')+var.get('l')))
                var.put('i', var.get('w').get('default').callprop('encloseSpan', var.get('r'), var.get('a'), var.get('l'), var.get('t')))
            PyJs_Object_412_ = Js({'type':Js('elem'),'elem':var.get('r'),'shift':Js(0.0)})
            PyJs_Object_413_ = Js({'type':Js('elem'),'elem':var.get('i'),'shift':var.get('s')})
            var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_412_, PyJs_Object_413_]), Js('individualShift'), var.get(u"null"), var.get('t')))
            if PyJsStrictNeq(var.get('a'),Js('fbox')):
                var.get('f').get('children').get('0').get('children').get('0').get('children').get('1').get('classes').callprop('push', Js('svg-align'))
            if JsRegExp('/cancel/').callprop('test', var.get('a')):
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord'), Js('cancel-lap')]), Js([var.get('f')]), var.get('t'))
            else:
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mord')]), Js([var.get('f')]), var.get('t'))
        PyJs_anonymous_411_._set_name('anonymous')
        var.get('E').put('enclose', PyJs_anonymous_411_)
        @Js
        def PyJs_anonymous_414_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'h', 'l', 'r', 'o', 'n', 's', 'e', 'a', 'f', 't'])
            var.put('r', var.get('t').get('style'))
            var.put('a', var.get('t').callprop('havingStyle', var.get('r').callprop('sup')))
            var.put('n', var.get('L')(var.get('e').get('value').get('body'), var.get('a'), var.get('t')))
            var.get('n').get('classes').callprop('push', Js('x-arrow-pad'))
            var.put('i', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('below'):
                var.put('a', var.get('t').callprop('havingStyle', var.get('r').callprop('sub')))
                var.put('i', var.get('L')(var.get('e').get('value').get('below'), var.get('a'), var.get('t')))
                var.get('i').get('classes').callprop('push', Js('x-arrow-pad'))
            var.put('l', var.get('w').get('default').callprop('svgSpan', var.get('e'), var.get('t')))
            var.put('s', ((-var.get('t').callprop('fontMetrics').get('axisHeight'))+var.get('l').get('depth')))
            var.put('o', (((-var.get('t').callprop('fontMetrics').get('axisHeight'))-var.get('l').get('height'))-Js(0.111)))
            var.put('f', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('below'):
                var.put('h', ((((-var.get('t').callprop('fontMetrics').get('axisHeight'))+var.get('i').get('height'))+var.get('l').get('height'))+Js(0.111)))
                PyJs_Object_415_ = Js({'type':Js('elem'),'elem':var.get('n'),'shift':var.get('o')})
                PyJs_Object_416_ = Js({'type':Js('elem'),'elem':var.get('l'),'shift':var.get('s')})
                PyJs_Object_417_ = Js({'type':Js('elem'),'elem':var.get('i'),'shift':var.get('h')})
                var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_415_, PyJs_Object_416_, PyJs_Object_417_]), Js('individualShift'), var.get(u"null"), var.get('t')))
            else:
                PyJs_Object_418_ = Js({'type':Js('elem'),'elem':var.get('n'),'shift':var.get('o')})
                PyJs_Object_419_ = Js({'type':Js('elem'),'elem':var.get('l'),'shift':var.get('s')})
                var.put('f', var.get('c').get('default').callprop('makeVList', Js([PyJs_Object_418_, PyJs_Object_419_]), Js('individualShift'), var.get(u"null"), var.get('t')))
            var.get('f').get('children').get('0').get('children').get('0').get('children').get('1').get('classes').callprop('push', Js('svg-align'))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('mrel'), Js('x-arrow')]), Js([var.get('f')]), var.get('t'))
        PyJs_anonymous_414_._set_name('anonymous')
        var.get('E').put('xArrow', PyJs_anonymous_414_)
        @Js
        def PyJs_anonymous_420_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('C')(var.get('e').get('value').get('value'), var.get('t').callprop('withPhantom'), Js(False)))
            return var.get('c').get('default').get('makeFragment').create(var.get('r'))
        PyJs_anonymous_420_._set_name('anonymous')
        var.get('E').put('phantom', PyJs_anonymous_420_)
        @Js
        def PyJs_anonymous_421_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('C')(var.get('e').get('value').get('value'), var.get('t'), Js(True)))
            return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([var.get('e').get('value').get('mclass')]), var.get('r'), var.get('t'))
        PyJs_anonymous_421_._set_name('anonymous')
        var.get('E').put('mclass', PyJs_anonymous_421_)
        @Js
        def PyJs_e_422_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_422_}, var)
            var.registers(['i', 'r', 'n', 'a', 't'])
            if var.get('t').neg():
                return PyJsComma(Js(0.0),var.get('u').get('makeSpan'))()
            if var.get('E').get(var.get('t').get('type')):
                var.put('n', var.get('E').callprop(var.get('t').get('type'), var.get('t'), var.get('r')))
                if (var.get('a') and PyJsStrictNeq(var.get('r').get('size'),var.get('a').get('size'))):
                    var.put('n', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(var.get('r').callprop('sizingClasses', var.get('a')), Js([var.get('n')]), var.get('r')))
                    var.put('i', (var.get('r').get('sizeMultiplier')/var.get('a').get('sizeMultiplier')))
                    var.get('n').put('height', var.get('i'), '*')
                    var.get('n').put('depth', var.get('i'), '*')
                return var.get('n')
            else:
                PyJsTempException = JsToPyException(var.get('l').get('default').create(((Js("Got group of unknown type: '")+var.get('t').get('type'))+Js("'"))))
                raise PyJsTempException
        PyJs_e_422_._set_name('e')
        var.put('L', PyJs_e_422_)
        @Js
        def PyJs_e_423_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_423_}, var)
            var.registers(['i', 'l', 'r', 'o', 's', 'a', 't'])
            var.put('t', var.get('JSON').callprop('parse', PyJsComma(Js(0.0),var.get('n').get('default'))(var.get('t'))))
            var.put('a', var.get('C')(var.get('t'), var.get('r'), Js(True)))
            var.put('i', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('base')]), var.get('a'), var.get('r')))
            var.put('l', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('strut')])))
            var.put('s', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('strut'), Js('bottom')])))
            var.get('l').get('style').put('height', (var.get('i').get('height')+Js('em')))
            var.get('s').get('style').put('height', ((var.get('i').get('height')+var.get('i').get('depth'))+Js('em')))
            var.get('s').get('style').put('verticalAlign', ((-var.get('i').get('depth'))+Js('em')))
            var.put('o', PyJsComma(Js(0.0),var.get('u').get('makeSpan'))(Js([Js('katex-html')]), Js([var.get('l'), var.get('s'), var.get('i')])))
            var.get('o').callprop('setAttribute', Js('aria-hidden'), Js('true'))
            return var.get('o')
        PyJs_e_423_._set_name('e')
        var.put('P', PyJs_e_423_)
        var.get('t').put('exports', var.get('P'))
    PyJs_anonymous_299_._set_name('anonymous')
    PyJs_Object_424_ = Js({'./ParseError':Js(29.0),'./Style':Js(33.0),'./buildCommon':Js(34.0),'./delimiter':Js(38.0),'./domTree':Js(39.0),'./stretchy':Js(47.0),'./units':Js(50.0),'./utils':Js(51.0),'babel-runtime/core-js/json/stringify':Js(2.0)})
    @Js
    def PyJs_anonymous_425_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'o', 'y', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'b', 'l', 'c', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_x_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_426_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_426_)
        PyJsHoisted_x_.func_name = 'x'
        var.put('x', PyJsHoisted_x_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./buildCommon')))
        var.put('n', var.get('x')(var.get('a')))
        var.put('i', var.get('e')(Js('./fontMetrics')))
        var.put('l', var.get('x')(var.get('i')))
        var.put('s', var.get('e')(Js('./mathMLTree')))
        var.put('o', var.get('x')(var.get('s')))
        var.put('u', var.get('e')(Js('./ParseError')))
        var.put('c', var.get('x')(var.get('u')))
        var.put('f', var.get('e')(Js('./Style')))
        var.put('h', var.get('x')(var.get('f')))
        var.put('v', var.get('e')(Js('./symbols')))
        var.put('d', var.get('x')(var.get('v')))
        var.put('p', var.get('e')(Js('./utils')))
        var.put('m', var.get('x')(var.get('p')))
        var.put('g', var.get('e')(Js('./stretchy')))
        var.put('y', var.get('x')(var.get('g')))
        pass
        @Js
        def PyJs_e_427_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_427_}, var)
            var.registers(['r', 't'])
            if (var.get('d').get('default').get(var.get('r')).get(var.get('t')) and var.get('d').get('default').get(var.get('r')).get(var.get('t')).get('replace')):
                var.put('t', var.get('d').get('default').get(var.get('r')).get(var.get('t')).get('replace'))
            return var.get('o').get('default').get('TextNode').create(var.get('t'))
        PyJs_e_427_._set_name('e')
        var.put('w', PyJs_e_427_)
        @Js
        def PyJs_e_428_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_428_}, var)
            var.registers(['i', 'r', 'o', 'n', 's', 't'])
            var.put('n', var.get('r').get('font'))
            if var.get('n').neg():
                return var.get(u"null")
            var.put('i', var.get('t').get('mode'))
            if PyJsStrictEq(var.get('n'),Js('mathit')):
                return Js('italic')
            var.put('s', var.get('t').get('value'))
            if var.get('m').get('default').callprop('contains', Js([Js('\\imath'), Js('\\jmath')]), var.get('s')):
                return var.get(u"null")
            if (var.get('d').get('default').get(var.get('i')).get(var.get('s')) and var.get('d').get('default').get(var.get('i')).get(var.get('s')).get('replace')):
                var.put('s', var.get('d').get('default').get(var.get('i')).get(var.get('s')).get('replace'))
            var.put('o', var.get('a').get('fontMap').get(var.get('n')).get('fontName'))
            if var.get('l').get('default').callprop('getCharacterMetrics', var.get('s'), var.get('o')):
                return var.get('a').get('fontMap').get(var.get('r').get('font')).get('variant')
            return var.get(u"null")
        PyJs_e_428_._set_name('e')
        var.put('b', PyJs_e_428_)
        PyJs_Object_429_ = Js({})
        var.put('k', PyJs_Object_429_)
        PyJs_Object_430_ = Js({'mi':Js('italic'),'mn':Js('normal'),'mtext':Js('normal')})
        var.put('M', PyJs_Object_430_)
        @Js
        def PyJs_anonymous_431_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mi'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            var.put('a', (var.get('b')(var.get('e'), var.get('t')) or Js('italic')))
            if PyJsStrictNeq(var.get('a'),var.get('M').get(var.get('r').get('type'))):
                var.get('r').callprop('setAttribute', Js('mathvariant'), var.get('a'))
            return var.get('r')
        PyJs_anonymous_431_._set_name('anonymous')
        var.get('k').put('mathord', PyJs_anonymous_431_)
        @Js
        def PyJs_anonymous_432_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('w')(var.get('e').get('value'), var.get('e').get('mode')))
            var.put('a', (var.get('b')(var.get('e'), var.get('t')) or Js('normal')))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('e').get('mode'),Js('text')):
                var.put('n', var.get('o').get('default').get('MathNode').create(Js('mtext'), Js([var.get('r')])))
            else:
                if JsRegExp('/[0-9]/').callprop('test', var.get('e').get('value')):
                    var.put('n', var.get('o').get('default').get('MathNode').create(Js('mn'), Js([var.get('r')])))
                else:
                    if PyJsStrictEq(var.get('e').get('value'),Js('\\prime')):
                        var.put('n', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('r')])))
                    else:
                        var.put('n', var.get('o').get('default').get('MathNode').create(Js('mi'), Js([var.get('r')])))
            if PyJsStrictNeq(var.get('a'),var.get('M').get(var.get('n').get('type'))):
                var.get('n').callprop('setAttribute', Js('mathvariant'), var.get('a'))
            return var.get('n')
        PyJs_anonymous_432_._set_name('anonymous')
        var.get('k').put('textord', PyJs_anonymous_432_)
        @Js
        def PyJs_anonymous_433_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            return var.get('t')
        PyJs_anonymous_433_._set_name('anonymous')
        var.get('k').put('bin', PyJs_anonymous_433_)
        @Js
        def PyJs_anonymous_434_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            return var.get('t')
        PyJs_anonymous_434_._set_name('anonymous')
        var.get('k').put('rel', PyJs_anonymous_434_)
        @Js
        def PyJs_anonymous_435_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            return var.get('t')
        PyJs_anonymous_435_._set_name('anonymous')
        var.get('k').put('open', PyJs_anonymous_435_)
        @Js
        def PyJs_anonymous_436_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            return var.get('t')
        PyJs_anonymous_436_._set_name('anonymous')
        var.get('k').put('close', PyJs_anonymous_436_)
        @Js
        def PyJs_anonymous_437_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            return var.get('t')
        PyJs_anonymous_437_._set_name('anonymous')
        var.get('k').put('inner', PyJs_anonymous_437_)
        @Js
        def PyJs_anonymous_438_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value'), var.get('e').get('mode'))])))
            var.get('t').callprop('setAttribute', Js('separator'), Js('true'))
            return var.get('t')
        PyJs_anonymous_438_._set_name('anonymous')
        var.get('k').put('punct', PyJs_anonymous_438_)
        @Js
        def PyJs_anonymous_439_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('z')(var.get('e').get('value'), var.get('t')))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('mrow'), var.get('r')))
            return var.get('a')
        PyJs_anonymous_439_._set_name('anonymous')
        var.get('k').put('ordgroup', PyJs_anonymous_439_)
        @Js
        def PyJs_anonymous_440_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('e').get('value').get('body'))
            var.put('a', Js([]))
            var.put('n', var.get(u"null"))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('r').get('length')):
                try:
                    var.put('l', var.get('S')(var.get('r').get(var.get('i')), var.get('t')))
                    if (PyJsStrictEq(var.get('l').get('type'),Js('mtext')) and (var.get('n')!=var.get(u"null"))):
                        var.get('Array').get('prototype').get('push').callprop('apply', var.get('n').get('children'), var.get('l').get('children'))
                    else:
                        var.get('a').callprop('push', var.get('l'))
                        if PyJsStrictEq(var.get('l').get('type'),Js('mtext')):
                            var.put('n', var.get('l'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if PyJsStrictEq(var.get('a').get('length'),Js(1.0)):
                return var.get('a').get('0')
            else:
                return var.get('o').get('default').get('MathNode').create(Js('mrow'), var.get('a'))
        PyJs_anonymous_440_._set_name('anonymous')
        var.get('k').put('text', PyJs_anonymous_440_)
        @Js
        def PyJs_anonymous_441_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('z')(var.get('e').get('value').get('value'), var.get('t')))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('mstyle'), var.get('r')))
            var.get('a').callprop('setAttribute', Js('mathcolor'), var.get('e').get('value').get('color'))
            return var.get('a')
        PyJs_anonymous_441_._set_name('anonymous')
        var.get('k').put('color', PyJs_anonymous_441_)
        @Js
        def PyJs_anonymous_442_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'c', 'n', 'u', 's', 'e', 'a', 't'])
            var.put('r', Js(False))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('base'):
                if PyJsStrictEq(var.get('e').get('value').get('base').get('value').get('type'),Js('horizBrace')):
                    var.put('n', (Js(True) if var.get('e').get('value').get('sup') else Js(False)))
                    if PyJsStrictEq(var.get('n'),var.get('e').get('value').get('base').get('value').get('isOver')):
                        var.put('r', Js(True))
                        var.put('a', var.get('e').get('value').get('base').get('value').get('isOver'))
            var.put('i', Js(True))
            var.put('l', Js([var.get('S')(var.get('e').get('value').get('base'), var.get('t'), var.get('i'))]))
            if var.get('e').get('value').get('sub'):
                var.get('l').callprop('push', var.get('S')(var.get('e').get('value').get('sub'), var.get('t'), var.get('i')))
            if var.get('e').get('value').get('sup'):
                var.get('l').callprop('push', var.get('S')(var.get('e').get('value').get('sup'), var.get('t'), var.get('i')))
            var.put('s', PyJsComma(Js(0.0), Js(None)))
            if var.get('r'):
                var.put('s', (Js('mover') if var.get('a') else Js('munder')))
            else:
                if var.get('e').get('value').get('sub').neg():
                    var.put('s', Js('msup'))
                else:
                    if var.get('e').get('value').get('sup').neg():
                        var.put('s', Js('msub'))
                    else:
                        var.put('u', var.get('e').get('value').get('base'))
                        if ((var.get('u') and var.get('u').get('value').get('limits')) and PyJsStrictEq(var.get('t').get('style'),var.get('h').get('default').get('DISPLAY'))):
                            var.put('s', Js('munderover'))
                        else:
                            var.put('s', Js('msubsup'))
            var.put('c', var.get('o').get('default').get('MathNode').create(var.get('s'), var.get('l')))
            return var.get('c')
        PyJs_anonymous_442_._set_name('anonymous')
        var.get('k').put('supsub', PyJs_anonymous_442_)
        @Js
        def PyJs_anonymous_443_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mfrac'), Js([var.get('S')(var.get('e').get('value').get('numer'), var.get('t')), var.get('S')(var.get('e').get('value').get('denom'), var.get('t'))])))
            if var.get('e').get('value').get('hasBarLine').neg():
                var.get('r').callprop('setAttribute', Js('linethickness'), Js('0px'))
            if ((var.get('e').get('value').get('leftDelim')!=var.get(u"null")) or (var.get('e').get('value').get('rightDelim')!=var.get(u"null"))):
                var.put('a', Js([]))
                if (var.get('e').get('value').get('leftDelim')!=var.get(u"null")):
                    var.put('n', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('o').get('default').get('TextNode').create(var.get('e').get('value').get('leftDelim'))])))
                    var.get('n').callprop('setAttribute', Js('fence'), Js('true'))
                    var.get('a').callprop('push', var.get('n'))
                var.get('a').callprop('push', var.get('r'))
                if (var.get('e').get('value').get('rightDelim')!=var.get(u"null")):
                    var.put('i', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('o').get('default').get('TextNode').create(var.get('e').get('value').get('rightDelim'))])))
                    var.get('i').callprop('setAttribute', Js('fence'), Js('true'))
                    var.get('a').callprop('push', var.get('i'))
                var.put('l', var.get('o').get('default').get('MathNode').create(Js('mrow'), var.get('a')))
                return var.get('l')
            return var.get('r')
        PyJs_anonymous_443_._set_name('anonymous')
        var.get('k').put('genfrac', PyJs_anonymous_443_)
        @Js
        def PyJs_anonymous_444_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            @Js
            def PyJs_anonymous_445_(e, this, arguments, var=var):
                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                var.registers(['e'])
                @Js
                def PyJs_anonymous_446_(e, this, arguments, var=var):
                    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                    var.registers(['e'])
                    return var.get('o').get('default').get('MathNode').create(Js('mtd'), Js([var.get('S')(var.get('e'), var.get('t'))]))
                PyJs_anonymous_446_._set_name('anonymous')
                return var.get('o').get('default').get('MathNode').create(Js('mtr'), var.get('e').callprop('map', PyJs_anonymous_446_))
            PyJs_anonymous_445_._set_name('anonymous')
            return var.get('o').get('default').get('MathNode').create(Js('mtable'), var.get('e').get('value').get('body').callprop('map', PyJs_anonymous_445_))
        PyJs_anonymous_444_._set_name('anonymous')
        var.get('k').put('array', PyJs_anonymous_444_)
        @Js
        def PyJs_anonymous_447_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('index'):
                var.put('r', var.get('o').get('default').get('MathNode').create(Js('mroot'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t')), var.get('S')(var.get('e').get('value').get('index'), var.get('t'))])))
            else:
                var.put('r', var.get('o').get('default').get('MathNode').create(Js('msqrt'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t'))])))
            return var.get('r')
        PyJs_anonymous_447_._set_name('anonymous')
        var.get('k').put('sqrt', PyJs_anonymous_447_)
        @Js
        def PyJs_anonymous_448_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('z')(var.get('e').get('value').get('body'), var.get('t')))
            if PyJsStrictNeq(var.get('e').get('value').get('left'),Js('.')):
                var.put('a', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value').get('left'), var.get('e').get('mode'))])))
                var.get('a').callprop('setAttribute', Js('fence'), Js('true'))
                var.get('r').callprop('unshift', var.get('a'))
            if PyJsStrictNeq(var.get('e').get('value').get('right'),Js('.')):
                var.put('n', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value').get('right'), var.get('e').get('mode'))])))
                var.get('n').callprop('setAttribute', Js('fence'), Js('true'))
                var.get('r').callprop('push', var.get('n'))
            var.put('i', var.get('o').get('default').get('MathNode').create(Js('mrow'), var.get('r')))
            return var.get('i')
        PyJs_anonymous_448_._set_name('anonymous')
        var.get('k').put('leftright', PyJs_anonymous_448_)
        @Js
        def PyJs_anonymous_449_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value').get('middle'), var.get('e').get('mode'))])))
            var.get('r').callprop('setAttribute', Js('fence'), Js('true'))
            return var.get('r')
        PyJs_anonymous_449_._set_name('anonymous')
        var.get('k').put('middle', PyJs_anonymous_449_)
        @Js
        def PyJs_anonymous_450_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('isStretchy'):
                var.put('r', var.get('y').get('default').callprop('mathMLnode', var.get('e').get('value').get('label')))
            else:
                var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value').get('label'), var.get('e').get('mode'))])))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('mover'), Js([var.get('S')(var.get('e').get('value').get('base'), var.get('t')), var.get('r')])))
            var.get('a').callprop('setAttribute', Js('accent'), Js('true'))
            return var.get('a')
        PyJs_anonymous_450_._set_name('anonymous')
        var.get('k').put('accent', PyJs_anonymous_450_)
        @Js
        def PyJs_anonymous_451_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', PyJsComma(Js(0.0), Js(None)))
            if (((PyJsStrictEq(var.get('e').get('value'),Js('\\ ')) or PyJsStrictEq(var.get('e').get('value'),Js('\\space'))) or PyJsStrictEq(var.get('e').get('value'),Js(' '))) or PyJsStrictEq(var.get('e').get('value'),Js('~'))):
                var.put('t', var.get('o').get('default').get('MathNode').create(Js('mtext'), Js([var.get('o').get('default').get('TextNode').create(Js('\xa0'))])))
            else:
                var.put('t', var.get('o').get('default').get('MathNode').create(Js('mspace')))
                var.get('t').callprop('setAttribute', Js('width'), var.get('n').get('default').get('spacingFunctions').get(var.get('e').get('value')).get('size'))
            return var.get('t')
        PyJs_anonymous_451_._set_name('anonymous')
        var.get('k').put('spacing', PyJs_anonymous_451_)
        @Js
        def PyJs_anonymous_452_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('symbol'):
                var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(var.get('e').get('value').get('body'), var.get('e').get('mode'))])))
            else:
                if var.get('e').get('value').get('value'):
                    var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), var.get('z')(var.get('e').get('value').get('value'), var.get('t'))))
                else:
                    var.put('r', var.get('o').get('default').get('MathNode').create(Js('mi'), Js([var.get('o').get('default').get('TextNode').create(var.get('e').get('value').get('body').callprop('slice', Js(1.0)))])))
            return var.get('r')
        PyJs_anonymous_452_._set_name('anonymous')
        var.get('k').put('op', PyJs_anonymous_452_)
        @Js
        def PyJs_anonymous_453_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', Js([]))
            if (PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pod')) or PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pmod'))):
                var.get('r').callprop('push', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(Js('('), var.get('e').get('mode'))])))
            if PyJsStrictNeq(var.get('e').get('value').get('modType'),Js('pod')):
                var.get('r').callprop('push', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(Js('mod'), var.get('e').get('mode'))])))
            if var.get('e').get('value').get('value'):
                var.put('a', var.get('o').get('default').get('MathNode').create(Js('mspace')))
                var.get('a').callprop('setAttribute', Js('width'), Js('0.333333em'))
                var.get('r').callprop('push', var.get('a'))
                var.put('r', var.get('r').callprop('concat', var.get('z')(var.get('e').get('value').get('value'), var.get('t'))))
            if (PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pod')) or PyJsStrictEq(var.get('e').get('value').get('modType'),Js('pmod'))):
                var.get('r').callprop('push', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('w')(Js(')'), var.get('e').get('mode'))])))
            return var.get('o').get('default').get('MathNode').create(Js('mo'), var.get('r'))
        PyJs_anonymous_453_._set_name('anonymous')
        var.get('k').put('mod', PyJs_anonymous_453_)
        @Js
        def PyJs_anonymous_454_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mtext'), Js([var.get('o').get('default').get('TextNode').create(Js('KaTeX'))])))
            return var.get('t')
        PyJs_anonymous_454_._set_name('anonymous')
        var.get('k').put('katex', PyJs_anonymous_454_)
        @Js
        def PyJs_anonymous_455_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('e').get('value').get('font'))
            return var.get('S')(var.get('e').get('value').get('body'), var.get('t').callprop('withFont', var.get('r')))
        PyJs_anonymous_455_._set_name('anonymous')
        var.get('k').put('font', PyJs_anonymous_455_)
        @Js
        def PyJs_anonymous_456_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('t', Js([]))
            if PyJsStrictNeq(var.get('e').get('value').get('value'),Js('.')):
                var.get('t').callprop('push', var.get('w')(var.get('e').get('value').get('value'), var.get('e').get('mode')))
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), var.get('t')))
            if (PyJsStrictEq(var.get('e').get('value').get('mclass'),Js('mopen')) or PyJsStrictEq(var.get('e').get('value').get('mclass'),Js('mclose'))):
                var.get('r').callprop('setAttribute', Js('fence'), Js('true'))
            else:
                var.get('r').callprop('setAttribute', Js('fence'), Js('false'))
            return var.get('r')
        PyJs_anonymous_456_._set_name('anonymous')
        var.get('k').put('delimsizing', PyJs_anonymous_456_)
        @Js
        def PyJs_anonymous_457_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 'u', 's', 'e', 'a', 't'])
            PyJs_Object_458_ = Js({'display':var.get('h').get('default').get('DISPLAY'),'text':var.get('h').get('default').get('TEXT'),'script':var.get('h').get('default').get('SCRIPT'),'scriptscript':var.get('h').get('default').get('SCRIPTSCRIPT')})
            var.put('r', PyJs_Object_458_)
            var.put('a', var.get('r').get(var.get('e').get('value').get('style')))
            var.put('n', var.get('t').callprop('havingStyle', var.get('a')))
            var.put('i', var.get('z')(var.get('e').get('value').get('value'), var.get('n')))
            var.put('l', var.get('o').get('default').get('MathNode').create(Js('mstyle'), var.get('i')))
            PyJs_Object_459_ = Js({'display':Js([Js('0'), Js('true')]),'text':Js([Js('0'), Js('false')]),'script':Js([Js('1'), Js('false')]),'scriptscript':Js([Js('2'), Js('false')])})
            var.put('s', PyJs_Object_459_)
            var.put('u', var.get('s').get(var.get('e').get('value').get('style')))
            var.get('l').callprop('setAttribute', Js('scriptlevel'), var.get('u').get('0'))
            var.get('l').callprop('setAttribute', Js('displaystyle'), var.get('u').get('1'))
            return var.get('l')
        PyJs_anonymous_457_._set_name('anonymous')
        var.get('k').put('styling', PyJs_anonymous_457_)
        @Js
        def PyJs_anonymous_460_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').callprop('havingSize', var.get('e').get('value').get('size')))
            var.put('a', var.get('z')(var.get('e').get('value').get('value'), var.get('r')))
            var.put('n', var.get('o').get('default').get('MathNode').create(Js('mstyle'), var.get('a')))
            var.get('n').callprop('setAttribute', Js('mathsize'), (var.get('r').get('sizeMultiplier')+Js('em')))
            return var.get('n')
        PyJs_anonymous_460_._set_name('anonymous')
        var.get('k').put('sizing', PyJs_anonymous_460_)
        @Js
        def PyJs_anonymous_461_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('o').get('default').get('TextNode').create(Js('‾'))])))
            var.get('r').callprop('setAttribute', Js('stretchy'), Js('true'))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('mover'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t')), var.get('r')])))
            var.get('a').callprop('setAttribute', Js('accent'), Js('true'))
            return var.get('a')
        PyJs_anonymous_461_._set_name('anonymous')
        var.get('k').put('overline', PyJs_anonymous_461_)
        @Js
        def PyJs_anonymous_462_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mo'), Js([var.get('o').get('default').get('TextNode').create(Js('‾'))])))
            var.get('r').callprop('setAttribute', Js('stretchy'), Js('true'))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('munder'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t')), var.get('r')])))
            var.get('a').callprop('setAttribute', Js('accentunder'), Js('true'))
            return var.get('a')
        PyJs_anonymous_462_._set_name('anonymous')
        var.get('k').put('underline', PyJs_anonymous_462_)
        @Js
        def PyJs_anonymous_463_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('y').get('default').callprop('mathMLnode', var.get('e').get('value').get('label')))
            var.put('a', var.get('o').get('default').get('MathNode').create(Js('munder'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t')), var.get('r')])))
            var.get('a').callprop('setAttribute', Js('accentunder'), Js('true'))
            return var.get('a')
        PyJs_anonymous_463_._set_name('anonymous')
        var.get('k').put('accentUnder', PyJs_anonymous_463_)
        @Js
        def PyJs_anonymous_464_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('menclose'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t'))])))
            var.put('a', Js(''))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('e').get('value').get('label'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\bcancel')):
                    SWITCHED = True
                    var.put('a', Js('downdiagonalstrike'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\sout')):
                    SWITCHED = True
                    var.put('a', Js('horizontalstrike'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\fbox')):
                    SWITCHED = True
                    var.put('a', Js('box'))
                    break
                if True:
                    SWITCHED = True
                    var.put('a', Js('updiagonalstrike'))
                SWITCHED = True
                break
            var.get('r').callprop('setAttribute', Js('notation'), var.get('a'))
            return var.get('r')
        PyJs_anonymous_464_._set_name('anonymous')
        var.get('k').put('enclose', PyJs_anonymous_464_)
        @Js
        def PyJs_anonymous_465_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('y').get('default').callprop('mathMLnode', var.get('e').get('value').get('label')))
            return var.get('o').get('default').get('MathNode').create((Js('mover') if var.get('e').get('value').get('isOver') else Js('munder')), Js([var.get('S')(var.get('e').get('value').get('base'), var.get('t')), var.get('r')]))
        PyJs_anonymous_465_._set_name('anonymous')
        var.get('k').put('horizBrace', PyJs_anonymous_465_)
        @Js
        def PyJs_anonymous_466_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('y').get('default').callprop('mathMLnode', var.get('e').get('value').get('label')))
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            if var.get('e').get('value').get('body'):
                var.put('i', var.get('S')(var.get('e').get('value').get('body'), var.get('t')))
                if var.get('e').get('value').get('below'):
                    var.put('n', var.get('S')(var.get('e').get('value').get('below'), var.get('t')))
                    var.put('a', var.get('o').get('default').get('MathNode').create(Js('munderover'), Js([var.get('r'), var.get('n'), var.get('i')])))
                else:
                    var.put('a', var.get('o').get('default').get('MathNode').create(Js('mover'), Js([var.get('r'), var.get('i')])))
            else:
                if var.get('e').get('value').get('below'):
                    var.put('n', var.get('S')(var.get('e').get('value').get('below'), var.get('t')))
                    var.put('a', var.get('o').get('default').get('MathNode').create(Js('munder'), Js([var.get('r'), var.get('n')])))
                else:
                    var.put('a', var.get('o').get('default').get('MathNode').create(Js('mover'), Js([var.get('r')])))
            return var.get('a')
        PyJs_anonymous_466_._set_name('anonymous')
        var.get('k').put('xArrow', PyJs_anonymous_466_)
        @Js
        def PyJs_anonymous_467_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mrow')))
            return var.get('t')
        PyJs_anonymous_467_._set_name('anonymous')
        var.get('k').put('rule', PyJs_anonymous_467_)
        @Js
        def PyJs_anonymous_468_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', var.get('o').get('default').get('MathNode').create(Js('mrow')))
            return var.get('t')
        PyJs_anonymous_468_._set_name('anonymous')
        var.get('k').put('kern', PyJs_anonymous_468_)
        @Js
        def PyJs_anonymous_469_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mpadded'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t'))])))
            var.get('r').callprop('setAttribute', Js('lspace'), Js('-1width'))
            var.get('r').callprop('setAttribute', Js('width'), Js('0px'))
            return var.get('r')
        PyJs_anonymous_469_._set_name('anonymous')
        var.get('k').put('llap', PyJs_anonymous_469_)
        @Js
        def PyJs_anonymous_470_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('o').get('default').get('MathNode').create(Js('mpadded'), Js([var.get('S')(var.get('e').get('value').get('body'), var.get('t'))])))
            var.get('r').callprop('setAttribute', Js('width'), Js('0px'))
            return var.get('r')
        PyJs_anonymous_470_._set_name('anonymous')
        var.get('k').put('rlap', PyJs_anonymous_470_)
        @Js
        def PyJs_anonymous_471_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('z')(var.get('e').get('value').get('value'), var.get('t')))
            return var.get('o').get('default').get('MathNode').create(Js('mphantom'), var.get('r'))
        PyJs_anonymous_471_._set_name('anonymous')
        var.get('k').put('phantom', PyJs_anonymous_471_)
        @Js
        def PyJs_anonymous_472_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('z')(var.get('e').get('value').get('value'), var.get('t')))
            return var.get('o').get('default').get('MathNode').create(Js('mstyle'), var.get('r'))
        PyJs_anonymous_472_._set_name('anonymous')
        var.get('k').put('mclass', PyJs_anonymous_472_)
        @Js
        def PyJs_e_473_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_473_}, var)
            var.registers(['i', 'r', 'n', 'a', 't'])
            var.put('a', Js([]))
            #for JS loop
            var.put('n', Js(0.0))
            while (var.get('n')<var.get('t').get('length')):
                try:
                    var.put('i', var.get('t').get(var.get('n')))
                    var.get('a').callprop('push', var.get('S')(var.get('i'), var.get('r')))
                finally:
                        (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
            return var.get('a')
        PyJs_e_473_._set_name('e')
        var.put('z', PyJs_e_473_)
        @Js
        def PyJs_e_474_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_474_}, var)
            var.registers(['r', 'a', 'n', 't'])
            var.put('a', (var.get('arguments').get('2') if ((var.get('arguments').get('length')>Js(2.0)) and PyJsStrictNeq(var.get('arguments').get('2'),var.get('undefined'))) else Js(False)))
            if var.get('t').neg():
                return var.get('o').get('default').get('MathNode').create(Js('mrow'))
            if var.get('k').get(var.get('t').get('type')):
                var.put('n', var.get('k').callprop(var.get('t').get('type'), var.get('t'), var.get('r')))
                if var.get('a'):
                    if (PyJsStrictEq(var.get('n').get('type'),Js('mrow')) and PyJsStrictEq(var.get('n').get('children').get('length'),Js(1.0))):
                        return var.get('n').get('children').get('0')
                return var.get('n')
            else:
                PyJsTempException = JsToPyException(var.get('c').get('default').create(((Js("Got group of unknown type: '")+var.get('t').get('type'))+Js("'"))))
                raise PyJsTempException
        PyJs_e_474_._set_name('e')
        var.put('S', PyJs_e_474_)
        @Js
        def PyJs_e_475_(t, r, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_475_}, var)
            var.registers(['i', 'l', 'r', 'c', 'n', 'u', 's', 't'])
            var.put('i', var.get('z')(var.get('t'), var.get('n')))
            var.put('l', var.get('o').get('default').get('MathNode').create(Js('mrow'), var.get('i')))
            var.put('s', var.get('o').get('default').get('MathNode').create(Js('annotation'), Js([var.get('o').get('default').get('TextNode').create(var.get('r'))])))
            var.get('s').callprop('setAttribute', Js('encoding'), Js('application/x-tex'))
            var.put('u', var.get('o').get('default').get('MathNode').create(Js('semantics'), Js([var.get('l'), var.get('s')])))
            var.put('c', var.get('o').get('default').get('MathNode').create(Js('math'), Js([var.get('u')])))
            return PyJsComma(Js(0.0),var.get('a').get('makeSpan'))(Js([Js('katex-mathml')]), Js([var.get('c')]))
        PyJs_e_475_._set_name('e')
        var.put('A', PyJs_e_475_)
        var.get('t').put('exports', var.get('A'))
    PyJs_anonymous_425_._set_name('anonymous')
    PyJs_Object_476_ = Js({'./ParseError':Js(29.0),'./Style':Js(33.0),'./buildCommon':Js(34.0),'./fontMetrics':Js(41.0),'./mathMLTree':Js(45.0),'./stretchy':Js(47.0),'./symbols':Js(48.0),'./utils':Js(51.0)})
    @Js
    def PyJs_anonymous_477_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_d_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_478_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_478_)
        PyJsHoisted_d_.func_name = 'd'
        var.put('d', PyJsHoisted_d_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./buildHTML')))
        var.put('n', var.get('d')(var.get('a')))
        var.put('i', var.get('e')(Js('./buildMathML')))
        var.put('l', var.get('d')(var.get('i')))
        var.put('s', var.get('e')(Js('./buildCommon')))
        var.put('o', var.get('e')(Js('./Options')))
        var.put('u', var.get('d')(var.get('o')))
        var.put('c', var.get('e')(Js('./Settings')))
        var.put('f', var.get('d')(var.get('c')))
        var.put('h', var.get('e')(Js('./Style')))
        var.put('v', var.get('d')(var.get('h')))
        pass
        @Js
        def PyJs_e_479_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_479_}, var)
            var.registers(['i', 'h', 'r', 'c', 'o', 'd', 'a', 't'])
            PyJs_Object_480_ = Js({})
            var.put('a', (var.get('a') or var.get('f').get('default').create(PyJs_Object_480_)))
            var.put('i', var.get('v').get('default').get('TEXT'))
            if var.get('a').get('displayMode'):
                var.put('i', var.get('v').get('default').get('DISPLAY'))
            PyJs_Object_481_ = Js({'style':var.get('i')})
            var.put('o', var.get('u').get('default').create(PyJs_Object_481_))
            var.put('c', PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('t'), var.get('r'), var.get('o')))
            var.put('h', PyJsComma(Js(0.0),var.get('n').get('default'))(var.get('t'), var.get('o')))
            var.put('d', PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([Js('katex')]), Js([var.get('c'), var.get('h')])))
            if var.get('a').get('displayMode'):
                return PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([Js('katex-display')]), Js([var.get('d')]))
            else:
                return var.get('d')
        PyJs_e_479_._set_name('e')
        var.put('p', PyJs_e_479_)
        var.get('t').put('exports', var.get('p'))
    PyJs_anonymous_477_._set_name('anonymous')
    PyJs_Object_482_ = Js({'./Options':Js(28.0),'./Settings':Js(32.0),'./Style':Js(33.0),'./buildCommon':Js(34.0),'./buildHTML':Js(35.0),'./buildMathML':Js(36.0)})
    @Js
    def PyJs_anonymous_483_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['B', 'R', 'q', 'E', 'r', 'o', 'y', 'T', 'N', 'L', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'O', '_', 'b', 'P', 'l', 'c', 'C', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_p_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_484_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_484_)
        PyJsHoisted_p_.func_name = 'p'
        var.put('p', PyJsHoisted_p_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./ParseError')))
        var.put('n', var.get('p')(var.get('a')))
        var.put('i', var.get('e')(Js('./Style')))
        var.put('l', var.get('p')(var.get('i')))
        var.put('s', var.get('e')(Js('./buildCommon')))
        var.put('o', var.get('p')(var.get('s')))
        var.put('u', var.get('e')(Js('./fontMetrics')))
        var.put('c', var.get('p')(var.get('u')))
        var.put('f', var.get('e')(Js('./symbols')))
        var.put('h', var.get('p')(var.get('f')))
        var.put('v', var.get('e')(Js('./utils')))
        var.put('d', var.get('p')(var.get('v')))
        pass
        @Js
        def PyJs_e_485_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_485_}, var)
            var.registers(['r', 't'])
            if (var.get('h').get('default').get('math').get(var.get('t')) and var.get('h').get('default').get('math').get(var.get('t')).get('replace')):
                return var.get('c').get('default').callprop('getCharacterMetrics', var.get('h').get('default').get('math').get(var.get('t')).get('replace'), var.get('r'))
            else:
                return var.get('c').get('default').callprop('getCharacterMetrics', var.get('t'), var.get('r'))
        PyJs_e_485_._set_name('e')
        var.put('m', PyJs_e_485_)
        @Js
        def PyJs_e_486_(t, r, a, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_486_}, var)
            var.registers(['i', 'r', 'l', 'n', 'a', 't'])
            var.put('i', var.get('a').callprop('havingBaseStyle', var.get('r')))
            var.put('l', PyJsComma(Js(0.0),var.get('s').get('makeSpan'))((var.get('n') or Js([])).callprop('concat', var.get('i').callprop('sizingClasses', var.get('a'))), Js([var.get('t')]), var.get('a')))
            var.get('l').put('delimSizeMultiplier', (var.get('i').get('sizeMultiplier')/var.get('a').get('sizeMultiplier')))
            var.get('l').put('height', var.get('l').get('delimSizeMultiplier'), '*')
            var.get('l').put('depth', var.get('l').get('delimSizeMultiplier'), '*')
            var.get('l').put('maxFontSize', var.get('i').get('sizeMultiplier'))
            return var.get('l')
        PyJs_e_486_._set_name('e')
        var.put('g', PyJs_e_486_)
        @Js
        def PyJs_e_487_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_487_}, var)
            var.registers(['i', 'r', 'n', 'a', 't'])
            var.put('n', var.get('r').callprop('havingBaseStyle', var.get('a')))
            var.put('i', ((Js(1.0)-(var.get('r').get('sizeMultiplier')/var.get('n').get('sizeMultiplier')))*var.get('r').callprop('fontMetrics').get('axisHeight')))
            var.get('t').get('classes').callprop('push', Js('delimcenter'))
            var.get('t').get('style').put('top', (var.get('i')+Js('em')))
            var.get('t').put('height', var.get('i'), '-')
            var.get('t').put('depth', var.get('i'), '+')
        PyJs_e_487_._set_name('e')
        var.put('y', PyJs_e_487_)
        @Js
        def PyJs_e_488_(t, r, a, n, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_488_}, var)
            var.registers(['i', 'r', 'l', 'n', 'u', 's', 'a', 't'])
            var.put('s', var.get('o').get('default').callprop('makeSymbol', var.get('t'), Js('Main-Regular'), var.get('i'), var.get('n')))
            var.put('u', var.get('g')(var.get('s'), var.get('r'), var.get('n'), var.get('l')))
            if var.get('a'):
                var.get('y')(var.get('u'), var.get('n'), var.get('r'))
            return var.get('u')
        PyJs_e_488_._set_name('e')
        var.put('x', PyJs_e_488_)
        @Js
        def PyJs_e_489_(t, r, a, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_489_}, var)
            var.registers(['r', 'a', 'n', 't'])
            return var.get('o').get('default').callprop('makeSymbol', var.get('t'), ((Js('Size')+var.get('r'))+Js('-Regular')), var.get('a'), var.get('n'))
        PyJs_e_489_._set_name('e')
        var.put('w', PyJs_e_489_)
        @Js
        def PyJs_e_490_(t, r, a, n, i, o, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'o':o, 'this':this, 'arguments':arguments, 'e':PyJs_e_490_}, var)
            var.registers(['i', 'r', 'c', 'o', 'n', 'u', 'a', 't'])
            var.put('u', var.get('w')(var.get('t'), var.get('r'), var.get('i'), var.get('n')))
            var.put('c', var.get('g')(PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([Js('delimsizing'), (Js('size')+var.get('r'))]), Js([var.get('u')]), var.get('n')), var.get('l').get('default').get('TEXT'), var.get('n'), var.get('o')))
            if var.get('a'):
                var.get('y')(var.get('c'), var.get('n'), var.get('l').get('default').get('TEXT'))
            return var.get('c')
        PyJs_e_490_._set_name('e')
        var.put('b', PyJs_e_490_)
        @Js
        def PyJs_e_491_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_491_}, var)
            var.registers(['i', 'r', 'n', 'a', 't'])
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            if PyJsStrictEq(var.get('r'),Js('Size1-Regular')):
                var.put('n', Js('delim-size1'))
            else:
                if PyJsStrictEq(var.get('r'),Js('Size4-Regular')):
                    var.put('n', Js('delim-size4'))
            var.put('i', PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([Js('delimsizinginner'), var.get('n')]), Js([PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([]), Js([var.get('o').get('default').callprop('makeSymbol', var.get('t'), var.get('r'), var.get('a'))]))])))
            PyJs_Object_492_ = Js({'type':Js('elem'),'elem':var.get('i')})
            return PyJs_Object_492_
        PyJs_e_491_._set_name('e')
        var.put('k', PyJs_e_491_)
        @Js
        def PyJs_e_493_(t, r, a, n, i, u, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'u':u, 'this':this, 'arguments':arguments, 'e':PyJs_e_493_}, var)
            var.registers(['B', 'R', 'q', 'E', 'r', 'y', 'T', 'N', 'L', 'i', 'h', 'v', 'w', 'x', 'a', 'A', 'S', 'O', '_', 'b', 'P', 'c', 'C', 'z', 'u', 'M', 't', 'p', 'd', 'n', 'f'])
            var.put('c', PyJsComma(Js(0.0), Js(None)))
            var.put('f', PyJsComma(Js(0.0), Js(None)))
            var.put('h', PyJsComma(Js(0.0), Js(None)))
            var.put('v', PyJsComma(Js(0.0), Js(None)))
            var.put('c', var.put('h', var.put('v', var.get('t'))))
            var.put('f', var.get(u"null"))
            var.put('d', Js('Size1-Regular'))
            if PyJsStrictEq(var.get('t'),Js('\\uparrow')):
                var.put('h', var.put('v', Js('⏐')))
            else:
                if PyJsStrictEq(var.get('t'),Js('\\Uparrow')):
                    var.put('h', var.put('v', Js('‖')))
                else:
                    if PyJsStrictEq(var.get('t'),Js('\\downarrow')):
                        var.put('c', var.put('h', Js('⏐')))
                    else:
                        if PyJsStrictEq(var.get('t'),Js('\\Downarrow')):
                            var.put('c', var.put('h', Js('‖')))
                        else:
                            if PyJsStrictEq(var.get('t'),Js('\\updownarrow')):
                                var.put('c', Js('\\uparrow'))
                                var.put('h', Js('⏐'))
                                var.put('v', Js('\\downarrow'))
                            else:
                                if PyJsStrictEq(var.get('t'),Js('\\Updownarrow')):
                                    var.put('c', Js('\\Uparrow'))
                                    var.put('h', Js('‖'))
                                    var.put('v', Js('\\Downarrow'))
                                else:
                                    if (PyJsStrictEq(var.get('t'),Js('[')) or PyJsStrictEq(var.get('t'),Js('\\lbrack'))):
                                        var.put('c', Js('⎡'))
                                        var.put('h', Js('⎢'))
                                        var.put('v', Js('⎣'))
                                        var.put('d', Js('Size4-Regular'))
                                    else:
                                        if (PyJsStrictEq(var.get('t'),Js(']')) or PyJsStrictEq(var.get('t'),Js('\\rbrack'))):
                                            var.put('c', Js('⎤'))
                                            var.put('h', Js('⎥'))
                                            var.put('v', Js('⎦'))
                                            var.put('d', Js('Size4-Regular'))
                                        else:
                                            if PyJsStrictEq(var.get('t'),Js('\\lfloor')):
                                                var.put('h', var.put('c', Js('⎢')))
                                                var.put('v', Js('⎣'))
                                                var.put('d', Js('Size4-Regular'))
                                            else:
                                                if PyJsStrictEq(var.get('t'),Js('\\lceil')):
                                                    var.put('c', Js('⎡'))
                                                    var.put('h', var.put('v', Js('⎢')))
                                                    var.put('d', Js('Size4-Regular'))
                                                else:
                                                    if PyJsStrictEq(var.get('t'),Js('\\rfloor')):
                                                        var.put('h', var.put('c', Js('⎥')))
                                                        var.put('v', Js('⎦'))
                                                        var.put('d', Js('Size4-Regular'))
                                                    else:
                                                        if PyJsStrictEq(var.get('t'),Js('\\rceil')):
                                                            var.put('c', Js('⎤'))
                                                            var.put('h', var.put('v', Js('⎥')))
                                                            var.put('d', Js('Size4-Regular'))
                                                        else:
                                                            if PyJsStrictEq(var.get('t'),Js('(')):
                                                                var.put('c', Js('⎛'))
                                                                var.put('h', Js('⎜'))
                                                                var.put('v', Js('⎝'))
                                                                var.put('d', Js('Size4-Regular'))
                                                            else:
                                                                if PyJsStrictEq(var.get('t'),Js(')')):
                                                                    var.put('c', Js('⎞'))
                                                                    var.put('h', Js('⎟'))
                                                                    var.put('v', Js('⎠'))
                                                                    var.put('d', Js('Size4-Regular'))
                                                                else:
                                                                    if (PyJsStrictEq(var.get('t'),Js('\\{')) or PyJsStrictEq(var.get('t'),Js('\\lbrace'))):
                                                                        var.put('c', Js('⎧'))
                                                                        var.put('f', Js('⎨'))
                                                                        var.put('v', Js('⎩'))
                                                                        var.put('h', Js('⎪'))
                                                                        var.put('d', Js('Size4-Regular'))
                                                                    else:
                                                                        if (PyJsStrictEq(var.get('t'),Js('\\}')) or PyJsStrictEq(var.get('t'),Js('\\rbrace'))):
                                                                            var.put('c', Js('⎫'))
                                                                            var.put('f', Js('⎬'))
                                                                            var.put('v', Js('⎭'))
                                                                            var.put('h', Js('⎪'))
                                                                            var.put('d', Js('Size4-Regular'))
                                                                        else:
                                                                            if PyJsStrictEq(var.get('t'),Js('\\lgroup')):
                                                                                var.put('c', Js('⎧'))
                                                                                var.put('v', Js('⎩'))
                                                                                var.put('h', Js('⎪'))
                                                                                var.put('d', Js('Size4-Regular'))
                                                                            else:
                                                                                if PyJsStrictEq(var.get('t'),Js('\\rgroup')):
                                                                                    var.put('c', Js('⎫'))
                                                                                    var.put('v', Js('⎭'))
                                                                                    var.put('h', Js('⎪'))
                                                                                    var.put('d', Js('Size4-Regular'))
                                                                                else:
                                                                                    if PyJsStrictEq(var.get('t'),Js('\\lmoustache')):
                                                                                        var.put('c', Js('⎧'))
                                                                                        var.put('v', Js('⎭'))
                                                                                        var.put('h', Js('⎪'))
                                                                                        var.put('d', Js('Size4-Regular'))
                                                                                    else:
                                                                                        if PyJsStrictEq(var.get('t'),Js('\\rmoustache')):
                                                                                            var.put('c', Js('⎫'))
                                                                                            var.put('v', Js('⎩'))
                                                                                            var.put('h', Js('⎪'))
                                                                                            var.put('d', Js('Size4-Regular'))
            var.put('p', var.get('m')(var.get('c'), var.get('d')))
            var.put('y', (var.get('p').get('height')+var.get('p').get('depth')))
            var.put('x', var.get('m')(var.get('h'), var.get('d')))
            var.put('w', (var.get('x').get('height')+var.get('x').get('depth')))
            var.put('b', var.get('m')(var.get('v'), var.get('d')))
            var.put('M', (var.get('b').get('height')+var.get('b').get('depth')))
            var.put('z', Js(0.0))
            var.put('S', Js(1.0))
            if PyJsStrictNeq(var.get('f'),var.get(u"null")):
                var.put('A', var.get('m')(var.get('f'), var.get('d')))
                var.put('z', (var.get('A').get('height')+var.get('A').get('depth')))
                var.put('S', Js(2.0))
            var.put('C', ((var.get('y')+var.get('M'))+var.get('z')))
            var.put('T', var.get('Math').callprop('ceil', ((var.get('r')-var.get('C'))/(var.get('S')*var.get('w')))))
            var.put('N', (var.get('C')+((var.get('T')*var.get('S'))*var.get('w'))))
            var.put('R', var.get('n').callprop('fontMetrics').get('axisHeight'))
            if var.get('a'):
                var.put('R', var.get('n').get('sizeMultiplier'), '*')
            var.put('q', ((var.get('N')/Js(2.0))-var.get('R')))
            var.put('_', Js([]))
            var.get('_').callprop('push', var.get('k')(var.get('v'), var.get('d'), var.get('i')))
            if PyJsStrictEq(var.get('f'),var.get(u"null")):
                #for JS loop
                var.put('E', Js(0.0))
                while (var.get('E')<var.get('T')):
                    try:
                        var.get('_').callprop('push', var.get('k')(var.get('h'), var.get('d'), var.get('i')))
                    finally:
                            (var.put('E',Js(var.get('E').to_number())+Js(1))-Js(1))
            else:
                #for JS loop
                var.put('B', Js(0.0))
                while (var.get('B')<var.get('T')):
                    try:
                        var.get('_').callprop('push', var.get('k')(var.get('h'), var.get('d'), var.get('i')))
                    finally:
                            (var.put('B',Js(var.get('B').to_number())+Js(1))-Js(1))
                var.get('_').callprop('push', var.get('k')(var.get('f'), var.get('d'), var.get('i')))
                #for JS loop
                var.put('O', Js(0.0))
                while (var.get('O')<var.get('T')):
                    try:
                        var.get('_').callprop('push', var.get('k')(var.get('h'), var.get('d'), var.get('i')))
                    finally:
                            (var.put('O',Js(var.get('O').to_number())+Js(1))-Js(1))
            var.get('_').callprop('push', var.get('k')(var.get('c'), var.get('d'), var.get('i')))
            var.put('L', var.get('n').callprop('havingBaseStyle', var.get('l').get('default').get('TEXT')))
            var.put('P', var.get('o').get('default').callprop('makeVList', var.get('_'), Js('bottom'), var.get('q'), var.get('L')))
            return var.get('g')(PyJsComma(Js(0.0),var.get('s').get('makeSpan'))(Js([Js('delimsizing'), Js('mult')]), Js([var.get('P')]), var.get('L')), var.get('l').get('default').get('TEXT'), var.get('n'), var.get('u'))
        PyJs_e_493_._set_name('e')
        var.put('M', PyJs_e_493_)
        PyJs_Object_494_ = Js({'main':Js("<svg viewBox='0 0 400000 1000' preserveAspectRatio='xMinYMin\nslice'><path d='M95 622c-2.667 0-7.167-2.667-13.5\n-8S72 604 72 600c0-2 .333-3.333 1-4 1.333-2.667 23.833-20.667 67.5-54s\n65.833-50.333 66.5-51c1.333-1.333 3-2 5-2 4.667 0 8.667 3.333 12 10l173\n378c.667 0 35.333-71 104-213s137.5-285 206.5-429S812 17.333 812 14c5.333\n-9.333 12-14 20-14h399166v40H845.272L620 507 385 993c-2.667 4.667-9 7-19\n7-6 0-10-1-12-3L160 575l-65 47zM834 0h399166v40H845z'/></svg>"),'1':Js("<svg viewBox='0 0 400000 1200' preserveAspectRatio='xMinYMin\nslice'><path d='M263 601c.667 0 18 39.667 52 119s68.167\n 158.667 102.5 238 51.833 119.333 52.5 120C810 373.333 980.667 17.667 982 11\nc4.667-7.333 11-11 19-11h398999v40H1012.333L741 607c-38.667 80.667-84 175-136\n 283s-89.167 185.333-111.5 232-33.833 70.333-34.5 71c-4.667 4.667-12.333 7-23\n 7l-12-1-109-253c-72.667-168-109.333-252-110-252-10.667 8-22 16.667-34 26-22\n 17.333-33.333 26-34 26l-26-26 76-59 76-60zM1001 0h398999v40H1012z'/></svg>"),'2':Js("<svg viewBox='0 0 400000 1800' preserveAspectRatio='xMinYMin\nslice'><path d='M1001 0h398999v40H1013.084S929.667 308 749\n 880s-277 876.333-289 913c-4.667 4.667-12.667 7-24 7h-12c-1.333-3.333-3.667\n-11.667-7-25-35.333-125.333-106.667-373.333-214-744-10 12-21 25-33 39l-32 39\nc-6-5.333-15-14-27-26l25-30c26.667-32.667 52-63 76-91l52-60 208 722c56-175.333\n 126.333-397.333 211-666s153.833-488.167 207.5-658.5C944.167 129.167 975 32.667\n 983 10c4-6.667 10-10 18-10zm0 0h398999v40H1013z'/></svg>"),'3':Js("<svg viewBox='0 0 400000 2400' preserveAspectRatio='xMinYMin\nslice'><path d='M424 2398c-1.333-.667-38.5-172-111.5-514\nS202.667 1370.667 202 1370c0-2-10.667 14.333-32 49-4.667 7.333-9.833 15.667\n-15.5 25s-9.833 16-12.5 20l-5 7c-4-3.333-8.333-7.667-13-13l-13-13 76-122 77-121\n 209 968c0-2 84.667-361.667 254-1079C896.333 373.667 981.667 13.333 983 10\nc4-6.667 10-10 18-10h398999v40H1014.622S927.332 418.667 742 1206c-185.333\n 787.333-279.333 1182.333-282 1185-2 6-10 9-24 9-8 0-12-.667-12-2z\nM1001 0h398999v40H1014z'/></svg>"),'4':Js("<svg viewBox='0 0 400000 3000' preserveAspectRatio='xMinYMin\nslice'><path d='M473 2713C812.333 913.667 982.333 13 983 11\nc3.333-7.333 9.333-11 18-11h399110v40H1017.698S927.168 518 741.5 1506C555.833\n 2494 462 2989 460 2991c-2 6-10 9-24 9-8 0-12-.667-12-2s-5.333-32-16-92c-50.667\n-293.333-119.667-693.333-207-1200 0-1.333-5.333 8.667-16 30l-32 64-16 33-26-26\n 76-153 77-151c.667.667 35.667 202 105 604 67.333 400.667 102 602.667 104 606z\nM1001 0h398999v40H1017z'/></svg>"),'tall':Js("l-4 4-4 4c-.667.667-2 1.5-4 2.5s-4.167 1.833-6.5 2.5-5.5 1-9.5 1h\n-12l-28-84c-16.667-52-96.667 -294.333-240-727l-212 -643 -85 170c-4-3.333-8.333\n-7.667-13 -13l-13-13l77-155 77-156c66 199.333 139 419.667 219 661 l218 661z\nM702 0H400000v40H742z'/></svg>")})
        var.put('z', PyJs_Object_494_)
        @Js
        def PyJs_e_495_(t, r, a, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_495_}, var)
            var.registers(['i', 'l', 'r', 'n', 'u', 's', 'a', 't'])
            var.put('n', var.get('o').get('default').callprop('makeSpan', Js([]), Js([]), var.get('a')))
            var.put('i', var.get('a').get('sizeMultiplier'))
            if PyJsStrictEq(var.get('r').get('type'),Js('small')):
                var.put('l', var.get('a').callprop('havingBaseStyle', var.get('r').get('style')))
                var.put('i', (var.get('l').get('sizeMultiplier')/var.get('a').get('sizeMultiplier')))
                var.get('n').put('height', (Js(1.0)*var.get('i')))
                var.get('n').get('style').put('height', (var.get('n').get('height')+Js('em')))
                var.get('n').put('surdWidth', (Js(0.833)*var.get('i')))
                var.get('n').put('innerHTML', ((((Js("<svg width='100%' height='")+var.get('n').get('height'))+Js("em'>\n            "))+var.get('z').get('main'))+Js('</svg>')))
            else:
                if PyJsStrictEq(var.get('r').get('type'),Js('large')):
                    var.get('n').put('height', (var.get('N').get(var.get('r').get('size'))/var.get('i')))
                    var.get('n').get('style').put('height', (var.get('n').get('height')+Js('em')))
                    var.get('n').put('surdWidth', (Js(1.0)/var.get('i')))
                    var.get('n').put('innerHTML', ((((Js('<svg width="100%" height="')+var.get('n').get('height'))+Js('em">\n            '))+var.get('z').get(var.get('r').get('size')))+Js('</svg>')))
                else:
                    var.get('n').put('height', (var.get('t')/var.get('i')))
                    var.get('n').get('style').put('height', (var.get('n').get('height')+Js('em')))
                    var.get('n').put('surdWidth', (Js(1.056)/var.get('i')))
                    var.put('s', var.get('Math').callprop('floor', (var.get('n').get('height')*Js(1000.0))))
                    var.put('u', (var.get('s')-Js(54.0)))
                    var.get('n').put('innerHTML', ((((((((Js("<svg width='100%' height='")+var.get('n').get('height'))+Js("em'>\n            <svg viewBox='0 0 400000 "))+var.get('s'))+Js("'\n            preserveAspectRatio='xMinYMax slice'>\n            <path d='M702 0H400000v40H742v"))+var.get('u'))+Js('\n            '))+var.get('z').get('tall'))+Js('</svg>')))
            var.get('n').put('sizeMultiplier', var.get('i'))
            return var.get('n')
        PyJs_e_495_._set_name('e')
        var.put('S', PyJs_e_495_)
        var.put('A', Js([Js('('), Js(')'), Js('['), Js('\\lbrack'), Js(']'), Js('\\rbrack'), Js('\\{'), Js('\\lbrace'), Js('\\}'), Js('\\rbrace'), Js('\\lfloor'), Js('\\rfloor'), Js('\\lceil'), Js('\\rceil'), Js('\\surd')]))
        var.put('C', Js([Js('\\uparrow'), Js('\\downarrow'), Js('\\updownarrow'), Js('\\Uparrow'), Js('\\Downarrow'), Js('\\Updownarrow'), Js('|'), Js('\\|'), Js('\\vert'), Js('\\Vert'), Js('\\lvert'), Js('\\rvert'), Js('\\lVert'), Js('\\rVert'), Js('\\lgroup'), Js('\\rgroup'), Js('\\lmoustache'), Js('\\rmoustache')]))
        var.put('T', Js([Js('<'), Js('>'), Js('\\langle'), Js('\\rangle'), Js('/'), Js('\\backslash'), Js('\\lt'), Js('\\gt')]))
        var.put('N', Js([Js(0.0), Js(1.2), Js(1.8), Js(2.4), Js(3.0)]))
        @Js
        def PyJs_e_496_(t, r, a, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_496_}, var)
            var.registers(['i', 'r', 'l', 'a', 't'])
            if (PyJsStrictEq(var.get('t'),Js('<')) or PyJsStrictEq(var.get('t'),Js('\\lt'))):
                var.put('t', Js('\\langle'))
            else:
                if (PyJsStrictEq(var.get('t'),Js('>')) or PyJsStrictEq(var.get('t'),Js('\\gt'))):
                    var.put('t', Js('\\rangle'))
            if (var.get('d').get('default').callprop('contains', var.get('A'), var.get('t')) or var.get('d').get('default').callprop('contains', var.get('T'), var.get('t'))):
                return var.get('b')(var.get('t'), var.get('r'), Js(False), var.get('a'), var.get('i'), var.get('l'))
            else:
                if var.get('d').get('default').callprop('contains', var.get('C'), var.get('t')):
                    return var.get('M')(var.get('t'), var.get('N').get(var.get('r')), Js(False), var.get('a'), var.get('i'), var.get('l'))
                else:
                    PyJsTempException = JsToPyException(var.get('n').get('default').create(((Js("Illegal delimiter: '")+var.get('t'))+Js("'"))))
                    raise PyJsTempException
        PyJs_e_496_._set_name('e')
        var.put('R', PyJs_e_496_)
        PyJs_Object_497_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPTSCRIPT')})
        PyJs_Object_498_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPT')})
        PyJs_Object_499_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('TEXT')})
        PyJs_Object_500_ = Js({'type':Js('large'),'size':Js(1.0)})
        PyJs_Object_501_ = Js({'type':Js('large'),'size':Js(2.0)})
        PyJs_Object_502_ = Js({'type':Js('large'),'size':Js(3.0)})
        PyJs_Object_503_ = Js({'type':Js('large'),'size':Js(4.0)})
        var.put('q', Js([PyJs_Object_497_, PyJs_Object_498_, PyJs_Object_499_, PyJs_Object_500_, PyJs_Object_501_, PyJs_Object_502_, PyJs_Object_503_]))
        PyJs_Object_504_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPTSCRIPT')})
        PyJs_Object_505_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPT')})
        PyJs_Object_506_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('TEXT')})
        PyJs_Object_507_ = Js({'type':Js('stack')})
        var.put('_', Js([PyJs_Object_504_, PyJs_Object_505_, PyJs_Object_506_, PyJs_Object_507_]))
        PyJs_Object_508_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPTSCRIPT')})
        PyJs_Object_509_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('SCRIPT')})
        PyJs_Object_510_ = Js({'type':Js('small'),'style':var.get('l').get('default').get('TEXT')})
        PyJs_Object_511_ = Js({'type':Js('large'),'size':Js(1.0)})
        PyJs_Object_512_ = Js({'type':Js('large'),'size':Js(2.0)})
        PyJs_Object_513_ = Js({'type':Js('large'),'size':Js(3.0)})
        PyJs_Object_514_ = Js({'type':Js('large'),'size':Js(4.0)})
        PyJs_Object_515_ = Js({'type':Js('stack')})
        var.put('E', Js([PyJs_Object_508_, PyJs_Object_509_, PyJs_Object_510_, PyJs_Object_511_, PyJs_Object_512_, PyJs_Object_513_, PyJs_Object_514_, PyJs_Object_515_]))
        @Js
        def PyJs_e_516_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_516_}, var)
            var.registers(['t'])
            if PyJsStrictEq(var.get('t').get('type'),Js('small')):
                return Js('Main-Regular')
            else:
                if PyJsStrictEq(var.get('t').get('type'),Js('large')):
                    return ((Js('Size')+var.get('t').get('size'))+Js('-Regular'))
                else:
                    if PyJsStrictEq(var.get('t').get('type'),Js('stack')):
                        return Js('Size4-Regular')
        PyJs_e_516_._set_name('e')
        var.put('B', PyJs_e_516_)
        @Js
        def PyJs_e_517_(t, r, a, n, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'this':this, 'arguments':arguments, 'e':PyJs_e_517_}, var)
            var.registers(['i', 'l', 'r', 'o', 'n', 'u', 's', 'a', 't'])
            var.put('i', var.get('Math').callprop('min', Js(2.0), (Js(3.0)-var.get('n').get('style').get('size'))))
            #for JS loop
            var.put('l', var.get('i'))
            while (var.get('l')<var.get('a').get('length')):
                try:
                    if PyJsStrictEq(var.get('a').get(var.get('l')).get('type'),Js('stack')):
                        break
                    var.put('s', var.get('m')(var.get('t'), var.get('B')(var.get('a').get(var.get('l')))))
                    var.put('o', (var.get('s').get('height')+var.get('s').get('depth')))
                    if PyJsStrictEq(var.get('a').get(var.get('l')).get('type'),Js('small')):
                        var.put('u', var.get('n').callprop('havingBaseStyle', var.get('a').get(var.get('l')).get('style')))
                        var.put('o', var.get('u').get('sizeMultiplier'), '*')
                    if (var.get('o')>var.get('r')):
                        return var.get('a').get(var.get('l'))
                finally:
                        (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
            return var.get('a').get((var.get('a').get('length')-Js(1.0)))
        PyJs_e_517_._set_name('e')
        var.put('O', PyJs_e_517_)
        @Js
        def PyJs_e_518_(t, r, a, n, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_518_}, var)
            var.registers(['i', 'r', 'l', 'o', 'n', 's', 'a', 't'])
            if (PyJsStrictEq(var.get('t'),Js('<')) or PyJsStrictEq(var.get('t'),Js('\\lt'))):
                var.put('t', Js('\\langle'))
            else:
                if (PyJsStrictEq(var.get('t'),Js('>')) or PyJsStrictEq(var.get('t'),Js('\\gt'))):
                    var.put('t', Js('\\rangle'))
            var.put('s', PyJsComma(Js(0.0), Js(None)))
            if var.get('d').get('default').callprop('contains', var.get('T'), var.get('t')):
                var.put('s', var.get('q'))
            else:
                if var.get('d').get('default').callprop('contains', var.get('A'), var.get('t')):
                    var.put('s', var.get('E'))
                else:
                    var.put('s', var.get('_'))
            var.put('o', var.get('O')(var.get('t'), var.get('r'), var.get('s'), var.get('n')))
            if PyJsStrictEq(var.get('t'),Js('\\surd')):
                return var.get('S')(var.get('r'), var.get('o'), var.get('n'))
            else:
                if PyJsStrictEq(var.get('o').get('type'),Js('small')):
                    return var.get('x')(var.get('t'), var.get('o').get('style'), var.get('a'), var.get('n'), var.get('i'), var.get('l'))
                else:
                    if PyJsStrictEq(var.get('o').get('type'),Js('large')):
                        return var.get('b')(var.get('t'), var.get('o').get('size'), var.get('a'), var.get('n'), var.get('i'), var.get('l'))
                    else:
                        if PyJsStrictEq(var.get('o').get('type'),Js('stack')):
                            return var.get('M')(var.get('t'), var.get('r'), var.get('a'), var.get('n'), var.get('i'), var.get('l'))
        PyJs_e_518_._set_name('e')
        var.put('L', PyJs_e_518_)
        @Js
        def PyJs_e_519_(t, r, a, n, i, l, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'a':a, 'n':n, 'i':i, 'l':l, 'this':this, 'arguments':arguments, 'e':PyJs_e_519_}, var)
            var.registers(['i', 'r', 'l', 'c', 'o', 'n', 'u', 's', 'a', 'f', 't'])
            var.put('s', (var.get('n').callprop('fontMetrics').get('axisHeight')*var.get('n').get('sizeMultiplier')))
            var.put('o', Js(901.0))
            var.put('u', (Js(5.0)/var.get('n').callprop('fontMetrics').get('ptPerEm')))
            var.put('c', var.get('Math').callprop('max', (var.get('r')-var.get('s')), (var.get('a')+var.get('s'))))
            var.put('f', var.get('Math').callprop('max', ((var.get('c')/Js(500.0))*var.get('o')), ((Js(2.0)*var.get('c'))-var.get('u'))))
            return var.get('L')(var.get('t'), var.get('f'), Js(True), var.get('n'), var.get('i'), var.get('l'))
        PyJs_e_519_._set_name('e')
        var.put('P', PyJs_e_519_)
        PyJs_Object_520_ = Js({'sizedDelim':var.get('R'),'customSizedDelim':var.get('L'),'leftRightDelim':var.get('P')})
        var.get('t').put('exports', PyJs_Object_520_)
    PyJs_anonymous_483_._set_name('anonymous')
    PyJs_Object_521_ = Js({'./ParseError':Js(29.0),'./Style':Js(33.0),'./buildCommon':Js(34.0),'./fontMetrics':Js(41.0),'./symbols':Js(48.0),'./utils':Js(51.0)})
    @Js
    def PyJs_anonymous_522_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_f_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_523_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_523_)
        PyJsHoisted_f_.func_name = 'f'
        var.put('f', PyJsHoisted_f_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('f')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('f')(var.get('i')))
        var.put('s', var.get('e')(Js('./unicodeRegexes')))
        var.put('o', var.get('f')(var.get('s')))
        var.put('u', var.get('e')(Js('./utils')))
        var.put('c', var.get('f')(var.get('u')))
        pass
        @Js
        def PyJs_e_524_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_524_}, var)
            var.registers(['r', 't'])
            var.put('t', var.get('t').callprop('slice'))
            #for JS loop
            var.put('r', (var.get('t').get('length')-Js(1.0)))
            while (var.get('r')>=Js(0.0)):
                try:
                    if var.get('t').get(var.get('r')).neg():
                        var.get('t').callprop('splice', var.get('r'), Js(1.0))
                finally:
                        (var.put('r',Js(var.get('r').to_number())-Js(1))+Js(1))
            return var.get('t').callprop('join', Js(' '))
        PyJs_e_524_._set_name('e')
        var.put('h', PyJs_e_524_)
        @Js
        def PyJs_anonymous_525_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, a, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 'a', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('classes', (var.get('t') or Js([])))
                var.get(u"this").put('children', (var.get('r') or Js([])))
                var.get(u"this").put('height', Js(0.0))
                var.get(u"this").put('depth', Js(0.0))
                var.get(u"this").put('maxFontSize', Js(0.0))
                PyJs_Object_526_ = Js({})
                var.get(u"this").put('style', PyJs_Object_526_)
                PyJs_Object_527_ = Js({})
                var.get(u"this").put('attributes', PyJs_Object_527_)
                var.get(u"this").get('innerHTML')
                if var.get('a'):
                    if var.get('a').get('style').callprop('isTight'):
                        var.get(u"this").get('classes').callprop('push', Js('mtight'))
                    if var.get('a').callprop('getColor'):
                        var.get(u"this").get('style').put('color', var.get('a').callprop('getColor'))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_529_(t, r, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_529_}, var)
                var.registers(['r', 't'])
                var.get(u"this").get('attributes').put(var.get('t'), var.get('r'))
            PyJs_e_529_._set_name('e')
            PyJs_Object_528_ = Js({'key':Js('setAttribute'),'value':PyJs_e_529_})
            @Js
            def PyJs_e_531_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_531_}, var)
                var.registers(['t'])
                return Js(False)
            PyJs_e_531_._set_name('e')
            PyJs_Object_530_ = Js({'key':Js('tryCombine'),'value':PyJs_e_531_})
            @Js
            def PyJs_e_533_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_533_}, var)
                var.registers(['r', 'a', 'n', 't'])
                var.put('t', var.get('document').callprop('createElement', Js('span')))
                var.get('t').put('className', var.get('h')(var.get(u"this").get('classes')))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('r', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('style'), var.get('r')):
                        var.get('t').get('style').put(var.get('r'), var.get(u"this").get('style').get(var.get('r')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('a', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('a')):
                        var.get('t').callprop('setAttribute', var.get('a'), var.get(u"this").get('attributes').get(var.get('a')))
                if var.get(u"this").get('innerHTML'):
                    var.get('t').put('innerHTML', var.get(u"this").get('innerHTML'))
                #for JS loop
                var.put('n', Js(0.0))
                while (var.get('n')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('t').callprop('appendChild', var.get(u"this").get('children').get(var.get('n')).callprop('toNode'))
                    finally:
                            (var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1))
                return var.get('t')
            PyJs_e_533_._set_name('e')
            PyJs_Object_532_ = Js({'key':Js('toNode'),'value':PyJs_e_533_})
            @Js
            def PyJs_e_535_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_535_}, var)
                var.registers(['i', 'r', 'n', 'a', 't'])
                var.put('t', Js('<span'))
                if var.get(u"this").get('classes').get('length'):
                    var.put('t', Js(' class="'), '+')
                    var.put('t', var.get('c').get('default').callprop('escape', var.get('h')(var.get(u"this").get('classes'))), '+')
                    var.put('t', Js('"'), '+')
                var.put('r', Js(''))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('a', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('a')):
                        var.put('r', (((var.get('c').get('default').callprop('hyphenate', var.get('a'))+Js(':'))+var.get(u"this").get('style').get(var.get('a')))+Js(';')), '+')
                if var.get('r'):
                    var.put('t', ((Js(' style="')+var.get('c').get('default').callprop('escape', var.get('r')))+Js('"')), '+')
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('n', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('n')):
                        var.put('t', ((Js(' ')+var.get('n'))+Js('="')), '+')
                        var.put('t', var.get('c').get('default').callprop('escape', var.get(u"this").get('attributes').get(var.get('n'))), '+')
                        var.put('t', Js('"'), '+')
                var.put('t', Js('>'), '+')
                if var.get(u"this").get('innerHTML'):
                    var.put('t', var.get(u"this").get('innerHTML'), '+')
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('t', var.get(u"this").get('children').get(var.get('i')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('t', Js('</span>'), '+')
                return var.get('t')
            PyJs_e_535_._set_name('e')
            PyJs_Object_534_ = Js({'key':Js('toMarkup'),'value':PyJs_e_535_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_528_, PyJs_Object_530_, PyJs_Object_532_, PyJs_Object_534_]))
            return var.get('e')
        PyJs_anonymous_525_._set_name('anonymous')
        var.put('v', PyJs_anonymous_525_())
        @Js
        def PyJs_anonymous_536_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('children', (var.get('t') or Js([])))
                var.get(u"this").put('height', Js(0.0))
                var.get(u"this").put('depth', Js(0.0))
                var.get(u"this").put('maxFontSize', Js(0.0))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_538_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_538_}, var)
                var.registers(['r', 't'])
                var.put('t', var.get('document').callprop('createDocumentFragment'))
                #for JS loop
                var.put('r', Js(0.0))
                while (var.get('r')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('t').callprop('appendChild', var.get(u"this").get('children').get(var.get('r')).callprop('toNode'))
                    finally:
                            (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
                return var.get('t')
            PyJs_e_538_._set_name('e')
            PyJs_Object_537_ = Js({'key':Js('toNode'),'value':PyJs_e_538_})
            @Js
            def PyJs_e_540_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_540_}, var)
                var.registers(['r', 't'])
                var.put('t', Js(''))
                #for JS loop
                var.put('r', Js(0.0))
                while (var.get('r')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('t', var.get(u"this").get('children').get(var.get('r')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('r',Js(var.get('r').to_number())+Js(1))-Js(1))
                return var.get('t')
            PyJs_e_540_._set_name('e')
            PyJs_Object_539_ = Js({'key':Js('toMarkup'),'value':PyJs_e_540_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_537_, PyJs_Object_539_]))
            return var.get('e')
        PyJs_anonymous_536_._set_name('anonymous')
        var.put('d', PyJs_anonymous_536_())
        PyJs_Object_541_ = Js({'î':Js('ı̂'),'ï':Js('ı̈'),'í':Js('ı́'),'ì':Js('ı̀')})
        var.put('p', PyJs_Object_541_)
        @Js
        def PyJs_anonymous_542_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, a, i, l, s, u, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'a':a, 'i':i, 'l':l, 's':s, 'u':u, 'this':this, 'arguments':arguments}, var)
                var.registers(['i', 'r', 'l', 'u', 's', 'a', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('value', (var.get('t') or Js('')))
                var.get(u"this").put('height', (var.get('r') or Js(0.0)))
                var.get(u"this").put('depth', (var.get('a') or Js(0.0)))
                var.get(u"this").put('italic', (var.get('i') or Js(0.0)))
                var.get(u"this").put('skew', (var.get('l') or Js(0.0)))
                var.get(u"this").put('classes', (var.get('s') or Js([])))
                PyJs_Object_543_ = Js({})
                var.get(u"this").put('style', (var.get('u') or PyJs_Object_543_))
                var.get(u"this").put('maxFontSize', Js(0.0))
                if var.get('o').get('default').get('cjkRegex').callprop('test', var.get('t')):
                    if var.get('o').get('default').get('hangulRegex').callprop('test', var.get('t')):
                        var.get(u"this").get('classes').callprop('push', Js('hangul_fallback'))
                    else:
                        var.get(u"this").get('classes').callprop('push', Js('cjk_fallback'))
                if JsRegExp('/[\\xee\\xef\\xed\\xec]/').callprop('test', var.get(u"this").get('value')):
                    var.get(u"this").put('value', var.get('p').get(var.get(u"this").get('value')))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_t_545_(r, this, arguments, var=var):
                var = Scope({'r':r, 'this':this, 'arguments':arguments, 't':PyJs_t_545_}, var)
                var.registers(['a', 'n', 'r'])
                if (((((var.get('r').neg() or var.get('r').instanceof(var.get('e')).neg()) or (var.get(u"this").get('italic')>Js(0.0))) or PyJsStrictNeq(var.get('h')(var.get(u"this").get('classes')),var.get('h')(var.get('r').get('classes')))) or PyJsStrictNeq(var.get(u"this").get('skew'),var.get('r').get('skew'))) or PyJsStrictNeq(var.get(u"this").get('maxFontSize'),var.get('r').get('maxFontSize'))):
                    return Js(False)
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('a', PyJsTemp)
                    if (var.get(u"this").get('style').callprop('hasOwnProperty', var.get('a')) and PyJsStrictNeq(var.get(u"this").get('style').get(var.get('a')),var.get('r').get('style').get(var.get('a')))):
                        return Js(False)
                for PyJsTemp in var.get('r').get('style'):
                    var.put('n', PyJsTemp)
                    if (var.get('r').get('style').callprop('hasOwnProperty', var.get('n')) and PyJsStrictNeq(var.get(u"this").get('style').get(var.get('n')),var.get('r').get('style').get(var.get('n')))):
                        return Js(False)
                var.get(u"this").put('value', var.get('r').get('value'), '+')
                var.get(u"this").put('height', var.get('Math').callprop('max', var.get(u"this").get('height'), var.get('r').get('height')))
                var.get(u"this").put('depth', var.get('Math').callprop('max', var.get(u"this").get('depth'), var.get('r').get('depth')))
                var.get(u"this").put('italic', var.get('r').get('italic'))
                return Js(True)
            PyJs_t_545_._set_name('t')
            PyJs_Object_544_ = Js({'key':Js('tryCombine'),'value':PyJs_t_545_})
            @Js
            def PyJs_e_547_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_547_}, var)
                var.registers(['r', 'a', 't'])
                var.put('t', var.get('document').callprop('createTextNode', var.get(u"this").get('value')))
                var.put('r', var.get(u"null"))
                if (var.get(u"this").get('italic')>Js(0.0)):
                    var.put('r', var.get('document').callprop('createElement', Js('span')))
                    var.get('r').get('style').put('marginRight', (var.get(u"this").get('italic')+Js('em')))
                if (var.get(u"this").get('classes').get('length')>Js(0.0)):
                    var.put('r', (var.get('r') or var.get('document').callprop('createElement', Js('span'))))
                    var.get('r').put('className', var.get('h')(var.get(u"this").get('classes')))
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('a', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('a')):
                        var.put('r', (var.get('r') or var.get('document').callprop('createElement', Js('span'))))
                        var.get('r').get('style').put(var.get('a'), var.get(u"this").get('style').get(var.get('a')))
                if var.get('r'):
                    var.get('r').callprop('appendChild', var.get('t'))
                    return var.get('r')
                else:
                    return var.get('t')
            PyJs_e_547_._set_name('e')
            PyJs_Object_546_ = Js({'key':Js('toNode'),'value':PyJs_e_547_})
            @Js
            def PyJs_e_549_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_549_}, var)
                var.registers(['i', 'r', 'n', 'a', 't'])
                var.put('t', Js(False))
                var.put('r', Js('<span'))
                if var.get(u"this").get('classes').get('length'):
                    var.put('t', Js(True))
                    var.put('r', Js(' class="'), '+')
                    var.put('r', var.get('c').get('default').callprop('escape', var.get('h')(var.get(u"this").get('classes'))), '+')
                    var.put('r', Js('"'), '+')
                var.put('a', Js(''))
                if (var.get(u"this").get('italic')>Js(0.0)):
                    var.put('a', ((Js('margin-right:')+var.get(u"this").get('italic'))+Js('em;')), '+')
                for PyJsTemp in var.get(u"this").get('style'):
                    var.put('n', PyJsTemp)
                    if var.get(u"this").get('style').callprop('hasOwnProperty', var.get('n')):
                        var.put('a', (((var.get('c').get('default').callprop('hyphenate', var.get('n'))+Js(':'))+var.get(u"this").get('style').get(var.get('n')))+Js(';')), '+')
                if var.get('a'):
                    var.put('t', Js(True))
                    var.put('r', ((Js(' style="')+var.get('c').get('default').callprop('escape', var.get('a')))+Js('"')), '+')
                var.put('i', var.get('c').get('default').callprop('escape', var.get(u"this").get('value')))
                if var.get('t'):
                    var.put('r', Js('>'), '+')
                    var.put('r', var.get('i'), '+')
                    var.put('r', Js('</span>'), '+')
                    return var.get('r')
                else:
                    return var.get('i')
            PyJs_e_549_._set_name('e')
            PyJs_Object_548_ = Js({'key':Js('toMarkup'),'value':PyJs_e_549_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_544_, PyJs_Object_546_, PyJs_Object_548_]))
            return var.get('e')
        PyJs_anonymous_542_._set_name('anonymous')
        var.put('m', PyJs_anonymous_542_())
        PyJs_Object_550_ = Js({'span':var.get('v'),'documentFragment':var.get('d'),'symbolNode':var.get('m')})
        var.get('t').put('exports', PyJs_Object_550_)
    PyJs_anonymous_522_._set_name('anonymous')
    PyJs_Object_551_ = Js({'./unicodeRegexes':Js(49.0),'./utils':Js(51.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0)})
    @Js
    def PyJs_anonymous_552_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'c', 'o', 'n', 'u', 's', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_s_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_553_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_553_)
        PyJsHoisted_s_.func_name = 's'
        var.put('s', PyJsHoisted_s_)
        @Js
        def PyJsHoisted_o_(e, t, r, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'c', 'o', 'u', 's', 'e', 'a', 't'])
            var.put('a', Js([]))
            var.put('i', Js([var.get('a')]))
            var.put('s', Js([]))
            while Js(True):
                var.put('o', var.get('e').callprop('parseExpression', Js(False), var.get(u"null")))
                var.put('o', var.get('n').get('default').create(Js('ordgroup'), var.get('o'), var.get('e').get('mode')))
                if var.get('r'):
                    PyJs_Object_554_ = Js({'style':var.get('r'),'value':Js([var.get('o')])})
                    var.put('o', var.get('n').get('default').create(Js('styling'), PyJs_Object_554_, var.get('e').get('mode')))
                var.get('a').callprop('push', var.get('o'))
                var.put('u', var.get('e').get('nextToken').get('text'))
                if PyJsStrictEq(var.get('u'),Js('&')):
                    var.get('e').callprop('consume')
                else:
                    if PyJsStrictEq(var.get('u'),Js('\\end')):
                        break
                    else:
                        if (PyJsStrictEq(var.get('u'),Js('\\\\')) or PyJsStrictEq(var.get('u'),Js('\\cr'))):
                            var.put('c', var.get('e').callprop('parseFunction'))
                            var.get('s').callprop('push', var.get('c').get('value').get('size'))
                            var.put('a', Js([]))
                            var.get('i').callprop('push', var.get('a'))
                        else:
                            PyJsTempException = JsToPyException(var.get('l').get('default').create(Js('Expected & or \\\\ or \\end'), var.get('e').get('nextToken')))
                            raise PyJsTempException
            var.get('t').put('body', var.get('i'))
            var.get('t').put('rowGaps', var.get('s'))
            return var.get('n').get('default').create(var.get('t').get('type'), var.get('t'), var.get('e').get('mode'))
        PyJsHoisted_o_.func_name = 'o'
        var.put('o', PyJsHoisted_o_)
        @Js
        def PyJsHoisted_u_(e, r, a, this, arguments, var=var):
            var = Scope({'e':e, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a'])
            if PyJsStrictEq(var.get('e',throw=False).typeof(),Js('string')):
                var.put('e', Js([var.get('e')]))
            if PyJsStrictEq(var.get('r',throw=False).typeof(),Js('number')):
                PyJs_Object_555_ = Js({'numArgs':var.get('r')})
                var.put('r', PyJs_Object_555_)
            PyJs_Object_556_ = Js({'numArgs':(var.get('r').get('numArgs') or Js(0.0)),'argTypes':var.get('r').get('argTypes'),'greediness':Js(1.0),'allowedInText':var.get('r').get('allowedInText').neg().neg(),'numOptionalArgs':(var.get('r').get('numOptionalArgs') or Js(0.0)),'handler':var.get('a')})
            var.put('n', PyJs_Object_556_)
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('e').get('length')):
                try:
                    var.get('t').get('exports').put(var.get('e').get(var.get('i')), var.get('n'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
        PyJsHoisted_u_.func_name = 'u'
        var.put('u', PyJsHoisted_u_)
        @Js
        def PyJsHoisted_c_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            if PyJsStrictEq(var.get('e').callprop('substr', Js(0.0), Js(1.0)),Js('d')):
                return Js('display')
            else:
                return Js('text')
        PyJsHoisted_c_.func_name = 'c'
        var.put('c', PyJsHoisted_c_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./ParseNode')))
        var.put('n', var.get('s')(var.get('a')))
        var.put('i', var.get('e')(Js('./ParseError')))
        var.put('l', var.get('s')(var.get('i')))
        pass
        pass
        pass
        pass
        PyJs_Object_557_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_558_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('r', (var.get('r').get('value') if var.get('r').get('value').get('map') else Js([var.get('r')])))
            @Js
            def PyJs_anonymous_559_(e, this, arguments, var=var):
                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                var.registers(['e', 't'])
                var.put('t', var.get('e').get('value'))
                if PyJsStrictNeq(Js('lcr').callprop('indexOf', var.get('t')),(-Js(1.0))):
                    PyJs_Object_560_ = Js({'type':Js('align'),'align':var.get('t')})
                    return PyJs_Object_560_
                else:
                    if PyJsStrictEq(var.get('t'),Js('|')):
                        PyJs_Object_561_ = Js({'type':Js('separator'),'separator':Js('|')})
                        return PyJs_Object_561_
                PyJsTempException = JsToPyException(var.get('l').get('default').create((Js('Unknown column alignment: ')+var.get('e').get('value')), var.get('e')))
                raise PyJsTempException
            PyJs_anonymous_559_._set_name('anonymous')
            var.put('a', var.get('r').callprop('map', PyJs_anonymous_559_))
            PyJs_Object_562_ = Js({'type':Js('array'),'cols':var.get('a'),'hskipBeforeAndAfter':Js(True)})
            var.put('n', PyJs_Object_562_)
            var.put('n', var.get('o')(var.get('e').get('parser'), var.get('n'), var.get('c')(var.get('e').get('envName'))))
            return var.get('n')
        PyJs_anonymous_558_._set_name('anonymous')
        var.get('u')(Js([Js('array'), Js('darray')]), PyJs_Object_557_, PyJs_anonymous_558_)
        PyJs_Object_563_ = Js({})
        @Js
        def PyJs_anonymous_564_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            PyJs_Object_565_ = Js({'matrix':var.get(u"null"),'pmatrix':Js([Js('('), Js(')')]),'bmatrix':Js([Js('['), Js(']')]),'Bmatrix':Js([Js('\\{'), Js('\\}')]),'vmatrix':Js([Js('|'), Js('|')]),'Vmatrix':Js([Js('\\Vert'), Js('\\Vert')])})
            var.put('t', PyJs_Object_565_.get(var.get('e').get('envName')))
            PyJs_Object_566_ = Js({'type':Js('array'),'hskipBeforeAndAfter':Js(False)})
            var.put('r', PyJs_Object_566_)
            var.put('r', var.get('o')(var.get('e').get('parser'), var.get('r'), var.get('c')(var.get('e').get('envName'))))
            if var.get('t'):
                PyJs_Object_567_ = Js({'body':Js([var.get('r')]),'left':var.get('t').get('0'),'right':var.get('t').get('1')})
                var.put('r', var.get('n').get('default').create(Js('leftright'), PyJs_Object_567_, var.get('e').get('mode')))
            return var.get('r')
        PyJs_anonymous_564_._set_name('anonymous')
        var.get('u')(Js([Js('matrix'), Js('pmatrix'), Js('bmatrix'), Js('Bmatrix'), Js('vmatrix'), Js('Vmatrix')]), PyJs_Object_563_, PyJs_anonymous_564_)
        PyJs_Object_568_ = Js({})
        @Js
        def PyJs_anonymous_569_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            PyJs_Object_571_ = Js({'type':Js('align'),'align':Js('l'),'pregap':Js(0.0),'postgap':Js(1.0)})
            PyJs_Object_572_ = Js({'type':Js('align'),'align':Js('l'),'pregap':Js(0.0),'postgap':Js(0.0)})
            PyJs_Object_570_ = Js({'type':Js('array'),'arraystretch':Js(1.2),'cols':Js([PyJs_Object_571_, PyJs_Object_572_])})
            var.put('t', PyJs_Object_570_)
            var.put('t', var.get('o')(var.get('e').get('parser'), var.get('t'), var.get('c')(var.get('e').get('envName'))))
            PyJs_Object_573_ = Js({'body':Js([var.get('t')]),'left':Js('\\{'),'right':Js('.')})
            var.put('t', var.get('n').get('default').create(Js('leftright'), PyJs_Object_573_, var.get('e').get('mode')))
            return var.get('t')
        PyJs_anonymous_569_._set_name('anonymous')
        var.get('u')(Js([Js('cases'), Js('dcases')]), PyJs_Object_568_, PyJs_anonymous_569_)
        PyJs_Object_574_ = Js({})
        @Js
        def PyJs_anonymous_575_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'l', 's', 'e', 'a', 't'])
            PyJs_Object_576_ = Js({'type':Js('array'),'cols':Js([]),'addJot':Js(True)})
            var.put('t', PyJs_Object_576_)
            var.put('t', var.get('o')(var.get('e').get('parser'), var.get('t'), Js('display')))
            var.put('r', var.get('n').get('default').create(Js('ordgroup'), Js([]), var.get('e').get('mode')))
            var.put('a', Js(0.0))
            @Js
            def PyJs_anonymous_577_(e, this, arguments, var=var):
                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                var.registers(['e', 'n', 't'])
                #for JS loop
                var.put('t', Js(1.0))
                while (var.get('t')<var.get('e').get('length')):
                    try:
                        var.put('n', var.get('e').get(var.get('t')).get('value').get('value').get('0'))
                        var.get('n').get('value').callprop('unshift', var.get('r'))
                    finally:
                            var.put('t', Js(2.0), '+')
                if (var.get('a')<var.get('e').get('length')):
                    var.put('a', var.get('e').get('length'))
            PyJs_anonymous_577_._set_name('anonymous')
            var.get('t').get('value').get('body').callprop('forEach', PyJs_anonymous_577_)
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('a')):
                try:
                    var.put('l', Js('r'))
                    var.put('s', Js(0.0))
                    if PyJsStrictEq((var.get('i')%Js(2.0)),Js(1.0)):
                        var.put('l', Js('l'))
                    else:
                        if (var.get('i')>Js(0.0)):
                            var.put('s', Js(2.0))
                    PyJs_Object_578_ = Js({'type':Js('align'),'align':var.get('l'),'pregap':var.get('s'),'postgap':Js(0.0)})
                    var.get('t').get('value').get('cols').put(var.get('i'), PyJs_Object_578_)
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('t')
        PyJs_anonymous_575_._set_name('anonymous')
        var.get('u')(Js('aligned'), PyJs_Object_574_, PyJs_anonymous_575_)
        PyJs_Object_579_ = Js({})
        @Js
        def PyJs_anonymous_580_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            PyJs_Object_582_ = Js({'type':Js('align'),'align':Js('c')})
            PyJs_Object_581_ = Js({'type':Js('array'),'cols':Js([PyJs_Object_582_]),'addJot':Js(True)})
            var.put('t', PyJs_Object_581_)
            var.put('t', var.get('o')(var.get('e').get('parser'), var.get('t'), Js('display')))
            return var.get('t')
        PyJs_anonymous_580_._set_name('anonymous')
        var.get('u')(Js('gathered'), PyJs_Object_579_, PyJs_anonymous_580_)
    PyJs_anonymous_552_._set_name('anonymous')
    PyJs_Object_583_ = Js({'./ParseError':Js(29.0),'./ParseNode':Js(30.0)})
    @Js
    def PyJs_anonymous_584_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'c', 'o', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_l_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_585_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_585_)
        PyJsHoisted_l_.func_name = 'l'
        var.put('l', PyJsHoisted_l_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./unicodeRegexes')))
        var.put('n', var.get('e')(Js('./fontMetricsData')))
        var.put('i', var.get('l')(var.get('n')))
        pass
        PyJs_Object_586_ = Js({'slant':Js([Js(0.25), Js(0.25), Js(0.25)]),'space':Js([Js(0.0), Js(0.0), Js(0.0)]),'stretch':Js([Js(0.0), Js(0.0), Js(0.0)]),'shrink':Js([Js(0.0), Js(0.0), Js(0.0)]),'xHeight':Js([Js(0.431), Js(0.431), Js(0.431)]),'quad':Js([Js(1.0), Js(1.171), Js(1.472)]),'extraSpace':Js([Js(0.0), Js(0.0), Js(0.0)]),'num1':Js([Js(0.677), Js(0.732), Js(0.925)]),'num2':Js([Js(0.394), Js(0.384), Js(0.387)]),'num3':Js([Js(0.444), Js(0.471), Js(0.504)]),'denom1':Js([Js(0.686), Js(0.752), Js(1.025)]),'denom2':Js([Js(0.345), Js(0.344), Js(0.532)]),'sup1':Js([Js(0.413), Js(0.503), Js(0.504)]),'sup2':Js([Js(0.363), Js(0.431), Js(0.404)]),'sup3':Js([Js(0.289), Js(0.286), Js(0.294)]),'sub1':Js([Js(0.15), Js(0.143), Js(0.2)]),'sub2':Js([Js(0.247), Js(0.286), Js(0.4)]),'supDrop':Js([Js(0.386), Js(0.353), Js(0.494)]),'subDrop':Js([Js(0.05), Js(0.071), Js(0.1)]),'delim1':Js([Js(2.39), Js(1.7), Js(1.98)]),'delim2':Js([Js(1.01), Js(1.157), Js(1.42)]),'axisHeight':Js([Js(0.25), Js(0.25), Js(0.25)]),'defaultRuleThickness':Js([Js(0.04), Js(0.049), Js(0.049)]),'bigOpSpacing1':Js([Js(0.111), Js(0.111), Js(0.111)]),'bigOpSpacing2':Js([Js(0.166), Js(0.166), Js(0.166)]),'bigOpSpacing3':Js([Js(0.2), Js(0.2), Js(0.2)]),'bigOpSpacing4':Js([Js(0.6), Js(0.611), Js(0.611)]),'bigOpSpacing5':Js([Js(0.1), Js(0.143), Js(0.143)]),'sqrtRuleThickness':Js([Js(0.04), Js(0.04), Js(0.04)]),'ptPerEm':Js([Js(10.0), Js(10.0), Js(10.0)]),'doubleRuleSep':Js([Js(0.2), Js(0.2), Js(0.2)])})
        var.put('s', PyJs_Object_586_)
        PyJs_Object_587_ = Js({'À':Js('A'),'Á':Js('A'),'Â':Js('A'),'Ã':Js('A'),'Ä':Js('A'),'Å':Js('A'),'Æ':Js('A'),'Ç':Js('C'),'È':Js('E'),'É':Js('E'),'Ê':Js('E'),'Ë':Js('E'),'Ì':Js('I'),'Í':Js('I'),'Î':Js('I'),'Ï':Js('I'),'Ð':Js('D'),'Ñ':Js('N'),'Ò':Js('O'),'Ó':Js('O'),'Ô':Js('O'),'Õ':Js('O'),'Ö':Js('O'),'Ø':Js('O'),'Ù':Js('U'),'Ú':Js('U'),'Û':Js('U'),'Ü':Js('U'),'Ý':Js('Y'),'Þ':Js('o'),'ß':Js('B'),'à':Js('a'),'á':Js('a'),'â':Js('a'),'ã':Js('a'),'ä':Js('a'),'å':Js('a'),'æ':Js('a'),'ç':Js('c'),'è':Js('e'),'é':Js('e'),'ê':Js('e'),'ë':Js('e'),'ì':Js('i'),'í':Js('i'),'î':Js('i'),'ï':Js('i'),'ð':Js('d'),'ñ':Js('n'),'ò':Js('o'),'ó':Js('o'),'ô':Js('o'),'õ':Js('o'),'ö':Js('o'),'ø':Js('o'),'ù':Js('u'),'ú':Js('u'),'û':Js('u'),'ü':Js('u'),'ý':Js('y'),'þ':Js('o'),'ÿ':Js('y'),'А':Js('A'),'Б':Js('B'),'В':Js('B'),'Г':Js('F'),'Д':Js('A'),'Е':Js('E'),'Ж':Js('K'),'З':Js('3'),'И':Js('N'),'Й':Js('N'),'К':Js('K'),'Л':Js('N'),'М':Js('M'),'Н':Js('H'),'О':Js('O'),'П':Js('N'),'Р':Js('P'),'С':Js('C'),'Т':Js('T'),'У':Js('y'),'Ф':Js('O'),'Х':Js('X'),'Ц':Js('U'),'Ч':Js('h'),'Ш':Js('W'),'Щ':Js('W'),'Ъ':Js('B'),'Ы':Js('X'),'Ь':Js('B'),'Э':Js('3'),'Ю':Js('X'),'Я':Js('R'),'а':Js('a'),'б':Js('b'),'в':Js('a'),'г':Js('r'),'д':Js('y'),'е':Js('e'),'ж':Js('m'),'з':Js('e'),'и':Js('n'),'й':Js('n'),'к':Js('n'),'л':Js('n'),'м':Js('m'),'н':Js('n'),'о':Js('o'),'п':Js('n'),'р':Js('p'),'с':Js('c'),'т':Js('o'),'у':Js('y'),'ф':Js('b'),'х':Js('x'),'ц':Js('n'),'ч':Js('n'),'ш':Js('w'),'щ':Js('w'),'ъ':Js('a'),'ы':Js('m'),'ь':Js('a'),'э':Js('e'),'ю':Js('m'),'я':Js('r')})
        var.put('o', PyJs_Object_587_)
        @Js
        def PyJs_e_588_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_588_}, var)
            var.registers(['r', 'l', 'n', 't'])
            var.put('n', var.get('t').callprop('charCodeAt', Js(0.0)))
            if var.get('o').contains(var.get('t').get('0')):
                var.put('n', var.get('o').get(var.get('t').get('0')).callprop('charCodeAt', Js(0.0)))
            else:
                if var.get('a').get('cjkRegex').callprop('test', var.get('t').get('0')):
                    var.put('n', Js('M').callprop('charCodeAt', Js(0.0)))
            var.put('l', var.get('i').get('default').get(var.get('r')).get(var.get('n')))
            if var.get('l'):
                PyJs_Object_589_ = Js({'depth':var.get('l').get('0'),'height':var.get('l').get('1'),'italic':var.get('l').get('2'),'skew':var.get('l').get('3'),'width':var.get('l').get('4')})
                return PyJs_Object_589_
        PyJs_e_588_._set_name('e')
        var.put('u', PyJs_e_588_)
        PyJs_Object_590_ = Js({})
        var.put('c', PyJs_Object_590_)
        @Js
        def PyJs_e_591_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_591_}, var)
            var.registers(['r', 'a', 'n', 't'])
            var.put('r', PyJsComma(Js(0.0), Js(None)))
            if (var.get('t')>=Js(5.0)):
                var.put('r', Js(0.0))
            else:
                if (var.get('t')>=Js(3.0)):
                    var.put('r', Js(1.0))
                else:
                    var.put('r', Js(2.0))
            if var.get('c').get(var.get('r')).neg():
                PyJs_Object_592_ = Js({})
                var.put('a', var.get('c').put(var.get('r'), PyJs_Object_592_))
                for PyJsTemp in var.get('s'):
                    var.put('n', PyJsTemp)
                    if var.get('s').callprop('hasOwnProperty', var.get('n')):
                        var.get('a').put(var.get('n'), var.get('s').get(var.get('n')).get(var.get('r')))
                var.get('a').put('cssEmPerMu', (var.get('a').get('quad')/Js(18.0)))
            return var.get('c').get(var.get('r'))
        PyJs_e_591_._set_name('e')
        var.put('f', PyJs_e_591_)
        PyJs_Object_593_ = Js({'getFontMetrics':var.get('f'),'getCharacterMetrics':var.get('u')})
        var.get('t').put('exports', PyJs_Object_593_)
    PyJs_anonymous_584_._set_name('anonymous')
    PyJs_Object_594_ = Js({'./fontMetricsData':Js(42.0),'./unicodeRegexes':Js(49.0)})
    @Js
    def PyJs_anonymous_595_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['e', 'r', 't'])
        Js('use strict')
        PyJs_Object_597_ = Js({'65':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'70':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'74':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'79':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0)]),'80':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'81':Js([Js(0.16667), Js(0.68889), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'87':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'88':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'89':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'90':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'165':Js([Js(0.0), Js(0.675), Js(0.025), Js(0.0)]),'174':Js([Js(0.15559), Js(0.69224), Js(0.0), Js(0.0)]),'240':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'295':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.9), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.9), Js(0.0), Js(0.0)]),'989':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'1008':Js([Js(0.0), Js(0.43056), Js(0.04028), Js(0.0)]),'8245':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8487':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8498':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8502':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8503':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8504':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8513':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8592':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0)]),'8594':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0)]),'8602':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8603':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8606':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8608':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8610':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8611':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8619':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8620':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8621':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0)]),'8622':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8624':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8625':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8630':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'8631':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'8634':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8635':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8638':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8639':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8642':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8643':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8644':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8646':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8647':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8648':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8649':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8650':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8651':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8652':Js([Js(0.01354), Js(0.52239), Js(0.0), Js(0.0)]),'8653':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8654':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8655':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8666':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8667':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8669':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0)]),'8672':Js([(-Js(0.064)), Js(0.437), Js(0.0), Js(0.0)]),'8674':Js([(-Js(0.064)), Js(0.437), Js(0.0), Js(0.0)]),'8705':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'8708':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8709':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8717':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'8722':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0)]),'8724':Js([Js(0.08198), Js(0.69224), Js(0.0), Js(0.0)]),'8726':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8733':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8737':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8738':Js([Js(0.03517), Js(0.52239), Js(0.0), Js(0.0)]),'8739':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8740':Js([Js(0.25142), Js(0.74111), Js(0.0), Js(0.0)]),'8741':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8742':Js([Js(0.25142), Js(0.74111), Js(0.0), Js(0.0)]),'8756':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8757':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8764':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8765':Js([(-Js(0.13313)), Js(0.37788), Js(0.0), Js(0.0)]),'8769':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8770':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0)]),'8774':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8776':Js([(-Js(0.01688)), Js(0.48312), Js(0.0), Js(0.0)]),'8778':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8782':Js([Js(0.06062), Js(0.54986), Js(0.0), Js(0.0)]),'8783':Js([Js(0.06062), Js(0.54986), Js(0.0), Js(0.0)]),'8785':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8786':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8787':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8790':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8791':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0)]),'8796':Js([Js(0.08198), Js(0.91667), Js(0.0), Js(0.0)]),'8806':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'8807':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'8808':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'8809':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'8812':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'8814':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8815':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8816':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8817':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8818':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0)]),'8819':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0)]),'8822':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8823':Js([Js(0.1808), Js(0.675), Js(0.0), Js(0.0)]),'8828':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8829':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8830':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0)]),'8831':Js([Js(0.22958), Js(0.72958), Js(0.0), Js(0.0)]),'8832':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8833':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8840':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8841':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8842':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8843':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8847':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8848':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8858':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8859':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8861':Js([Js(0.08198), Js(0.58198), Js(0.0), Js(0.0)]),'8862':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'8863':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'8864':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'8865':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'8872':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8873':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8874':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8876':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8877':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8878':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8879':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8882':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8883':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8884':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8885':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8888':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8890':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'8891':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8892':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8901':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8903':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8905':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8906':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'8907':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8908':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8909':Js([(-Js(0.03598)), Js(0.46402), Js(0.0), Js(0.0)]),'8910':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8911':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8912':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8913':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8914':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8915':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'8916':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8918':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8919':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8920':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8921':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'8922':Js([Js(0.38569), Js(0.88569), Js(0.0), Js(0.0)]),'8923':Js([Js(0.38569), Js(0.88569), Js(0.0), Js(0.0)]),'8926':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8927':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'8928':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8929':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8934':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0)]),'8935':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0)]),'8936':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0)]),'8937':Js([Js(0.23222), Js(0.74111), Js(0.0), Js(0.0)]),'8938':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8939':Js([Js(0.20576), Js(0.70576), Js(0.0), Js(0.0)]),'8940':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8941':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'8994':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'8995':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'9416':Js([Js(0.15559), Js(0.69224), Js(0.0), Js(0.0)]),'9484':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'9488':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'9492':Js([Js(0.0), Js(0.37788), Js(0.0), Js(0.0)]),'9496':Js([Js(0.0), Js(0.37788), Js(0.0), Js(0.0)]),'9585':Js([Js(0.19444), Js(0.68889), Js(0.0), Js(0.0)]),'9586':Js([Js(0.19444), Js(0.74111), Js(0.0), Js(0.0)]),'9632':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'9633':Js([Js(0.0), Js(0.675), Js(0.0), Js(0.0)]),'9650':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'9651':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'9654':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'9660':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'9661':Js([Js(0.0), Js(0.54986), Js(0.0), Js(0.0)]),'9664':Js([Js(0.03517), Js(0.54986), Js(0.0), Js(0.0)]),'9674':Js([Js(0.11111), Js(0.69224), Js(0.0), Js(0.0)]),'9733':Js([Js(0.19444), Js(0.69224), Js(0.0), Js(0.0)]),'10003':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'10016':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'10731':Js([Js(0.11111), Js(0.69224), Js(0.0), Js(0.0)]),'10846':Js([Js(0.19444), Js(0.75583), Js(0.0), Js(0.0)]),'10877':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'10878':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'10885':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'10886':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'10887':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'10888':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'10889':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10890':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10891':Js([Js(0.48256), Js(0.98256), Js(0.0), Js(0.0)]),'10892':Js([Js(0.48256), Js(0.98256), Js(0.0), Js(0.0)]),'10901':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'10902':Js([Js(0.13667), Js(0.63667), Js(0.0), Js(0.0)]),'10933':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'10934':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'10935':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10936':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10937':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10938':Js([Js(0.26167), Js(0.75726), Js(0.0), Js(0.0)]),'10949':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'10950':Js([Js(0.25583), Js(0.75583), Js(0.0), Js(0.0)]),'10955':Js([Js(0.28481), Js(0.79383), Js(0.0), Js(0.0)]),'10956':Js([Js(0.28481), Js(0.79383), Js(0.0), Js(0.0)]),'57350':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'57351':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'57352':Js([Js(0.08167), Js(0.58167), Js(0.0), Js(0.0)]),'57353':Js([Js(0.0), Js(0.43056), Js(0.04028), Js(0.0)]),'57356':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57357':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57358':Js([Js(0.41951), Js(0.91951), Js(0.0), Js(0.0)]),'57359':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'57360':Js([Js(0.30274), Js(0.79383), Js(0.0), Js(0.0)]),'57361':Js([Js(0.41951), Js(0.91951), Js(0.0), Js(0.0)]),'57366':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57367':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57368':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57369':Js([Js(0.25142), Js(0.75726), Js(0.0), Js(0.0)]),'57370':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'57371':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)])})
        PyJs_Object_598_ = Js({'48':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'51':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'52':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'53':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'55':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'57':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.19445)]),'66':Js([Js(0.0), Js(0.68333), Js(0.03041), Js(0.13889)]),'67':Js([Js(0.0), Js(0.68333), Js(0.05834), Js(0.13889)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334)]),'69':Js([Js(0.0), Js(0.68333), Js(0.08944), Js(0.11111)]),'70':Js([Js(0.0), Js(0.68333), Js(0.09931), Js(0.11111)]),'71':Js([Js(0.09722), Js(0.68333), Js(0.0593), Js(0.11111)]),'72':Js([Js(0.0), Js(0.68333), Js(0.00965), Js(0.11111)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07382), Js(0.0)]),'74':Js([Js(0.09722), Js(0.68333), Js(0.18472), Js(0.16667)]),'75':Js([Js(0.0), Js(0.68333), Js(0.01445), Js(0.05556)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889)]),'77':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889)]),'78':Js([Js(0.0), Js(0.68333), Js(0.14736), Js(0.08334)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.11111)]),'80':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.08334)]),'81':Js([Js(0.09722), Js(0.68333), Js(0.0), Js(0.11111)]),'82':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334)]),'83':Js([Js(0.0), Js(0.68333), Js(0.075), Js(0.13889)]),'84':Js([Js(0.0), Js(0.68333), Js(0.25417), Js(0.0)]),'85':Js([Js(0.0), Js(0.68333), Js(0.09931), Js(0.08334)]),'86':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.0)]),'87':Js([Js(0.0), Js(0.68333), Js(0.08222), Js(0.08334)]),'88':Js([Js(0.0), Js(0.68333), Js(0.14643), Js(0.13889)]),'89':Js([Js(0.09722), Js(0.68333), Js(0.08222), Js(0.08334)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07944), Js(0.13889)])})
        PyJs_Object_599_ = Js({'33':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'34':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'38':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'39':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'40':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0)]),'41':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0)]),'42':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'43':Js([Js(0.08319), Js(0.58283), Js(0.0), Js(0.0)]),'44':Js([Js(0.0), Js(0.10803), Js(0.0), Js(0.0)]),'45':Js([Js(0.08319), Js(0.58283), Js(0.0), Js(0.0)]),'46':Js([Js(0.0), Js(0.10803), Js(0.0), Js(0.0)]),'47':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0)]),'48':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'51':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'52':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'53':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'55':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'57':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'58':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'59':Js([Js(0.12604), Js(0.47534), Js(0.0), Js(0.0)]),'61':Js([(-Js(0.13099)), Js(0.36866), Js(0.0), Js(0.0)]),'63':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'70':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'72':Js([Js(0.06302), Js(0.69141), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'74':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'79':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'80':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'81':Js([Js(0.03781), Js(0.69141), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'87':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'88':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'89':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'90':Js([Js(0.12604), Js(0.69141), Js(0.0), Js(0.0)]),'91':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0)]),'93':Js([Js(0.24982), Js(0.74947), Js(0.0), Js(0.0)]),'94':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'97':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'102':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'103':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'104':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'106':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'108':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'109':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'112':Js([Js(0.18906), Js(0.52396), Js(0.0), Js(0.0)]),'113':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'114':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'115':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.52396), Js(0.0), Js(0.0)]),'119':Js([Js(0.0), Js(0.52396), Js(0.0), Js(0.0)]),'120':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'121':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'122':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'8216':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'8217':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'58112':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'58113':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'58114':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'58115':Js([Js(0.18906), Js(0.69141), Js(0.0), Js(0.0)]),'58116':Js([Js(0.18906), Js(0.47534), Js(0.0), Js(0.0)]),'58117':Js([Js(0.0), Js(0.69141), Js(0.0), Js(0.0)]),'58118':Js([Js(0.0), Js(0.62119), Js(0.0), Js(0.0)]),'58119':Js([Js(0.0), Js(0.47534), Js(0.0), Js(0.0)])})
        PyJs_Object_600_ = Js({'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'43':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'44':Js([Js(0.19444), Js(0.15556), Js(0.0), Js(0.0)]),'45':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'46':Js([Js(0.0), Js(0.15556), Js(0.0), Js(0.0)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'48':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'51':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'52':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'53':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'55':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'57':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'58':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'59':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'60':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'61':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'62':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'70':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'74':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'79':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'80':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'81':Js([Js(0.19444), Js(0.68611), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.68611), Js(0.01597), Js(0.0)]),'87':Js([Js(0.0), Js(0.68611), Js(0.01597), Js(0.0)]),'88':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'89':Js([Js(0.0), Js(0.68611), Js(0.02875), Js(0.0)]),'90':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'92':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'95':Js([Js(0.31), Js(0.13444), Js(0.03194), Js(0.0)]),'96':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'102':Js([Js(0.0), Js(0.69444), Js(0.10903), Js(0.0)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.01597), Js(0.0)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'114':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.63492), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.44444), Js(0.01597), Js(0.0)]),'119':Js([Js(0.0), Js(0.44444), Js(0.01597), Js(0.0)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.01597), Js(0.0)]),'122':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'123':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'124':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'125':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'126':Js([Js(0.35), Js(0.34444), Js(0.0), Js(0.0)]),'168':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'172':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'175':Js([Js(0.0), Js(0.59611), Js(0.0), Js(0.0)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'177':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'180':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'215':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'247':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'305':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'711':Js([Js(0.0), Js(0.63194), Js(0.0), Js(0.0)]),'713':Js([Js(0.0), Js(0.59611), Js(0.0), Js(0.0)]),'714':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'729':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'768':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'769':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'772':Js([Js(0.0), Js(0.59611), Js(0.0), Js(0.0)]),'774':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'775':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'776':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'778':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'779':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'780':Js([Js(0.0), Js(0.63194), Js(0.0), Js(0.0)]),'824':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'915':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'916':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'923':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'928':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'931':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'933':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'934':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'936':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'937':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8224':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8225':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8242':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8407':Js([Js(0.0), Js(0.72444), Js(0.15486), Js(0.0)]),'8463':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8465':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8467':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8472':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'8476':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8501':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8592':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8593':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8594':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8595':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8596':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8597':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8598':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8599':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8600':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8601':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8636':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8637':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8640':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8641':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8656':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8657':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8658':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8659':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8660':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8661':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8704':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8706':Js([Js(0.0), Js(0.69444), Js(0.06389), Js(0.0)]),'8707':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8709':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'8711':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'8712':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8715':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8722':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8723':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8725':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8726':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8727':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0)]),'8728':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0)]),'8729':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0)]),'8730':Js([Js(0.18), Js(0.82), Js(0.0), Js(0.0)]),'8733':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'8734':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8739':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8741':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8743':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8744':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8745':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8746':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8747':Js([Js(0.19444), Js(0.69444), Js(0.12778), Js(0.0)]),'8764':Js([(-Js(0.10889)), Js(0.39111), Js(0.0), Js(0.0)]),'8768':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8771':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0)]),'8776':Js([Js(0.02444), Js(0.52444), Js(0.0), Js(0.0)]),'8781':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0)]),'8801':Js([Js(0.00222), Js(0.50222), Js(0.0), Js(0.0)]),'8804':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8805':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8810':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8811':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8826':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8827':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8834':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8835':Js([Js(0.08556), Js(0.58556), Js(0.0), Js(0.0)]),'8838':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8839':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8846':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8849':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8850':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'8851':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8852':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8853':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8854':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8855':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8856':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8857':Js([Js(0.13333), Js(0.63333), Js(0.0), Js(0.0)]),'8866':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8867':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8868':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8869':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8900':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0)]),'8901':Js([(-Js(0.02639)), Js(0.47361), Js(0.0), Js(0.0)]),'8902':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0)]),'8968':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8969':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8970':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8971':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8994':Js([(-Js(0.13889)), Js(0.36111), Js(0.0), Js(0.0)]),'8995':Js([(-Js(0.13889)), Js(0.36111), Js(0.0), Js(0.0)]),'9651':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9657':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0)]),'9661':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9667':Js([(-Js(0.02778)), Js(0.47222), Js(0.0), Js(0.0)]),'9711':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9824':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9825':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9826':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9827':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9837':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'9838':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9839':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'10216':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'10217':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'10815':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'10927':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)]),'10928':Js([Js(0.19667), Js(0.69667), Js(0.0), Js(0.0)])})
        PyJs_Object_601_ = Js({'33':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0)]),'34':Js([Js(0.0), Js(0.69444), Js(0.06961), Js(0.0)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.06616), Js(0.0)]),'37':Js([Js(0.05556), Js(0.75), Js(0.13639), Js(0.0)]),'38':Js([Js(0.0), Js(0.69444), Js(0.09694), Js(0.0)]),'39':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0)]),'40':Js([Js(0.25), Js(0.75), Js(0.16194), Js(0.0)]),'41':Js([Js(0.25), Js(0.75), Js(0.03694), Js(0.0)]),'42':Js([Js(0.0), Js(0.75), Js(0.14917), Js(0.0)]),'43':Js([Js(0.05667), Js(0.56167), Js(0.03694), Js(0.0)]),'44':Js([Js(0.19444), Js(0.10556), Js(0.0), Js(0.0)]),'45':Js([Js(0.0), Js(0.43056), Js(0.02826), Js(0.0)]),'46':Js([Js(0.0), Js(0.10556), Js(0.0), Js(0.0)]),'47':Js([Js(0.25), Js(0.75), Js(0.16194), Js(0.0)]),'48':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'49':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'50':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'51':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'52':Js([Js(0.19444), Js(0.64444), Js(0.13556), Js(0.0)]),'53':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'54':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'55':Js([Js(0.19444), Js(0.64444), Js(0.13556), Js(0.0)]),'56':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'57':Js([Js(0.0), Js(0.64444), Js(0.13556), Js(0.0)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0582), Js(0.0)]),'59':Js([Js(0.19444), Js(0.43056), Js(0.0582), Js(0.0)]),'61':Js([(-Js(0.13313)), Js(0.36687), Js(0.06616), Js(0.0)]),'63':Js([Js(0.0), Js(0.69444), Js(0.1225), Js(0.0)]),'64':Js([Js(0.0), Js(0.69444), Js(0.09597), Js(0.0)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0)]),'67':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0)]),'68':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0)]),'69':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0)]),'71':Js([Js(0.0), Js(0.68333), Js(0.08722), Js(0.0)]),'72':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0)]),'73':Js([Js(0.0), Js(0.68333), Js(0.15806), Js(0.0)]),'74':Js([Js(0.0), Js(0.68333), Js(0.14028), Js(0.0)]),'75':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0)]),'78':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0)]),'79':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0)]),'80':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.09403), Js(0.0)]),'82':Js([Js(0.0), Js(0.68333), Js(0.03868), Js(0.0)]),'83':Js([Js(0.0), Js(0.68333), Js(0.11972), Js(0.0)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0)]),'85':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0)]),'86':Js([Js(0.0), Js(0.68333), Js(0.18361), Js(0.0)]),'87':Js([Js(0.0), Js(0.68333), Js(0.18361), Js(0.0)]),'88':Js([Js(0.0), Js(0.68333), Js(0.15806), Js(0.0)]),'89':Js([Js(0.0), Js(0.68333), Js(0.19383), Js(0.0)]),'90':Js([Js(0.0), Js(0.68333), Js(0.14528), Js(0.0)]),'91':Js([Js(0.25), Js(0.75), Js(0.1875), Js(0.0)]),'93':Js([Js(0.25), Js(0.75), Js(0.10528), Js(0.0)]),'94':Js([Js(0.0), Js(0.69444), Js(0.06646), Js(0.0)]),'95':Js([Js(0.31), Js(0.12056), Js(0.09208), Js(0.0)]),'97':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.06312), Js(0.0)]),'99':Js([Js(0.0), Js(0.43056), Js(0.05653), Js(0.0)]),'100':Js([Js(0.0), Js(0.69444), Js(0.10333), Js(0.0)]),'101':Js([Js(0.0), Js(0.43056), Js(0.07514), Js(0.0)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.21194), Js(0.0)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0)]),'104':Js([Js(0.0), Js(0.69444), Js(0.07671), Js(0.0)]),'105':Js([Js(0.0), Js(0.65536), Js(0.1019), Js(0.0)]),'106':Js([Js(0.19444), Js(0.65536), Js(0.14467), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.10764), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.10333), Js(0.0)]),'109':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0)]),'110':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0)]),'111':Js([Js(0.0), Js(0.43056), Js(0.06312), Js(0.0)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.06312), Js(0.0)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0)]),'114':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0)]),'115':Js([Js(0.0), Js(0.43056), Js(0.08208), Js(0.0)]),'116':Js([Js(0.0), Js(0.61508), Js(0.09486), Js(0.0)]),'117':Js([Js(0.0), Js(0.43056), Js(0.07671), Js(0.0)]),'118':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0)]),'119':Js([Js(0.0), Js(0.43056), Js(0.10764), Js(0.0)]),'120':Js([Js(0.0), Js(0.43056), Js(0.12042), Js(0.0)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.08847), Js(0.0)]),'122':Js([Js(0.0), Js(0.43056), Js(0.12292), Js(0.0)]),'126':Js([Js(0.35), Js(0.31786), Js(0.11585), Js(0.0)]),'163':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778)]),'567':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'768':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'769':Js([Js(0.0), Js(0.69444), Js(0.09694), Js(0.0)]),'770':Js([Js(0.0), Js(0.69444), Js(0.06646), Js(0.0)]),'771':Js([Js(0.0), Js(0.66786), Js(0.11585), Js(0.0)]),'772':Js([Js(0.0), Js(0.56167), Js(0.10333), Js(0.0)]),'774':Js([Js(0.0), Js(0.69444), Js(0.10806), Js(0.0)]),'775':Js([Js(0.0), Js(0.66786), Js(0.11752), Js(0.0)]),'776':Js([Js(0.0), Js(0.66786), Js(0.10474), Js(0.0)]),'778':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'779':Js([Js(0.0), Js(0.69444), Js(0.1225), Js(0.0)]),'780':Js([Js(0.0), Js(0.62847), Js(0.08295), Js(0.0)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13305), Js(0.0)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.68333), Js(0.09403), Js(0.0)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.68333), Js(0.15294), Js(0.0)]),'928':Js([Js(0.0), Js(0.68333), Js(0.16389), Js(0.0)]),'931':Js([Js(0.0), Js(0.68333), Js(0.12028), Js(0.0)]),'933':Js([Js(0.0), Js(0.68333), Js(0.11111), Js(0.0)]),'934':Js([Js(0.0), Js(0.68333), Js(0.05986), Js(0.0)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11111), Js(0.0)]),'937':Js([Js(0.0), Js(0.68333), Js(0.10257), Js(0.0)]),'8211':Js([Js(0.0), Js(0.43056), Js(0.09208), Js(0.0)]),'8212':Js([Js(0.0), Js(0.43056), Js(0.09208), Js(0.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.12417), Js(0.0)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.1685), Js(0.0)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.06961), Js(0.0)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)])})
        PyJs_Object_602_ = Js({'32':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]),'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'43':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'44':Js([Js(0.19444), Js(0.10556), Js(0.0), Js(0.0)]),'45':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'46':Js([Js(0.0), Js(0.10556), Js(0.0), Js(0.0)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'48':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'51':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'52':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'53':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'55':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'57':Js([Js(0.0), Js(0.64444), Js(0.0), Js(0.0)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'59':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'60':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'61':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'62':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'70':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'74':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'79':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'80':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.68333), Js(0.01389), Js(0.0)]),'87':Js([Js(0.0), Js(0.68333), Js(0.01389), Js(0.0)]),'88':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'89':Js([Js(0.0), Js(0.68333), Js(0.025), Js(0.0)]),'90':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'92':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'95':Js([Js(0.31), Js(0.12056), Js(0.02778), Js(0.0)]),'96':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'102':Js([Js(0.0), Js(0.69444), Js(0.07778), Js(0.0)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.01389), Js(0.0)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.66786), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'114':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.43056), Js(0.01389), Js(0.0)]),'119':Js([Js(0.0), Js(0.43056), Js(0.01389), Js(0.0)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.01389), Js(0.0)]),'122':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'123':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'124':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'125':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'126':Js([Js(0.35), Js(0.31786), Js(0.0), Js(0.0)]),'160':Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]),'168':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'172':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'175':Js([Js(0.0), Js(0.56778), Js(0.0), Js(0.0)]),'176':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'177':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'180':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'215':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'247':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'567':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'711':Js([Js(0.0), Js(0.62847), Js(0.0), Js(0.0)]),'713':Js([Js(0.0), Js(0.56778), Js(0.0), Js(0.0)]),'714':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'715':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'728':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'729':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'730':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'768':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'769':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'772':Js([Js(0.0), Js(0.56778), Js(0.0), Js(0.0)]),'774':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'775':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'776':Js([Js(0.0), Js(0.66786), Js(0.0), Js(0.0)]),'778':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'779':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'780':Js([Js(0.0), Js(0.62847), Js(0.0), Js(0.0)]),'824':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'915':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'928':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'931':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'933':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'936':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'937':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'8211':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0)]),'8212':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8224':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8225':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8230':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0)]),'8242':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8407':Js([Js(0.0), Js(0.71444), Js(0.15382), Js(0.0)]),'8463':Js([Js(0.0), Js(0.68889), Js(0.0), Js(0.0)]),'8465':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8467':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.11111)]),'8472':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.11111)]),'8476':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8501':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8592':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8593':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8594':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8595':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8596':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8597':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8598':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8599':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8600':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8601':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8614':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'8617':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'8618':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'8636':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8637':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8640':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8641':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8652':Js([Js(0.011), Js(0.671), Js(0.0), Js(0.0)]),'8656':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8657':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8658':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8659':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8660':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8661':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8704':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8706':Js([Js(0.0), Js(0.69444), Js(0.05556), Js(0.08334)]),'8707':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8709':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'8711':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'8712':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8715':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8722':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8723':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8725':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8726':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8727':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0)]),'8728':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0)]),'8729':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0)]),'8730':Js([Js(0.2), Js(0.8), Js(0.0), Js(0.0)]),'8733':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'8734':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'8736':Js([Js(0.0), Js(0.69224), Js(0.0), Js(0.0)]),'8739':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8741':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8743':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8744':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8745':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8746':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8747':Js([Js(0.19444), Js(0.69444), Js(0.11111), Js(0.0)]),'8764':Js([(-Js(0.13313)), Js(0.36687), Js(0.0), Js(0.0)]),'8768':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'8771':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0)]),'8773':Js([(-Js(0.022)), Js(0.589), Js(0.0), Js(0.0)]),'8776':Js([(-Js(0.01688)), Js(0.48312), Js(0.0), Js(0.0)]),'8781':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0)]),'8784':Js([(-Js(0.133)), Js(0.67), Js(0.0), Js(0.0)]),'8800':Js([Js(0.215), Js(0.716), Js(0.0), Js(0.0)]),'8801':Js([(-Js(0.03625)), Js(0.46375), Js(0.0), Js(0.0)]),'8804':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8805':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8810':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8811':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8826':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8827':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8834':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8835':Js([Js(0.0391), Js(0.5391), Js(0.0), Js(0.0)]),'8838':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8839':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8846':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8849':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8850':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'8851':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8852':Js([Js(0.0), Js(0.55556), Js(0.0), Js(0.0)]),'8853':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8854':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8855':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8856':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8857':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'8866':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8867':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8868':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8869':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8872':Js([Js(0.249), Js(0.75), Js(0.0), Js(0.0)]),'8900':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0)]),'8901':Js([(-Js(0.05555)), Js(0.44445), Js(0.0), Js(0.0)]),'8902':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0)]),'8904':Js([Js(0.005), Js(0.505), Js(0.0), Js(0.0)]),'8942':Js([Js(0.03), Js(0.9), Js(0.0), Js(0.0)]),'8943':Js([(-Js(0.19)), Js(0.31), Js(0.0), Js(0.0)]),'8945':Js([(-Js(0.1)), Js(0.82), Js(0.0), Js(0.0)]),'8968':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8969':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8970':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8971':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'8994':Js([(-Js(0.14236)), Js(0.35764), Js(0.0), Js(0.0)]),'8995':Js([(-Js(0.14236)), Js(0.35764), Js(0.0), Js(0.0)]),'9136':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0)]),'9137':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0)]),'9651':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9657':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0)]),'9661':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9667':Js([(-Js(0.03472)), Js(0.46528), Js(0.0), Js(0.0)]),'9711':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9824':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9825':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9826':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9827':Js([Js(0.12963), Js(0.69444), Js(0.0), Js(0.0)]),'9837':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'9838':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'9839':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'10216':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'10217':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'10222':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0)]),'10223':Js([Js(0.244), Js(0.744), Js(0.0), Js(0.0)]),'10229':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'10230':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'10231':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'10232':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0)]),'10233':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0)]),'10234':Js([Js(0.024), Js(0.525), Js(0.0), Js(0.0)]),'10236':Js([Js(0.011), Js(0.511), Js(0.0), Js(0.0)]),'10815':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.0)]),'10927':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)]),'10928':Js([Js(0.13597), Js(0.63597), Js(0.0), Js(0.0)])})
        PyJs_Object_603_ = Js({'47':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.68611), Js(0.04835), Js(0.0)]),'67':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0)]),'68':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0)]),'69':Js([Js(0.0), Js(0.68611), Js(0.05451), Js(0.0)]),'70':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'71':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.68611), Js(0.08229), Js(0.0)]),'73':Js([Js(0.0), Js(0.68611), Js(0.07778), Js(0.0)]),'74':Js([Js(0.0), Js(0.68611), Js(0.10069), Js(0.0)]),'75':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0)]),'76':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0)]),'78':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0)]),'79':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0)]),'80':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'81':Js([Js(0.19444), Js(0.68611), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.68611), Js(0.00421), Js(0.0)]),'83':Js([Js(0.0), Js(0.68611), Js(0.05382), Js(0.0)]),'84':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'85':Js([Js(0.0), Js(0.68611), Js(0.11424), Js(0.0)]),'86':Js([Js(0.0), Js(0.68611), Js(0.25555), Js(0.0)]),'87':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'88':Js([Js(0.0), Js(0.68611), Js(0.07778), Js(0.0)]),'89':Js([Js(0.0), Js(0.68611), Js(0.25555), Js(0.0)]),'90':Js([Js(0.0), Js(0.68611), Js(0.06979), Js(0.0)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.11042), Js(0.0)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.69326), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.69326), Js(0.0622), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.01852), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0088), Js(0.0)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0)]),'114':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.63492), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0)]),'119':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0)]),'122':Js([Js(0.0), Js(0.44444), Js(0.04213), Js(0.0)]),'915':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'916':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.68611), Js(0.03194), Js(0.0)]),'923':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.68611), Js(0.07458), Js(0.0)]),'928':Js([Js(0.0), Js(0.68611), Js(0.08229), Js(0.0)]),'931':Js([Js(0.0), Js(0.68611), Js(0.05451), Js(0.0)]),'933':Js([Js(0.0), Js(0.68611), Js(0.15972), Js(0.0)]),'934':Js([Js(0.0), Js(0.68611), Js(0.0), Js(0.0)]),'936':Js([Js(0.0), Js(0.68611), Js(0.11653), Js(0.0)]),'937':Js([Js(0.0), Js(0.68611), Js(0.04835), Js(0.0)]),'945':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.03403), Js(0.0)]),'947':Js([Js(0.19444), Js(0.44444), Js(0.06389), Js(0.0)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03819), Js(0.0)]),'949':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.06215), Js(0.0)]),'951':Js([Js(0.19444), Js(0.44444), Js(0.03704), Js(0.0)]),'952':Js([Js(0.0), Js(0.69444), Js(0.03194), Js(0.0)]),'953':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'954':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'956':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'957':Js([Js(0.0), Js(0.44444), Js(0.06898), Js(0.0)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.03021), Js(0.0)]),'959':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'960':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0)]),'961':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'962':Js([Js(0.09722), Js(0.44444), Js(0.07917), Js(0.0)]),'963':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0)]),'964':Js([Js(0.0), Js(0.44444), Js(0.13472), Js(0.0)]),'965':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0)]),'966':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'967':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03704), Js(0.0)]),'969':Js([Js(0.0), Js(0.44444), Js(0.03704), Js(0.0)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'982':Js([Js(0.0), Js(0.44444), Js(0.03194), Js(0.0)]),'1009':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'1013':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)])})
        PyJs_Object_604_ = Js({'47':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889)]),'66':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334)]),'67':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.05556)]),'69':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334)]),'72':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.11111)]),'74':Js([Js(0.0), Js(0.68333), Js(0.09618), Js(0.16667)]),'75':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.05556)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.02778)]),'77':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334)]),'78':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334)]),'80':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.08334)]),'82':Js([Js(0.0), Js(0.68333), Js(0.00773), Js(0.08334)]),'83':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'85':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.02778)]),'86':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0)]),'87':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.0)]),'88':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.08334)]),'89':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.16667)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.10764), Js(0.16667)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.02778)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.65952), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.65952), Js(0.05724), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.03148), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.01968), Js(0.08334)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.08334)]),'114':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.05556)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.08334)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778)]),'118':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778)]),'119':Js([Js(0.0), Js(0.43056), Js(0.02691), Js(0.08334)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556)]),'122':Js([Js(0.0), Js(0.43056), Js(0.04398), Js(0.05556)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667)]),'920':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667)]),'926':Js([Js(0.0), Js(0.68333), Js(0.07569), Js(0.08334)]),'928':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556)]),'931':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'933':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.05556)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11), Js(0.05556)]),'937':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334)]),'945':Js([Js(0.0), Js(0.43056), Js(0.0037), Js(0.02778)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.05278), Js(0.08334)]),'947':Js([Js(0.19444), Js(0.43056), Js(0.05556), Js(0.0)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03785), Js(0.05556)]),'949':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.08334)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.07378), Js(0.08334)]),'951':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556)]),'952':Js([Js(0.0), Js(0.69444), Js(0.02778), Js(0.08334)]),'953':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'954':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'956':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.02778)]),'957':Js([Js(0.0), Js(0.43056), Js(0.06366), Js(0.02778)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.04601), Js(0.11111)]),'959':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'960':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'961':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'962':Js([Js(0.09722), Js(0.43056), Js(0.07986), Js(0.08334)]),'963':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'964':Js([Js(0.0), Js(0.43056), Js(0.1132), Js(0.02778)]),'965':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778)]),'966':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'967':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.05556)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03588), Js(0.11111)]),'969':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.08334)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.08334)]),'982':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0)]),'1009':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'1013':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)])})
        PyJs_Object_605_ = Js({'65':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.13889)]),'66':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334)]),'67':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334)]),'68':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.05556)]),'69':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'70':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'71':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334)]),'72':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556)]),'73':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.11111)]),'74':Js([Js(0.0), Js(0.68333), Js(0.09618), Js(0.16667)]),'75':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.05556)]),'76':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.02778)]),'77':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334)]),'78':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.08334)]),'79':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334)]),'80':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'81':Js([Js(0.19444), Js(0.68333), Js(0.0), Js(0.08334)]),'82':Js([Js(0.0), Js(0.68333), Js(0.00773), Js(0.08334)]),'83':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'84':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'85':Js([Js(0.0), Js(0.68333), Js(0.10903), Js(0.02778)]),'86':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0)]),'87':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.0)]),'88':Js([Js(0.0), Js(0.68333), Js(0.07847), Js(0.08334)]),'89':Js([Js(0.0), Js(0.68333), Js(0.22222), Js(0.0)]),'90':Js([Js(0.0), Js(0.68333), Js(0.07153), Js(0.08334)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.16667)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'102':Js([Js(0.19444), Js(0.69444), Js(0.10764), Js(0.16667)]),'103':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.02778)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.65952), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.65952), Js(0.05724), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.03148), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.01968), Js(0.08334)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'112':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'113':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.08334)]),'114':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.05556)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'116':Js([Js(0.0), Js(0.61508), Js(0.0), Js(0.08334)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778)]),'118':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778)]),'119':Js([Js(0.0), Js(0.43056), Js(0.02691), Js(0.08334)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.02778)]),'121':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556)]),'122':Js([Js(0.0), Js(0.43056), Js(0.04398), Js(0.05556)]),'915':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.08334)]),'916':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667)]),'920':Js([Js(0.0), Js(0.68333), Js(0.02778), Js(0.08334)]),'923':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.16667)]),'926':Js([Js(0.0), Js(0.68333), Js(0.07569), Js(0.08334)]),'928':Js([Js(0.0), Js(0.68333), Js(0.08125), Js(0.05556)]),'931':Js([Js(0.0), Js(0.68333), Js(0.05764), Js(0.08334)]),'933':Js([Js(0.0), Js(0.68333), Js(0.13889), Js(0.05556)]),'934':Js([Js(0.0), Js(0.68333), Js(0.0), Js(0.08334)]),'936':Js([Js(0.0), Js(0.68333), Js(0.11), Js(0.05556)]),'937':Js([Js(0.0), Js(0.68333), Js(0.05017), Js(0.08334)]),'945':Js([Js(0.0), Js(0.43056), Js(0.0037), Js(0.02778)]),'946':Js([Js(0.19444), Js(0.69444), Js(0.05278), Js(0.08334)]),'947':Js([Js(0.19444), Js(0.43056), Js(0.05556), Js(0.0)]),'948':Js([Js(0.0), Js(0.69444), Js(0.03785), Js(0.05556)]),'949':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.08334)]),'950':Js([Js(0.19444), Js(0.69444), Js(0.07378), Js(0.08334)]),'951':Js([Js(0.19444), Js(0.43056), Js(0.03588), Js(0.05556)]),'952':Js([Js(0.0), Js(0.69444), Js(0.02778), Js(0.08334)]),'953':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'954':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'955':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'956':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.02778)]),'957':Js([Js(0.0), Js(0.43056), Js(0.06366), Js(0.02778)]),'958':Js([Js(0.19444), Js(0.69444), Js(0.04601), Js(0.11111)]),'959':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)]),'960':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'961':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'962':Js([Js(0.09722), Js(0.43056), Js(0.07986), Js(0.08334)]),'963':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'964':Js([Js(0.0), Js(0.43056), Js(0.1132), Js(0.02778)]),'965':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.02778)]),'966':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'967':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.05556)]),'968':Js([Js(0.19444), Js(0.69444), Js(0.03588), Js(0.11111)]),'969':Js([Js(0.0), Js(0.43056), Js(0.03588), Js(0.0)]),'977':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.08334)]),'981':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.08334)]),'982':Js([Js(0.0), Js(0.43056), Js(0.02778), Js(0.0)]),'1009':Js([Js(0.19444), Js(0.43056), Js(0.0), Js(0.08334)]),'1013':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.05556)])})
        PyJs_Object_606_ = Js({'33':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'34':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'35':Js([Js(0.19444), Js(0.69444), Js(0.0), Js(0.0)]),'36':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'37':Js([Js(0.05556), Js(0.75), Js(0.0), Js(0.0)]),'38':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'39':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'40':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'41':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'42':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'43':Js([Js(0.08333), Js(0.58333), Js(0.0), Js(0.0)]),'44':Js([Js(0.125), Js(0.08333), Js(0.0), Js(0.0)]),'45':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'46':Js([Js(0.0), Js(0.08333), Js(0.0), Js(0.0)]),'47':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'48':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'51':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'52':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'53':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'55':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'57':Js([Js(0.0), Js(0.65556), Js(0.0), Js(0.0)]),'58':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'59':Js([Js(0.125), Js(0.44444), Js(0.0), Js(0.0)]),'61':Js([(-Js(0.13)), Js(0.37), Js(0.0), Js(0.0)]),'63':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'64':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'70':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'74':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'79':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'80':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'81':Js([Js(0.125), Js(0.69444), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.69444), Js(0.01389), Js(0.0)]),'87':Js([Js(0.0), Js(0.69444), Js(0.01389), Js(0.0)]),'88':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'89':Js([Js(0.0), Js(0.69444), Js(0.025), Js(0.0)]),'90':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'91':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'93':Js([Js(0.25), Js(0.75), Js(0.0), Js(0.0)]),'94':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'95':Js([Js(0.35), Js(0.09444), Js(0.02778), Js(0.0)]),'97':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'102':Js([Js(0.0), Js(0.69444), Js(0.06944), Js(0.0)]),'103':Js([Js(0.19444), Js(0.44444), Js(0.01389), Js(0.0)]),'104':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0)]),'106':Js([Js(0.19444), Js(0.67937), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'108':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'109':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'112':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'113':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'114':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0)]),'115':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.57143), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0)]),'119':Js([Js(0.0), Js(0.44444), Js(0.01389), Js(0.0)]),'120':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'121':Js([Js(0.19444), Js(0.44444), Js(0.01389), Js(0.0)]),'122':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'126':Js([Js(0.35), Js(0.32659), Js(0.0), Js(0.0)]),'305':Js([Js(0.0), Js(0.44444), Js(0.0), Js(0.0)]),'567':Js([Js(0.19444), Js(0.44444), Js(0.0), Js(0.0)]),'768':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'769':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.67659), Js(0.0), Js(0.0)]),'772':Js([Js(0.0), Js(0.60889), Js(0.0), Js(0.0)]),'774':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'775':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0)]),'776':Js([Js(0.0), Js(0.67937), Js(0.0), Js(0.0)]),'778':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'779':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'780':Js([Js(0.0), Js(0.63194), Js(0.0), Js(0.0)]),'915':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'916':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'923':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'928':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'931':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'933':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'934':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'936':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'937':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8211':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0)]),'8212':Js([Js(0.0), Js(0.44444), Js(0.02778), Js(0.0)]),'8216':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8217':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8220':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)]),'8221':Js([Js(0.0), Js(0.69444), Js(0.0), Js(0.0)])})
        PyJs_Object_607_ = Js({'65':Js([Js(0.0), Js(0.7), Js(0.22925), Js(0.0)]),'66':Js([Js(0.0), Js(0.7), Js(0.04087), Js(0.0)]),'67':Js([Js(0.0), Js(0.7), Js(0.1689), Js(0.0)]),'68':Js([Js(0.0), Js(0.7), Js(0.09371), Js(0.0)]),'69':Js([Js(0.0), Js(0.7), Js(0.18583), Js(0.0)]),'70':Js([Js(0.0), Js(0.7), Js(0.13634), Js(0.0)]),'71':Js([Js(0.0), Js(0.7), Js(0.17322), Js(0.0)]),'72':Js([Js(0.0), Js(0.7), Js(0.29694), Js(0.0)]),'73':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0)]),'74':Js([Js(0.27778), Js(0.7), Js(0.19189), Js(0.0)]),'75':Js([Js(0.0), Js(0.7), Js(0.31259), Js(0.0)]),'76':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0)]),'77':Js([Js(0.0), Js(0.7), Js(0.15981), Js(0.0)]),'78':Js([Js(0.0), Js(0.7), Js(0.3525), Js(0.0)]),'79':Js([Js(0.0), Js(0.7), Js(0.08078), Js(0.0)]),'80':Js([Js(0.0), Js(0.7), Js(0.08078), Js(0.0)]),'81':Js([Js(0.0), Js(0.7), Js(0.03305), Js(0.0)]),'82':Js([Js(0.0), Js(0.7), Js(0.06259), Js(0.0)]),'83':Js([Js(0.0), Js(0.7), Js(0.19189), Js(0.0)]),'84':Js([Js(0.0), Js(0.7), Js(0.29087), Js(0.0)]),'85':Js([Js(0.0), Js(0.7), Js(0.25815), Js(0.0)]),'86':Js([Js(0.0), Js(0.7), Js(0.27523), Js(0.0)]),'87':Js([Js(0.0), Js(0.7), Js(0.27523), Js(0.0)]),'88':Js([Js(0.0), Js(0.7), Js(0.26006), Js(0.0)]),'89':Js([Js(0.0), Js(0.7), Js(0.2939), Js(0.0)]),'90':Js([Js(0.0), Js(0.7), Js(0.24037), Js(0.0)])})
        PyJs_Object_608_ = Js({'40':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'41':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'47':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'91':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'92':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'93':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'123':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'125':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.72222), Js(0.0), Js(0.0)]),'8214':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0)]),'8593':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'8595':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'8657':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'8659':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'8719':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8720':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8721':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8730':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'8739':Js([(-Js(0.00599)), Js(0.606), Js(0.0), Js(0.0)]),'8741':Js([(-Js(0.00599)), Js(0.606), Js(0.0), Js(0.0)]),'8747':Js([Js(0.30612), Js(0.805), Js(0.19445), Js(0.0)]),'8748':Js([Js(0.306), Js(0.805), Js(0.19445), Js(0.0)]),'8749':Js([Js(0.306), Js(0.805), Js(0.19445), Js(0.0)]),'8750':Js([Js(0.30612), Js(0.805), Js(0.19445), Js(0.0)]),'8896':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8897':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8898':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8899':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'8968':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'8969':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'8970':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'8971':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'9168':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0)]),'10216':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'10217':Js([Js(0.35001), Js(0.85), Js(0.0), Js(0.0)]),'10752':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'10753':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'10754':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'10756':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)]),'10758':Js([Js(0.25001), Js(0.75), Js(0.0), Js(0.0)])})
        PyJs_Object_609_ = Js({'40':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'41':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'47':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'91':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'92':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'93':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'123':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'125':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'8719':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8720':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8721':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8730':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'8747':Js([Js(0.86225), Js(1.36), Js(0.44445), Js(0.0)]),'8748':Js([Js(0.862), Js(1.36), Js(0.44445), Js(0.0)]),'8749':Js([Js(0.862), Js(1.36), Js(0.44445), Js(0.0)]),'8750':Js([Js(0.86225), Js(1.36), Js(0.44445), Js(0.0)]),'8896':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8897':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8898':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8899':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'8968':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'8969':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'8970':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'8971':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'10216':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'10217':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'10752':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'10753':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'10754':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'10756':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)]),'10758':Js([Js(0.55001), Js(1.05), Js(0.0), Js(0.0)])})
        PyJs_Object_610_ = Js({'40':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'41':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'47':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'91':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'92':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'93':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'123':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'125':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.75), Js(0.0), Js(0.0)]),'8730':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'8968':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'8969':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'8970':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'8971':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'10216':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)]),'10217':Js([Js(0.95003), Js(1.45), Js(0.0), Js(0.0)])})
        PyJs_Object_611_ = Js({'40':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'41':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'47':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'91':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'92':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'93':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'123':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'125':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'710':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'732':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.825), Js(0.0), Js(0.0)]),'8730':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'8968':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'8969':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'8970':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'8971':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'9115':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9116':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'9117':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9118':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9119':Js([Js(1e-05), Js(0.6), Js(0.0), Js(0.0)]),'9120':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9121':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9122':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0)]),'9123':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9124':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9125':Js([(-Js(0.00099)), Js(0.601), Js(0.0), Js(0.0)]),'9126':Js([Js(0.64502), Js(1.155), Js(0.0), Js(0.0)]),'9127':Js([Js(1e-05), Js(0.9), Js(0.0), Js(0.0)]),'9128':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'9129':Js([Js(0.90001), Js(0.0), Js(0.0), Js(0.0)]),'9130':Js([Js(0.0), Js(0.3), Js(0.0), Js(0.0)]),'9131':Js([Js(1e-05), Js(0.9), Js(0.0), Js(0.0)]),'9132':Js([Js(0.65002), Js(1.15), Js(0.0), Js(0.0)]),'9133':Js([Js(0.90001), Js(0.0), Js(0.0), Js(0.0)]),'9143':Js([Js(0.88502), Js(0.915), Js(0.0), Js(0.0)]),'10216':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'10217':Js([Js(1.25003), Js(1.75), Js(0.0), Js(0.0)]),'57344':Js([(-Js(0.00499)), Js(0.605), Js(0.0), Js(0.0)]),'57345':Js([(-Js(0.00499)), Js(0.605), Js(0.0), Js(0.0)]),'57680':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0)]),'57681':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0)]),'57682':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0)]),'57683':Js([Js(0.0), Js(0.12), Js(0.0), Js(0.0)])})
        PyJs_Object_612_ = Js({'33':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'34':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'35':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'36':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'37':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'38':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'39':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'40':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'41':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'42':Js([Js(0.0), Js(0.52083), Js(0.0), Js(0.0)]),'43':Js([(-Js(0.08056)), Js(0.53055), Js(0.0), Js(0.0)]),'44':Js([Js(0.13889), Js(0.125), Js(0.0), Js(0.0)]),'45':Js([(-Js(0.08056)), Js(0.53055), Js(0.0), Js(0.0)]),'46':Js([Js(0.0), Js(0.125), Js(0.0), Js(0.0)]),'47':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'48':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'49':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'50':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'51':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'52':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'53':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'54':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'55':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'56':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'57':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'58':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'59':Js([Js(0.13889), Js(0.43056), Js(0.0), Js(0.0)]),'60':Js([(-Js(0.05556)), Js(0.55556), Js(0.0), Js(0.0)]),'61':Js([(-Js(0.19549)), Js(0.41562), Js(0.0), Js(0.0)]),'62':Js([(-Js(0.05556)), Js(0.55556), Js(0.0), Js(0.0)]),'63':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'64':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'65':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'66':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'67':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'68':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'69':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'70':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'71':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'72':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'73':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'74':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'75':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'76':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'77':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'78':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'79':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'80':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'81':Js([Js(0.13889), Js(0.61111), Js(0.0), Js(0.0)]),'82':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'83':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'84':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'85':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'86':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'87':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'88':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'89':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'90':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'91':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'92':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'93':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'94':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'95':Js([Js(0.09514), Js(0.0), Js(0.0), Js(0.0)]),'96':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'97':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'98':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'99':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'100':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'101':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'102':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'103':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0)]),'104':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'105':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'106':Js([Js(0.22222), Js(0.61111), Js(0.0), Js(0.0)]),'107':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'108':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'109':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'110':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'111':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'112':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0)]),'113':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0)]),'114':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'115':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'116':Js([Js(0.0), Js(0.55358), Js(0.0), Js(0.0)]),'117':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'118':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'119':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'120':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'121':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0)]),'122':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'123':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'124':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'125':Js([Js(0.08333), Js(0.69444), Js(0.0), Js(0.0)]),'126':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'127':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'305':Js([Js(0.0), Js(0.43056), Js(0.0), Js(0.0)]),'567':Js([Js(0.22222), Js(0.43056), Js(0.0), Js(0.0)]),'768':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'769':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'770':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'771':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'772':Js([Js(0.0), Js(0.56555), Js(0.0), Js(0.0)]),'774':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'776':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'778':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'780':Js([Js(0.0), Js(0.56597), Js(0.0), Js(0.0)]),'915':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'916':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'920':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'923':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'926':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'928':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'931':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'933':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'934':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'936':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'937':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'2018':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'2019':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)]),'8242':Js([Js(0.0), Js(0.61111), Js(0.0), Js(0.0)])})
        PyJs_Object_596_ = Js({'AMS-Regular':PyJs_Object_597_,'Caligraphic-Regular':PyJs_Object_598_,'Fraktur-Regular':PyJs_Object_599_,'Main-Bold':PyJs_Object_600_,'Main-Italic':PyJs_Object_601_,'Main-Regular':PyJs_Object_602_,'Math-BoldItalic':PyJs_Object_603_,'Math-Italic':PyJs_Object_604_,'Math-Regular':PyJs_Object_605_,'SansSerif-Regular':PyJs_Object_606_,'Script-Regular':PyJs_Object_607_,'Size1-Regular':PyJs_Object_608_,'Size2-Regular':PyJs_Object_609_,'Size3-Regular':PyJs_Object_610_,'Size4-Regular':PyJs_Object_611_,'Typewriter-Regular':PyJs_Object_612_})
        var.get('t').put('exports', PyJs_Object_596_)
    PyJs_anonymous_595_._set_name('anonymous')
    PyJs_Object_613_ = Js({})
    @Js
    def PyJs_anonymous_614_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'm', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_u_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_615_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_615_)
        PyJsHoisted_u_.func_name = 'u'
        var.put('u', PyJsHoisted_u_)
        @Js
        def PyJsHoisted_c_(e, r, a, this, arguments, var=var):
            var = Scope({'e':e, 'r':r, 'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a'])
            if PyJsStrictEq(var.get('e',throw=False).typeof(),Js('string')):
                var.put('e', Js([var.get('e')]))
            if PyJsStrictEq(var.get('r',throw=False).typeof(),Js('number')):
                PyJs_Object_616_ = Js({'numArgs':var.get('r')})
                var.put('r', PyJs_Object_616_)
            PyJs_Object_617_ = Js({'numArgs':var.get('r').get('numArgs'),'argTypes':var.get('r').get('argTypes'),'greediness':(Js(1.0) if PyJsStrictEq(var.get('r').get('greediness'),var.get('undefined')) else var.get('r').get('greediness')),'allowedInText':var.get('r').get('allowedInText').neg().neg(),'allowedInMath':var.get('r').get('allowedInMath'),'numOptionalArgs':(var.get('r').get('numOptionalArgs') or Js(0.0)),'infix':var.get('r').get('infix').neg().neg(),'handler':var.get('a')})
            var.put('n', PyJs_Object_617_)
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('e').get('length')):
                try:
                    var.get('t').get('exports').put(var.get('e').get(var.get('i')), var.get('n'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
        PyJsHoisted_c_.func_name = 'c'
        var.put('c', PyJsHoisted_c_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./utils')))
        var.put('n', var.get('u')(var.get('a')))
        var.put('i', var.get('e')(Js('./ParseError')))
        var.put('l', var.get('u')(var.get('i')))
        var.put('s', var.get('e')(Js('./ParseNode')))
        var.put('o', var.get('u')(var.get('s')))
        pass
        pass
        @Js
        def PyJs_e_618_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_618_}, var)
            var.registers(['t'])
            if PyJsStrictEq(var.get('t').get('type'),Js('ordgroup')):
                return var.get('t').get('value')
            else:
                return Js([var.get('t')])
        PyJs_e_618_._set_name('e')
        var.put('f', PyJs_e_618_)
        PyJs_Object_619_ = Js({'numArgs':Js(1.0),'numOptionalArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_620_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('t').get('1'))
            PyJs_Object_621_ = Js({'type':Js('sqrt'),'body':var.get('a'),'index':var.get('r')})
            return PyJs_Object_621_
        PyJs_anonymous_620_._set_name('anonymous')
        var.get('c')(Js('\\sqrt'), PyJs_Object_619_, PyJs_anonymous_620_)
        PyJs_Object_622_ = Js({'\\text':var.get('undefined'),'\\textrm':Js('mathrm'),'\\textsf':Js('mathsf'),'\\texttt':Js('mathtt'),'\\textnormal':Js('mathrm'),'\\textbf':Js('mathbf'),'\\textit':Js('textit')})
        var.put('h', PyJs_Object_622_)
        PyJs_Object_623_ = Js({'numArgs':Js(1.0),'argTypes':Js([Js('text')]),'greediness':Js(2.0),'allowedInText':Js(True)})
        @Js
        def PyJs_anonymous_624_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_625_ = Js({'type':Js('text'),'body':var.get('f')(var.get('r')),'style':var.get('h').get(var.get('e').get('funcName'))})
            return PyJs_Object_625_
        PyJs_anonymous_624_._set_name('anonymous')
        var.get('c')(Js([Js('\\text'), Js('\\textrm'), Js('\\textsf'), Js('\\texttt'), Js('\\textnormal'), Js('\\textbf'), Js('\\textit')]), PyJs_Object_623_, PyJs_anonymous_624_)
        PyJs_Object_626_ = Js({'numArgs':Js(2.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color'), Js('original')])})
        @Js
        def PyJs_anonymous_627_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('t').get('1'))
            PyJs_Object_628_ = Js({'type':Js('color'),'color':var.get('r').get('value'),'value':var.get('f')(var.get('a'))})
            return PyJs_Object_628_
        PyJs_anonymous_627_._set_name('anonymous')
        var.get('c')(Js('\\textcolor'), PyJs_Object_626_, PyJs_anonymous_627_)
        PyJs_Object_629_ = Js({'numArgs':Js(1.0),'allowedInText':Js(True),'greediness':Js(3.0),'argTypes':Js([Js('color')])})
        var.get('c')(Js('\\color'), PyJs_Object_629_, var.get(u"null"))
        PyJs_Object_630_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_631_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_632_ = Js({'type':Js('overline'),'body':var.get('r')})
            return PyJs_Object_632_
        PyJs_anonymous_631_._set_name('anonymous')
        var.get('c')(Js('\\overline'), PyJs_Object_630_, PyJs_anonymous_631_)
        PyJs_Object_633_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_634_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_635_ = Js({'type':Js('underline'),'body':var.get('r')})
            return PyJs_Object_635_
        PyJs_anonymous_634_._set_name('anonymous')
        var.get('c')(Js('\\underline'), PyJs_Object_633_, PyJs_anonymous_634_)
        PyJs_Object_636_ = Js({'numArgs':Js(2.0),'numOptionalArgs':Js(1.0),'argTypes':Js([Js('size'), Js('size'), Js('size')])})
        @Js
        def PyJs_anonymous_637_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('t').get('1'))
            var.put('n', var.get('t').get('2'))
            PyJs_Object_638_ = Js({'type':Js('rule'),'shift':(var.get('r') and var.get('r').get('value')),'width':var.get('a').get('value'),'height':var.get('n').get('value')})
            return PyJs_Object_638_
        PyJs_anonymous_637_._set_name('anonymous')
        var.get('c')(Js('\\rule'), PyJs_Object_636_, PyJs_anonymous_637_)
        PyJs_Object_639_ = Js({'numArgs':Js(1.0),'argTypes':Js([Js('size')])})
        @Js
        def PyJs_anonymous_640_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            PyJs_Object_641_ = Js({'type':Js('kern'),'dimension':var.get('t').get('0').get('value')})
            return PyJs_Object_641_
        PyJs_anonymous_640_._set_name('anonymous')
        var.get('c')(Js([Js('\\kern'), Js('\\mkern')]), PyJs_Object_639_, PyJs_anonymous_640_)
        PyJs_Object_642_ = Js({'numArgs':Js(0.0)})
        @Js
        def PyJs_anonymous_643_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_644_ = Js({'type':Js('katex')})
            return PyJs_Object_644_
        PyJs_anonymous_643_._set_name('anonymous')
        var.get('c')(Js('\\KaTeX'), PyJs_Object_642_, PyJs_anonymous_643_)
        PyJs_Object_645_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_646_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_647_ = Js({'type':Js('phantom'),'value':var.get('f')(var.get('r'))})
            return PyJs_Object_647_
        PyJs_anonymous_646_._set_name('anonymous')
        var.get('c')(Js('\\phantom'), PyJs_Object_645_, PyJs_anonymous_646_)
        PyJs_Object_648_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_649_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_650_ = Js({'type':Js('mclass'),'mclass':(Js('m')+var.get('e').get('funcName').callprop('substr', Js(5.0))),'value':var.get('f')(var.get('r'))})
            return PyJs_Object_650_
        PyJs_anonymous_649_._set_name('anonymous')
        var.get('c')(Js([Js('\\mathord'), Js('\\mathbin'), Js('\\mathrel'), Js('\\mathopen'), Js('\\mathclose'), Js('\\mathpunct'), Js('\\mathinner')]), PyJs_Object_648_, PyJs_anonymous_649_)
        PyJs_Object_651_ = Js({'numArgs':Js(2.0)})
        @Js
        def PyJs_anonymous_652_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('t').get('1'))
            PyJs_Object_653_ = Js({'type':Js('op'),'limits':Js(True),'alwaysHandleSupSub':Js(True),'symbol':Js(False),'value':var.get('f')(var.get('a'))})
            var.put('n', var.get('o').get('default').create(Js('op'), PyJs_Object_653_, var.get('a').get('mode')))
            PyJs_Object_654_ = Js({'base':var.get('n'),'sup':var.get('r'),'sub':var.get(u"null")})
            var.put('i', var.get('o').get('default').create(Js('supsub'), PyJs_Object_654_, var.get('r').get('mode')))
            PyJs_Object_655_ = Js({'type':Js('mclass'),'mclass':Js('mrel'),'value':Js([var.get('i')])})
            return PyJs_Object_655_
        PyJs_anonymous_652_._set_name('anonymous')
        var.get('c')(Js('\\stackrel'), PyJs_Object_651_, PyJs_anonymous_652_)
        PyJs_Object_656_ = Js({'numArgs':Js(0.0)})
        @Js
        def PyJs_anonymous_657_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            PyJs_Object_658_ = Js({'type':Js('mod'),'modType':Js('bmod'),'value':var.get(u"null")})
            return PyJs_Object_658_
        PyJs_anonymous_657_._set_name('anonymous')
        var.get('c')(Js('\\bmod'), PyJs_Object_656_, PyJs_anonymous_657_)
        PyJs_Object_659_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_660_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_661_ = Js({'type':Js('mod'),'modType':var.get('e').get('funcName').callprop('substr', Js(1.0)),'value':var.get('f')(var.get('r'))})
            return PyJs_Object_661_
        PyJs_anonymous_660_._set_name('anonymous')
        var.get('c')(Js([Js('\\pod'), Js('\\pmod'), Js('\\mod')]), PyJs_Object_659_, PyJs_anonymous_660_)
        PyJs_Object_663_ = Js({'mclass':Js('mopen'),'size':Js(1.0)})
        PyJs_Object_664_ = Js({'mclass':Js('mopen'),'size':Js(2.0)})
        PyJs_Object_665_ = Js({'mclass':Js('mopen'),'size':Js(3.0)})
        PyJs_Object_666_ = Js({'mclass':Js('mopen'),'size':Js(4.0)})
        PyJs_Object_667_ = Js({'mclass':Js('mclose'),'size':Js(1.0)})
        PyJs_Object_668_ = Js({'mclass':Js('mclose'),'size':Js(2.0)})
        PyJs_Object_669_ = Js({'mclass':Js('mclose'),'size':Js(3.0)})
        PyJs_Object_670_ = Js({'mclass':Js('mclose'),'size':Js(4.0)})
        PyJs_Object_671_ = Js({'mclass':Js('mrel'),'size':Js(1.0)})
        PyJs_Object_672_ = Js({'mclass':Js('mrel'),'size':Js(2.0)})
        PyJs_Object_673_ = Js({'mclass':Js('mrel'),'size':Js(3.0)})
        PyJs_Object_674_ = Js({'mclass':Js('mrel'),'size':Js(4.0)})
        PyJs_Object_675_ = Js({'mclass':Js('mord'),'size':Js(1.0)})
        PyJs_Object_676_ = Js({'mclass':Js('mord'),'size':Js(2.0)})
        PyJs_Object_677_ = Js({'mclass':Js('mord'),'size':Js(3.0)})
        PyJs_Object_678_ = Js({'mclass':Js('mord'),'size':Js(4.0)})
        PyJs_Object_662_ = Js({'\\bigl':PyJs_Object_663_,'\\Bigl':PyJs_Object_664_,'\\biggl':PyJs_Object_665_,'\\Biggl':PyJs_Object_666_,'\\bigr':PyJs_Object_667_,'\\Bigr':PyJs_Object_668_,'\\biggr':PyJs_Object_669_,'\\Biggr':PyJs_Object_670_,'\\bigm':PyJs_Object_671_,'\\Bigm':PyJs_Object_672_,'\\biggm':PyJs_Object_673_,'\\Biggm':PyJs_Object_674_,'\\big':PyJs_Object_675_,'\\Big':PyJs_Object_676_,'\\bigg':PyJs_Object_677_,'\\Bigg':PyJs_Object_678_})
        var.put('v', PyJs_Object_662_)
        var.put('d', Js([Js('('), Js(')'), Js('['), Js('\\lbrack'), Js(']'), Js('\\rbrack'), Js('\\{'), Js('\\lbrace'), Js('\\}'), Js('\\rbrace'), Js('\\lfloor'), Js('\\rfloor'), Js('\\lceil'), Js('\\rceil'), Js('<'), Js('>'), Js('\\langle'), Js('\\rangle'), Js('\\lt'), Js('\\gt'), Js('\\lvert'), Js('\\rvert'), Js('\\lVert'), Js('\\rVert'), Js('\\lgroup'), Js('\\rgroup'), Js('\\lmoustache'), Js('\\rmoustache'), Js('/'), Js('\\backslash'), Js('|'), Js('\\vert'), Js('\\|'), Js('\\Vert'), Js('\\uparrow'), Js('\\Uparrow'), Js('\\downarrow'), Js('\\Downarrow'), Js('\\updownarrow'), Js('\\Updownarrow'), Js('.')]))
        PyJs_Object_679_ = Js({'\\Bbb':Js('\\mathbb'),'\\bold':Js('\\mathbf'),'\\frak':Js('\\mathfrak')})
        var.put('p', PyJs_Object_679_)
        def PyJs_LONG_683_(var=var):
            PyJs_Object_680_ = Js({'numArgs':Js(1.0),'allowedInText':Js(True),'greediness':Js(3.0)})
            @Js
            def PyJs_anonymous_681_(e, t, this, arguments, var=var):
                var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['e', 'r', 't'])
                var.put('r', var.get('t').get('0'))
                PyJs_Object_682_ = Js({'type':Js('color'),'color':(Js('katex-')+var.get('e').get('funcName').callprop('slice', Js(1.0))),'value':var.get('f')(var.get('r'))})
                return PyJs_Object_682_
            PyJs_anonymous_681_._set_name('anonymous')
            return var.get('c')(Js([Js('\\blue'), Js('\\orange'), Js('\\pink'), Js('\\red'), Js('\\green'), Js('\\gray'), Js('\\purple'), Js('\\blueA'), Js('\\blueB'), Js('\\blueC'), Js('\\blueD'), Js('\\blueE'), Js('\\tealA'), Js('\\tealB'), Js('\\tealC'), Js('\\tealD'), Js('\\tealE'), Js('\\greenA'), Js('\\greenB'), Js('\\greenC'), Js('\\greenD'), Js('\\greenE'), Js('\\goldA'), Js('\\goldB'), Js('\\goldC'), Js('\\goldD'), Js('\\goldE'), Js('\\redA'), Js('\\redB'), Js('\\redC'), Js('\\redD'), Js('\\redE'), Js('\\maroonA'), Js('\\maroonB'), Js('\\maroonC'), Js('\\maroonD'), Js('\\maroonE'), Js('\\purpleA'), Js('\\purpleB'), Js('\\purpleC'), Js('\\purpleD'), Js('\\purpleE'), Js('\\mintA'), Js('\\mintB'), Js('\\mintC'), Js('\\grayA'), Js('\\grayB'), Js('\\grayC'), Js('\\grayD'), Js('\\grayE'), Js('\\grayF'), Js('\\grayG'), Js('\\grayH'), Js('\\grayI'), Js('\\kaBlue'), Js('\\kaGreen')]), PyJs_Object_680_, PyJs_anonymous_681_)
        PyJs_LONG_683_()
        def PyJs_LONG_687_(var=var):
            PyJs_Object_684_ = Js({'numArgs':Js(0.0)})
            @Js
            def PyJs_anonymous_685_(e, this, arguments, var=var):
                var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                var.registers(['e'])
                PyJs_Object_686_ = Js({'type':Js('op'),'limits':Js(False),'symbol':Js(False),'body':var.get('e').get('funcName')})
                return PyJs_Object_686_
            PyJs_anonymous_685_._set_name('anonymous')
            return var.get('c')(Js([Js('\\arcsin'), Js('\\arccos'), Js('\\arctan'), Js('\\arctg'), Js('\\arcctg'), Js('\\arg'), Js('\\ch'), Js('\\cos'), Js('\\cosec'), Js('\\cosh'), Js('\\cot'), Js('\\cotg'), Js('\\coth'), Js('\\csc'), Js('\\ctg'), Js('\\cth'), Js('\\deg'), Js('\\dim'), Js('\\exp'), Js('\\hom'), Js('\\ker'), Js('\\lg'), Js('\\ln'), Js('\\log'), Js('\\sec'), Js('\\sin'), Js('\\sinh'), Js('\\sh'), Js('\\tan'), Js('\\tanh'), Js('\\tg'), Js('\\th')]), PyJs_Object_684_, PyJs_anonymous_685_)
        PyJs_LONG_687_()
        PyJs_Object_688_ = Js({'numArgs':Js(0.0)})
        @Js
        def PyJs_anonymous_689_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_690_ = Js({'type':Js('op'),'limits':Js(True),'symbol':Js(False),'body':var.get('e').get('funcName')})
            return PyJs_Object_690_
        PyJs_anonymous_689_._set_name('anonymous')
        var.get('c')(Js([Js('\\det'), Js('\\gcd'), Js('\\inf'), Js('\\lim'), Js('\\liminf'), Js('\\limsup'), Js('\\max'), Js('\\min'), Js('\\Pr'), Js('\\sup')]), PyJs_Object_688_, PyJs_anonymous_689_)
        PyJs_Object_691_ = Js({'numArgs':Js(0.0)})
        @Js
        def PyJs_anonymous_692_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_693_ = Js({'type':Js('op'),'limits':Js(False),'symbol':Js(True),'body':var.get('e').get('funcName')})
            return PyJs_Object_693_
        PyJs_anonymous_692_._set_name('anonymous')
        var.get('c')(Js([Js('\\int'), Js('\\iint'), Js('\\iiint'), Js('\\oint')]), PyJs_Object_691_, PyJs_anonymous_692_)
        PyJs_Object_694_ = Js({'numArgs':Js(0.0)})
        @Js
        def PyJs_anonymous_695_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_696_ = Js({'type':Js('op'),'limits':Js(True),'symbol':Js(True),'body':var.get('e').get('funcName')})
            return PyJs_Object_696_
        PyJs_anonymous_695_._set_name('anonymous')
        var.get('c')(Js([Js('\\coprod'), Js('\\bigvee'), Js('\\bigwedge'), Js('\\biguplus'), Js('\\bigcap'), Js('\\bigcup'), Js('\\intop'), Js('\\prod'), Js('\\sum'), Js('\\bigotimes'), Js('\\bigoplus'), Js('\\bigodot'), Js('\\bigsqcup'), Js('\\smallint')]), PyJs_Object_694_, PyJs_anonymous_695_)
        PyJs_Object_697_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_698_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_699_ = Js({'type':Js('op'),'limits':Js(False),'symbol':Js(False),'value':var.get('f')(var.get('r'))})
            return PyJs_Object_699_
        PyJs_anonymous_698_._set_name('anonymous')
        var.get('c')(Js('\\mathop'), PyJs_Object_697_, PyJs_anonymous_698_)
        PyJs_Object_700_ = Js({'numArgs':Js(2.0),'greediness':Js(2.0)})
        @Js
        def PyJs_anonymous_701_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'l', 'r', 'n', 's', 'e', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('t').get('1'))
            var.put('n', PyJsComma(Js(0.0), Js(None)))
            var.put('i', var.get(u"null"))
            var.put('l', var.get(u"null"))
            var.put('s', Js('auto'))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('e').get('funcName'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dfrac')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\frac')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tfrac')):
                    SWITCHED = True
                    var.put('n', Js(True))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\\\atopfrac')):
                    SWITCHED = True
                    var.put('n', Js(False))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dbinom')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\binom')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tbinom')):
                    SWITCHED = True
                    var.put('n', Js(False))
                    var.put('i', Js('('))
                    var.put('l', Js(')'))
                    break
                if True:
                    SWITCHED = True
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('Unrecognized genfrac command')))
                    raise PyJsTempException
                SWITCHED = True
                break
            while 1:
                SWITCHED = False
                CONDITION = (var.get('e').get('funcName'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dfrac')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\dbinom')):
                    SWITCHED = True
                    var.put('s', Js('display'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tfrac')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\tbinom')):
                    SWITCHED = True
                    var.put('s', Js('text'))
                    break
                SWITCHED = True
                break
            PyJs_Object_702_ = Js({'type':Js('genfrac'),'numer':var.get('r'),'denom':var.get('a'),'hasBarLine':var.get('n'),'leftDelim':var.get('i'),'rightDelim':var.get('l'),'size':var.get('s')})
            return PyJs_Object_702_
        PyJs_anonymous_701_._set_name('anonymous')
        var.get('c')(Js([Js('\\dfrac'), Js('\\frac'), Js('\\tfrac'), Js('\\dbinom'), Js('\\binom'), Js('\\tbinom'), Js('\\\\atopfrac')]), PyJs_Object_700_, PyJs_anonymous_701_)
        PyJs_Object_703_ = Js({'numArgs':Js(1.0),'allowedInText':Js(True)})
        @Js
        def PyJs_anonymous_704_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_705_ = Js({'type':var.get('e').get('funcName').callprop('slice', Js(1.0)),'body':var.get('r')})
            return PyJs_Object_705_
        PyJs_anonymous_704_._set_name('anonymous')
        var.get('c')(Js([Js('\\llap'), Js('\\rlap')]), PyJs_Object_703_, PyJs_anonymous_704_)
        @Js
        def PyJs_e_706_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_706_}, var)
            var.registers(['r', 't'])
            if var.get('n').get('default').callprop('contains', var.get('d'), var.get('t').get('value')):
                return var.get('t')
            else:
                PyJsTempException = JsToPyException(var.get('l').get('default').create(((((Js("Invalid delimiter: '")+var.get('t').get('value'))+Js("' after '"))+var.get('r').get('funcName'))+Js("'")), var.get('t')))
                raise PyJsTempException
        PyJs_e_706_._set_name('e')
        var.put('m', PyJs_e_706_)
        PyJs_Object_707_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_708_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('m')(var.get('t').get('0'), var.get('e')))
            PyJs_Object_709_ = Js({'type':Js('delimsizing'),'size':var.get('v').get(var.get('e').get('funcName')).get('size'),'mclass':var.get('v').get(var.get('e').get('funcName')).get('mclass'),'value':var.get('r').get('value')})
            return PyJs_Object_709_
        PyJs_anonymous_708_._set_name('anonymous')
        var.get('c')(Js([Js('\\bigl'), Js('\\Bigl'), Js('\\biggl'), Js('\\Biggl'), Js('\\bigr'), Js('\\Bigr'), Js('\\biggr'), Js('\\Biggr'), Js('\\bigm'), Js('\\Bigm'), Js('\\biggm'), Js('\\Biggm'), Js('\\big'), Js('\\Big'), Js('\\bigg'), Js('\\Bigg')]), PyJs_Object_707_, PyJs_anonymous_708_)
        PyJs_Object_710_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_711_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('m')(var.get('t').get('0'), var.get('e')))
            PyJs_Object_712_ = Js({'type':Js('leftright'),'value':var.get('r').get('value')})
            return PyJs_Object_712_
        PyJs_anonymous_711_._set_name('anonymous')
        var.get('c')(Js([Js('\\left'), Js('\\right')]), PyJs_Object_710_, PyJs_anonymous_711_)
        PyJs_Object_713_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_714_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('m')(var.get('t').get('0'), var.get('e')))
            if var.get('e').get('parser').get('leftrightDepth').neg():
                PyJsTempException = JsToPyException(var.get('l').get('default').create(Js('\\middle without preceding \\left'), var.get('r')))
                raise PyJsTempException
            PyJs_Object_715_ = Js({'type':Js('middle'),'value':var.get('r').get('value')})
            return PyJs_Object_715_
        PyJs_anonymous_714_._set_name('anonymous')
        var.get('c')(Js('\\middle'), PyJs_Object_713_, PyJs_anonymous_714_)
        var.get('c')(Js([Js('\\tiny'), Js('\\scriptsize'), Js('\\footnotesize'), Js('\\small'), Js('\\normalsize'), Js('\\large'), Js('\\Large'), Js('\\LARGE'), Js('\\huge'), Js('\\Huge')]), Js(0.0), var.get(u"null"))
        var.get('c')(Js([Js('\\displaystyle'), Js('\\textstyle'), Js('\\scriptstyle'), Js('\\scriptscriptstyle')]), Js(0.0), var.get(u"null"))
        var.get('c')(Js([Js('\\rm'), Js('\\sf'), Js('\\tt'), Js('\\bf'), Js('\\it')]), Js(0.0), var.get(u"null"))
        PyJs_Object_716_ = Js({'numArgs':Js(1.0),'greediness':Js(2.0)})
        @Js
        def PyJs_anonymous_717_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            var.put('a', var.get('e').get('funcName'))
            if var.get('p').contains(var.get('a')):
                var.put('a', var.get('p').get(var.get('a')))
            PyJs_Object_718_ = Js({'type':Js('font'),'font':var.get('a').callprop('slice', Js(1.0)),'body':var.get('r')})
            return PyJs_Object_718_
        PyJs_anonymous_717_._set_name('anonymous')
        var.get('c')(Js([Js('\\mathrm'), Js('\\mathit'), Js('\\mathbf'), Js('\\mathbb'), Js('\\mathcal'), Js('\\mathfrak'), Js('\\mathscr'), Js('\\mathsf'), Js('\\mathtt'), Js('\\Bbb'), Js('\\bold'), Js('\\frak')]), PyJs_Object_716_, PyJs_anonymous_717_)
        def PyJs_LONG_722_(var=var):
            PyJs_Object_719_ = Js({'numArgs':Js(1.0)})
            @Js
            def PyJs_anonymous_720_(e, t, this, arguments, var=var):
                var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['i', 'r', 'e', 'a', 't'])
                var.put('r', var.get('t').get('0'))
                var.put('a', var.get('n').get('default').callprop('contains', Js([Js('\\acute'), Js('\\grave'), Js('\\ddot'), Js('\\tilde'), Js('\\bar'), Js('\\breve'), Js('\\check'), Js('\\hat'), Js('\\vec'), Js('\\dot')]), var.get('e').get('funcName')).neg())
                var.put('i', (var.get('a').neg() or var.get('n').get('default').callprop('contains', Js([Js('\\widehat'), Js('\\widetilde')]), var.get('e').get('funcName'))))
                PyJs_Object_721_ = Js({'type':Js('accent'),'label':var.get('e').get('funcName'),'isStretchy':var.get('a'),'isShifty':var.get('i'),'value':var.get('f')(var.get('r')),'base':var.get('r')})
                return PyJs_Object_721_
            PyJs_anonymous_720_._set_name('anonymous')
            return var.get('c')(Js([Js('\\acute'), Js('\\grave'), Js('\\ddot'), Js('\\tilde'), Js('\\bar'), Js('\\breve'), Js('\\check'), Js('\\hat'), Js('\\vec'), Js('\\dot'), Js('\\widehat'), Js('\\widetilde'), Js('\\overrightarrow'), Js('\\overleftarrow'), Js('\\Overrightarrow'), Js('\\overleftrightarrow'), Js('\\overgroup'), Js('\\overlinesegment'), Js('\\overleftharpoon'), Js('\\overrightharpoon')]), PyJs_Object_719_, PyJs_anonymous_720_)
        PyJs_LONG_722_()
        PyJs_Object_723_ = Js({'numArgs':Js(1.0),'allowedInText':Js(True),'allowedInMath':Js(False)})
        @Js
        def PyJs_anonymous_724_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_725_ = Js({'type':Js('accent'),'label':var.get('e').get('funcName'),'isStretchy':Js(False),'isShifty':Js(True),'value':var.get('f')(var.get('r')),'base':var.get('r')})
            return PyJs_Object_725_
        PyJs_anonymous_724_._set_name('anonymous')
        var.get('c')(Js([Js("\\'"), Js('\\`'), Js('\\^'), Js('\\~'), Js('\\='), Js('\\u'), Js('\\.'), Js('\\"'), Js('\\r'), Js('\\H'), Js('\\v')]), PyJs_Object_723_, PyJs_anonymous_724_)
        PyJs_Object_726_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_727_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_728_ = Js({'type':Js('horizBrace'),'label':var.get('e').get('funcName'),'isOver':JsRegExp('/^\\\\over/').callprop('test', var.get('e').get('funcName')),'base':var.get('r')})
            return PyJs_Object_728_
        PyJs_anonymous_727_._set_name('anonymous')
        var.get('c')(Js([Js('\\overbrace'), Js('\\underbrace')]), PyJs_Object_726_, PyJs_anonymous_727_)
        PyJs_Object_729_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_730_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_731_ = Js({'type':Js('accentUnder'),'label':var.get('e').get('funcName'),'value':var.get('f')(var.get('r')),'body':var.get('r')})
            return PyJs_Object_731_
        PyJs_anonymous_730_._set_name('anonymous')
        var.get('c')(Js([Js('\\underleftarrow'), Js('\\underrightarrow'), Js('\\underleftrightarrow'), Js('\\undergroup'), Js('\\underlinesegment'), Js('\\undertilde')]), PyJs_Object_729_, PyJs_anonymous_730_)
        def PyJs_LONG_735_(var=var):
            PyJs_Object_732_ = Js({'numArgs':Js(1.0),'numOptionalArgs':Js(1.0)})
            @Js
            def PyJs_anonymous_733_(e, t, this, arguments, var=var):
                var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['e', 'r', 'a', 't'])
                var.put('r', var.get('t').get('0'))
                var.put('a', var.get('t').get('1'))
                PyJs_Object_734_ = Js({'type':Js('xArrow'),'label':var.get('e').get('funcName'),'body':var.get('a'),'below':var.get('r')})
                return PyJs_Object_734_
            PyJs_anonymous_733_._set_name('anonymous')
            return var.get('c')(Js([Js('\\xleftarrow'), Js('\\xrightarrow'), Js('\\xLeftarrow'), Js('\\xRightarrow'), Js('\\xleftrightarrow'), Js('\\xLeftrightarrow'), Js('\\xhookleftarrow'), Js('\\xhookrightarrow'), Js('\\xmapsto'), Js('\\xrightharpoondown'), Js('\\xrightharpoonup'), Js('\\xleftharpoondown'), Js('\\xleftharpoonup'), Js('\\xrightleftharpoons'), Js('\\xleftrightharpoons'), Js('\\xLongequal'), Js('\\xtwoheadrightarrow'), Js('\\xtwoheadleftarrow'), Js('\\xLongequal'), Js('\\xtofrom')]), PyJs_Object_732_, PyJs_anonymous_733_)
        PyJs_LONG_735_()
        PyJs_Object_736_ = Js({'numArgs':Js(1.0)})
        @Js
        def PyJs_anonymous_737_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_738_ = Js({'type':Js('enclose'),'label':var.get('e').get('funcName'),'body':var.get('r')})
            return PyJs_Object_738_
        PyJs_anonymous_737_._set_name('anonymous')
        var.get('c')(Js([Js('\\cancel'), Js('\\bcancel'), Js('\\xcancel'), Js('\\sout'), Js('\\fbox')]), PyJs_Object_736_, PyJs_anonymous_737_)
        PyJs_Object_739_ = Js({'numArgs':Js(0.0),'infix':Js(True)})
        @Js
        def PyJs_anonymous_740_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 't'])
            var.put('t', PyJsComma(Js(0.0), Js(None)))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('e').get('funcName'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\over')):
                    SWITCHED = True
                    var.put('t', Js('\\frac'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\choose')):
                    SWITCHED = True
                    var.put('t', Js('\\binom'))
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('\\atop')):
                    SWITCHED = True
                    var.put('t', Js('\\\\atopfrac'))
                    break
                if True:
                    SWITCHED = True
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('Unrecognized infix genfrac command')))
                    raise PyJsTempException
                SWITCHED = True
                break
            PyJs_Object_741_ = Js({'type':Js('infix'),'replaceWith':var.get('t'),'token':var.get('e').get('token')})
            return PyJs_Object_741_
        PyJs_anonymous_740_._set_name('anonymous')
        var.get('c')(Js([Js('\\over'), Js('\\choose'), Js('\\atop')]), PyJs_Object_739_, PyJs_anonymous_740_)
        PyJs_Object_742_ = Js({'numArgs':Js(0.0),'numOptionalArgs':Js(1.0),'argTypes':Js([Js('size')])})
        @Js
        def PyJs_anonymous_743_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r', 't'])
            var.put('r', var.get('t').get('0'))
            PyJs_Object_744_ = Js({'type':Js('cr'),'size':var.get('r')})
            return PyJs_Object_744_
        PyJs_anonymous_743_._set_name('anonymous')
        var.get('c')(Js([Js('\\\\'), Js('\\cr')]), PyJs_Object_742_, PyJs_anonymous_743_)
        PyJs_Object_745_ = Js({'numArgs':Js(1.0),'argTypes':Js([Js('text')])})
        @Js
        def PyJs_anonymous_746_(e, t, this, arguments, var=var):
            var = Scope({'e':e, 't':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'n', 'e', 'a', 't'])
            var.put('r', var.get('t').get('0'))
            if PyJsStrictNeq(var.get('r').get('type'),Js('ordgroup')):
                PyJsTempException = JsToPyException(var.get('l').get('default').create(Js('Invalid environment name'), var.get('r')))
                raise PyJsTempException
            var.put('a', Js(''))
            #for JS loop
            var.put('n', Js(0.0))
            while (var.get('n')<var.get('r').get('value').get('length')):
                try:
                    var.put('a', var.get('r').get('value').get(var.get('n')).get('value'), '+')
                finally:
                        var.put('n',Js(var.get('n').to_number())+Js(1))
            PyJs_Object_747_ = Js({'type':Js('environment'),'name':var.get('a'),'nameGroup':var.get('r')})
            return PyJs_Object_747_
        PyJs_anonymous_746_._set_name('anonymous')
        var.get('c')(Js([Js('\\begin'), Js('\\end')]), PyJs_Object_745_, PyJs_anonymous_746_)
    PyJs_anonymous_614_._set_name('anonymous')
    PyJs_Object_748_ = Js({'./ParseError':Js(29.0),'./ParseNode':Js(30.0),'./utils':Js(51.0)})
    @Js
    def PyJs_anonymous_749_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_a_(e, r, this, arguments, var=var):
            var = Scope({'e':e, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['e', 'r'])
            var.get('t').get('exports').put(var.get('e'), var.get('r'))
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        Js('use strict')
        pass
        var.get('a')(Js('\\bgroup'), Js('{'))
        var.get('a')(Js('\\egroup'), Js('}'))
        var.get('a')(Js('\\begingroup'), Js('{'))
        var.get('a')(Js('\\endgroup'), Js('}'))
        var.get('a')(Js('\\mkern'), Js('\\kern'))
        var.get('a')(Js('\\overset'), Js('\\mathop{#2}\\limits^{#1}'))
        var.get('a')(Js('\\underset'), Js('\\mathop{#2}\\limits_{#1}'))
        var.get('a')(Js('\\boxed'), Js('\\fbox{\\displaystyle{#1}}'))
        var.get('a')(Js('\\iff'), Js('\\;\\Longleftrightarrow\\;'))
        var.get('a')(Js('\\implies'), Js('\\;\\Longrightarrow\\;'))
        var.get('a')(Js('\\impliedby'), Js('\\;\\Longleftarrow\\;'))
        var.get('a')(Js('\\ordinarycolon'), Js(':'))
        var.get('a')(Js('\\vcentcolon'), Js('\\mathrel{\\mathop\\ordinarycolon}'))
        var.get('a')(Js('\\dblcolon'), Js('\\vcentcolon\\mathrel{\\mkern-.9mu}\\vcentcolon'))
        var.get('a')(Js('\\coloneqq'), Js('\\vcentcolon\\mathrel{\\mkern-1.2mu}='))
        var.get('a')(Js('\\Coloneqq'), Js('\\dblcolon\\mathrel{\\mkern-1.2mu}='))
        var.get('a')(Js('\\coloneq'), Js('\\vcentcolon\\mathrel{\\mkern-1.2mu}\\mathrel{-}'))
        var.get('a')(Js('\\Coloneq'), Js('\\dblcolon\\mathrel{\\mkern-1.2mu}\\mathrel{-}'))
        var.get('a')(Js('\\eqqcolon'), Js('=\\mathrel{\\mkern-1.2mu}\\vcentcolon'))
        var.get('a')(Js('\\Eqqcolon'), Js('=\\mathrel{\\mkern-1.2mu}\\dblcolon'))
        var.get('a')(Js('\\eqcolon'), Js('\\mathrel{-}\\mathrel{\\mkern-1.2mu}\\vcentcolon'))
        var.get('a')(Js('\\Eqcolon'), Js('\\mathrel{-}\\mathrel{\\mkern-1.2mu}\\dblcolon'))
        var.get('a')(Js('\\colonapprox'), Js('\\vcentcolon\\mathrel{\\mkern-1.2mu}\\approx'))
        var.get('a')(Js('\\Colonapprox'), Js('\\dblcolon\\mathrel{\\mkern-1.2mu}\\approx'))
        var.get('a')(Js('\\colonsim'), Js('\\vcentcolon\\mathrel{\\mkern-1.2mu}\\sim'))
        var.get('a')(Js('\\Colonsim'), Js('\\dblcolon\\mathrel{\\mkern-1.2mu}\\sim'))
        var.get('a')(Js('\\ratio'), Js('\\vcentcolon'))
        var.get('a')(Js('\\coloncolon'), Js('\\dblcolon'))
        var.get('a')(Js('\\colonequals'), Js('\\coloneqq'))
        var.get('a')(Js('\\coloncolonequals'), Js('\\Coloneqq'))
        var.get('a')(Js('\\equalscolon'), Js('\\eqqcolon'))
        var.get('a')(Js('\\equalscoloncolon'), Js('\\Eqqcolon'))
        var.get('a')(Js('\\colonminus'), Js('\\coloneq'))
        var.get('a')(Js('\\coloncolonminus'), Js('\\Coloneq'))
        var.get('a')(Js('\\minuscolon'), Js('\\eqcolon'))
        var.get('a')(Js('\\minuscoloncolon'), Js('\\Eqcolon'))
        var.get('a')(Js('\\coloncolonapprox'), Js('\\Colonapprox'))
        var.get('a')(Js('\\coloncolonsim'), Js('\\Colonsim'))
        var.get('a')(Js('\\simcolon'), Js('\\sim\\mathrel{\\mkern-1.2mu}\\vcentcolon'))
        var.get('a')(Js('\\simcoloncolon'), Js('\\sim\\mathrel{\\mkern-1.2mu}\\dblcolon'))
        var.get('a')(Js('\\approxcolon'), Js('\\approx\\mathrel{\\mkern-1.2mu}\\vcentcolon'))
        var.get('a')(Js('\\approxcoloncolon'), Js('\\approx\\mathrel{\\mkern-1.2mu}\\dblcolon'))
    PyJs_anonymous_749_._set_name('anonymous')
    PyJs_Object_750_ = Js({})
    @Js
    def PyJs_anonymous_751_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'c', 'o', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_u_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_752_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_752_)
        PyJsHoisted_u_.func_name = 'u'
        var.put('u', PyJsHoisted_u_)
        Js('use strict')
        var.put('a', var.get('e')(Js('babel-runtime/helpers/classCallCheck')))
        var.put('n', var.get('u')(var.get('a')))
        var.put('i', var.get('e')(Js('babel-runtime/helpers/createClass')))
        var.put('l', var.get('u')(var.get('i')))
        var.put('s', var.get('e')(Js('./utils')))
        var.put('o', var.get('u')(var.get('s')))
        pass
        @Js
        def PyJs_anonymous_753_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, r, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments}, var)
                var.registers(['r', 't'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('type', var.get('t'))
                PyJs_Object_754_ = Js({})
                var.get(u"this").put('attributes', PyJs_Object_754_)
                var.get(u"this").put('children', (var.get('r') or Js([])))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_756_(t, r, this, arguments, var=var):
                var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_756_}, var)
                var.registers(['r', 't'])
                var.get(u"this").get('attributes').put(var.get('t'), var.get('r'))
            PyJs_e_756_._set_name('e')
            PyJs_Object_755_ = Js({'key':Js('setAttribute'),'value':PyJs_e_756_})
            @Js
            def PyJs_e_758_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_758_}, var)
                var.registers(['r', 'a', 't'])
                var.put('t', var.get('document').callprop('createElementNS', Js('http://www.w3.org/1998/Math/MathML'), var.get(u"this").get('type')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('r', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('r')):
                        var.get('t').callprop('setAttribute', var.get('r'), var.get(u"this").get('attributes').get(var.get('r')))
                #for JS loop
                var.put('a', Js(0.0))
                while (var.get('a')<var.get(u"this").get('children').get('length')):
                    try:
                        var.get('t').callprop('appendChild', var.get(u"this").get('children').get(var.get('a')).callprop('toNode'))
                    finally:
                            (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
                return var.get('t')
            PyJs_e_758_._set_name('e')
            PyJs_Object_757_ = Js({'key':Js('toNode'),'value':PyJs_e_758_})
            @Js
            def PyJs_e_760_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_760_}, var)
                var.registers(['r', 'a', 't'])
                var.put('t', (Js('<')+var.get(u"this").get('type')))
                for PyJsTemp in var.get(u"this").get('attributes'):
                    var.put('r', PyJsTemp)
                    if var.get('Object').get('prototype').get('hasOwnProperty').callprop('call', var.get(u"this").get('attributes'), var.get('r')):
                        var.put('t', ((Js(' ')+var.get('r'))+Js('="')), '+')
                        var.put('t', var.get('o').get('default').callprop('escape', var.get(u"this").get('attributes').get(var.get('r'))), '+')
                        var.put('t', Js('"'), '+')
                var.put('t', Js('>'), '+')
                #for JS loop
                var.put('a', Js(0.0))
                while (var.get('a')<var.get(u"this").get('children').get('length')):
                    try:
                        var.put('t', var.get(u"this").get('children').get(var.get('a')).callprop('toMarkup'), '+')
                    finally:
                            (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
                var.put('t', ((Js('</')+var.get(u"this").get('type'))+Js('>')), '+')
                return var.get('t')
            PyJs_e_760_._set_name('e')
            PyJs_Object_759_ = Js({'key':Js('toMarkup'),'value':PyJs_e_760_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_755_, PyJs_Object_757_, PyJs_Object_759_]))
            return var.get('e')
        PyJs_anonymous_753_._set_name('anonymous')
        var.put('c', PyJs_anonymous_753_())
        @Js
        def PyJs_anonymous_761_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            @Js
            def PyJsHoisted_e_(t, this, arguments, var=var):
                var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
                var.registers(['t'])
                PyJsComma(Js(0.0),var.get('n').get('default'))(var.get(u"this"), var.get('e'))
                var.get(u"this").put('text', var.get('t'))
            PyJsHoisted_e_.func_name = 'e'
            var.put('e', PyJsHoisted_e_)
            pass
            @Js
            def PyJs_e_763_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_763_}, var)
                var.registers([])
                return var.get('document').callprop('createTextNode', var.get(u"this").get('text'))
            PyJs_e_763_._set_name('e')
            PyJs_Object_762_ = Js({'key':Js('toNode'),'value':PyJs_e_763_})
            @Js
            def PyJs_e_765_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments, 'e':PyJs_e_765_}, var)
                var.registers([])
                return var.get('o').get('default').callprop('escape', var.get(u"this").get('text'))
            PyJs_e_765_._set_name('e')
            PyJs_Object_764_ = Js({'key':Js('toMarkup'),'value':PyJs_e_765_})
            PyJsComma(Js(0.0),var.get('l').get('default'))(var.get('e'), Js([PyJs_Object_762_, PyJs_Object_764_]))
            return var.get('e')
        PyJs_anonymous_761_._set_name('anonymous')
        var.put('f', PyJs_anonymous_761_())
        PyJs_Object_766_ = Js({'MathNode':var.get('c'),'TextNode':var.get('f')})
        var.get('t').put('exports', PyJs_Object_766_)
    PyJs_anonymous_751_._set_name('anonymous')
    PyJs_Object_767_ = Js({'./utils':Js(51.0),'babel-runtime/helpers/classCallCheck':Js(4.0),'babel-runtime/helpers/createClass':Js(5.0)})
    @Js
    def PyJs_anonymous_768_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'n', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_769_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_769_)
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./Parser')))
        var.put('n', var.get('i')(var.get('a')))
        pass
        @Js
        def PyJs_e_770_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_770_}, var)
            var.registers(['r', 'a', 't'])
            if (PyJsStrictEq(var.get('t',throw=False).typeof(),Js('string')) or var.get('t').instanceof(var.get('String'))).neg():
                PyJsTempException = JsToPyException(var.get('TypeError').create(Js('KaTeX can only parse string typed expression')))
                raise PyJsTempException
            var.put('a', var.get('n').get('default').create(var.get('t'), var.get('r')))
            return var.get('a').callprop('parse')
        PyJs_e_770_._set_name('e')
        var.put('l', PyJs_e_770_)
        var.get('t').put('exports', var.get('l'))
    PyJs_anonymous_768_._set_name('anonymous')
    PyJs_Object_771_ = Js({'./Parser':Js(31.0)})
    @Js
    def PyJs_anonymous_772_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'h', 'l', 'r', 'c', 'o', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        Js('use strict')
        var.put('a', var.get('e')(Js('./buildCommon')))
        var.put('n', var.get('e')(Js('./mathMLTree')))
        var.put('i', var.get('e')(Js('./utils')))
        PyJs_Object_773_ = Js({'widehat':Js('^'),'widetilde':Js('~'),'undertilde':Js('~'),'overleftarrow':Js('←'),'underleftarrow':Js('←'),'xleftarrow':Js('←'),'overrightarrow':Js('→'),'underrightarrow':Js('→'),'xrightarrow':Js('→'),'underbrace':Js('⎵'),'overbrace':Js('⏞'),'overleftrightarrow':Js('↔'),'underleftrightarrow':Js('↔'),'xleftrightarrow':Js('↔'),'Overrightarrow':Js('⇒'),'xRightarrow':Js('⇒'),'overleftharpoon':Js('↼'),'xleftharpoonup':Js('↼'),'overrightharpoon':Js('⇀'),'xrightharpoonup':Js('⇀'),'xLeftarrow':Js('⇐'),'xLeftrightarrow':Js('⇔'),'xhookleftarrow':Js('↩'),'xhookrightarrow':Js('↪'),'xmapsto':Js('↦'),'xrightharpoondown':Js('⇁'),'xleftharpoondown':Js('↽'),'xrightleftharpoons':Js('⇌'),'xleftrightharpoons':Js('⇋'),'xtwoheadleftarrow':Js('↞'),'xtwoheadrightarrow':Js('↠'),'xLongequal':Js('='),'xtofrom':Js('⇄')})
        var.put('l', PyJs_Object_773_)
        @Js
        def PyJs_e_774_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_774_}, var)
            var.registers(['r', 't'])
            var.put('r', var.get('n').get('MathNode').create(Js('mo'), Js([var.get('n').get('TextNode').create(var.get('l').get(var.get('t').callprop('substr', Js(1.0))))])))
            var.get('r').callprop('setAttribute', Js('stretchy'), Js('true'))
            return var.get('r')
        PyJs_e_774_._set_name('e')
        var.put('s', PyJs_e_774_)
        PyJs_Object_775_ = Js({'overleftarrow':Js([Js(0.522), Js(0.0), Js('leftarrow'), Js(0.5)]),'underleftarrow':Js([Js(0.522), Js(0.0), Js('leftarrow'), Js(0.5)]),'xleftarrow':Js([Js(0.261), Js(0.261), Js('leftarrow'), Js(0.783)]),'overrightarrow':Js([Js(0.522), Js(0.0), Js('rightarrow'), Js(0.5)]),'underrightarrow':Js([Js(0.522), Js(0.0), Js('rightarrow'), Js(0.5)]),'xrightarrow':Js([Js(0.261), Js(0.261), Js('rightarrow'), Js(0.783)]),'overbrace':Js([Js(0.548), Js(0.0), Js('overbrace'), Js(1.6)]),'underbrace':Js([Js(0.548), Js(0.0), Js('underbrace'), Js(1.6)]),'overleftrightarrow':Js([Js(0.522), Js(0.0), Js('leftrightarrow'), Js(0.5)]),'underleftrightarrow':Js([Js(0.522), Js(0.0), Js('leftrightarrow'), Js(0.5)]),'xleftrightarrow':Js([Js(0.261), Js(0.261), Js('leftrightarrow'), Js(0.783)]),'Overrightarrow':Js([Js(0.56), Js(0.0), Js('doublerightarrow'), Js(0.5)]),'xLeftarrow':Js([Js(0.28), Js(0.28), Js('doubleleftarrow'), Js(0.783)]),'xRightarrow':Js([Js(0.28), Js(0.28), Js('doublerightarrow'), Js(0.783)]),'xLeftrightarrow':Js([Js(0.28), Js(0.28), Js('doubleleftrightarrow'), Js(0.955)]),'overleftharpoon':Js([Js(0.522), Js(0.0), Js('leftharpoon'), Js(0.5)]),'overrightharpoon':Js([Js(0.522), Js(0.0), Js('rightharpoon'), Js(0.5)]),'xleftharpoonup':Js([Js(0.261), Js(0.261), Js('leftharpoon'), Js(0.783)]),'xrightharpoonup':Js([Js(0.261), Js(0.261), Js('rightharpoon'), Js(0.783)]),'xhookleftarrow':Js([Js(0.261), Js(0.261), Js('hookleftarrow'), Js(0.87)]),'xhookrightarrow':Js([Js(0.261), Js(0.261), Js('hookrightarrow'), Js(0.87)]),'overlinesegment':Js([Js(0.414), Js(0.0), Js('linesegment'), Js(0.5)]),'underlinesegment':Js([Js(0.414), Js(0.0), Js('linesegment'), Js(0.5)]),'xmapsto':Js([Js(0.261), Js(0.261), Js('mapsto'), Js(0.783)]),'xrightharpoondown':Js([Js(0.261), Js(0.261), Js('rightharpoondown'), Js(0.783)]),'xleftharpoondown':Js([Js(0.261), Js(0.261), Js('leftharpoondown'), Js(0.783)]),'xrightleftharpoons':Js([Js(0.358), Js(0.358), Js('rightleftharpoons'), Js(0.716)]),'xleftrightharpoons':Js([Js(0.358), Js(0.358), Js('leftrightharpoons'), Js(0.716)]),'overgroup':Js([Js(0.342), Js(0.0), Js('overgroup'), Js(0.87)]),'undergroup':Js([Js(0.342), Js(0.0), Js('undergroup'), Js(0.87)]),'xtwoheadleftarrow':Js([Js(0.167), Js(0.167), Js('twoheadleftarrow'), Js(0.86)]),'xtwoheadrightarrow':Js([Js(0.167), Js(0.167), Js('twoheadrightarrow'), Js(0.86)]),'xLongequal':Js([Js(0.167), Js(0.167), Js('longequal'), Js(0.5)]),'xtofrom':Js([Js(0.264), Js(0.264), Js('tofrom'), Js(0.86)])})
        var.put('o', PyJs_Object_775_)
        PyJs_Object_776_ = Js({'doubleleftarrow':Js("<path d='M262 157\nl10-10c34-36 62.7-77 86-123 3.3-8 5-13.3 5-16 0-5.3-6.7-8-20-8-7.3\n 0-12.2.5-14.5 1.5-2.3 1-4.8 4.5-7.5 10.5-49.3 97.3-121.7 169.3-217 216-28\n 14-57.3 25-88 33-6.7 2-11 3.8-13 5.5-2 1.7-3 4.2-3 7.5s1 5.8 3 7.5\nc2 1.7 6.3 3.5 13 5.5 68 17.3 128.2 47.8 180.5 91.5 52.3 43.7 93.8 96.2 124.5\n 157.5 9.3 8 15.3 12.3 18 13h6c12-.7 18-4 18-10 0-2-1.7-7-5-15-23.3-46-52-87\n-86-123l-10-10h399738v-40H218c328 0 0 0 0 0l-10-8c-26.7-20-65.7-43-117-69 2.7\n-2 6-3.7 10-5 36.7-16 72.3-37.3 107-64l10-8h399782v-40z\nm8 0v40h399730v-40zm0 194v40h399730v-40z'/>"),'doublerightarrow':Js("<path d='M399738 392l\n-10 10c-34 36-62.7 77-86 123-3.3 8-5 13.3-5 16 0 5.3 6.7 8 20 8 7.3 0 12.2-.5\n 14.5-1.5 2.3-1 4.8-4.5 7.5-10.5 49.3-97.3 121.7-169.3 217-216 28-14 57.3-25 88\n-33 6.7-2 11-3.8 13-5.5 2-1.7 3-4.2 3-7.5s-1-5.8-3-7.5c-2-1.7-6.3-3.5-13-5.5-68\n-17.3-128.2-47.8-180.5-91.5-52.3-43.7-93.8-96.2-124.5-157.5-9.3-8-15.3-12.3-18\n-13h-6c-12 .7-18 4-18 10 0 2 1.7 7 5 15 23.3 46 52 87 86 123l10 10H0v40h399782\nc-328 0 0 0 0 0l10 8c26.7 20 65.7 43 117 69-2.7 2-6 3.7-10 5-36.7 16-72.3 37.3\n-107 64l-10 8H0v40zM0 157v40h399730v-40zm0 194v40h399730v-40z'/>"),'leftarrow':Js("<path d='M400000 241H110l3-3c68.7-52.7 113.7-120\n 135-202 4-14.7 6-23 6-25 0-7.3-7-11-21-11-8 0-13.2.8-15.5 2.5-2.3 1.7-4.2 5.8\n-5.5 12.5-1.3 4.7-2.7 10.3-4 17-12 48.7-34.8 92-68.5 130S65.3 228.3 18 247\nc-10 4-16 7.7-18 11 0 8.7 6 14.3 18 17 47.3 18.7 87.8 47 121.5 85S196 441.3 208\n 490c.7 2 1.3 5 2 9s1.2 6.7 1.5 8c.3 1.3 1 3.3 2 6s2.2 4.5 3.5 5.5c1.3 1 3.3\n 1.8 6 2.5s6 1 10 1c14 0 21-3.7 21-11 0-2-2-10.3-6-25-20-79.3-65-146.7-135-202\n l-3-3h399890zM100 241v40h399900v-40z'/>"),'rightarrow':Js("<path d='M0 241v40h399891c-47.3 35.3-84 78-110 128\n-16.7 32-27.7 63.7-33 95 0 1.3-.2 2.7-.5 4-.3 1.3-.5 2.3-.5 3 0 7.3 6.7 11 20\n 11 8 0 13.2-.8 15.5-2.5 2.3-1.7 4.2-5.5 5.5-11.5 2-13.3 5.7-27 11-41 14.7-44.7\n 39-84.5 73-119.5s73.7-60.2 119-75.5c6-2 9-5.7 9-11s-3-9-9-11c-45.3-15.3-85\n-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5\n-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14 0-21 3.7-21 11 0 2 2 10.3 6 25 20.7 83.3 67\n 151.7 139 205zm0 0v40h399900v-40z'/>")})
        var.put('u', PyJs_Object_776_)
        def PyJs_LONG_778_(var=var):
            return ((Js("><svg width='50.1%' viewBox='0 0 400000 522'\npreserveAspectRatio='xMinYMin slice'>")+var.get('u').get('leftarrow'))+Js("</svg>\n<svg x='50%' width='50%' viewBox='0 0 400000 522' preserveAspectRatio='xMaxYMin\n slice'><path d='M399859 241c-764 0 0 0 0 0 40-3.3 68.7\n -15.7 86-37 10-12 15-25.3 15-40 0-22.7-9.8-40.7-29.5-54-19.7-13.3-43.5-21-71.5\n -23-17.3-1.3-26-8-26-20 0-13.3 8.7-20 26-20 38 0 71 11.2 99 33.5 0 0 7 5.6 21\n 16.7 14 11.2 21 33.5 21 66.8s-14 61.2-42 83.5c-28 22.3-61 33.5-99 33.5L0 241z\n M0 281v-40h399859v40z'/></svg>"))
        def PyJs_LONG_779_(var=var):
            return (Js("><svg width='50.1%' viewBox='0 0 400000 522'\npreserveAspectRatio='xMinYMin slice'><path d='M400000 281\nH103s-33-11.2-61-33.5S0 197.3 0 164s14.2-61.2 42.5-83.5C70.8 58.2 104 47 142 47\nc16.7 0 25 6.7 25 20 0 12-8.7 18.7-26 20-40 3.3-68.7 15.7-86 37-10 12-15 25.3\n-15 40 0 22.7 9.8 40.7 29.5 54 19.7 13.3 43.5 21 71.5 23h399859zM103 281v-40\nh399897v40z'/></svg><svg x='50%' width='50%' viewBox='0 0 400000 522'\npreserveAspectRatio='xMaxYMin slice'>")+var.get('u').get('rightarrow'))
        def PyJs_LONG_780_(var=var):
            return (Js("><svg width='50.1%' viewBox='0 0 400000 522'\npreserveAspectRatio='xMinYMin slice'><path d='M40 241c740\n 0 0 0 0 0v-75c0-40.7-.2-64.3-.5-71-.3-6.7-2.2-11.7-5.5-15-4-4-8.7-6-14-6-5.3 0\n-10 2-14 6C2.7 83.3.8 91.3.5 104 .2 116.7 0 169 0 261c0 114 .7 172.3 2 175 4 8\n 10 12 18 12 5.3 0 10-2 14-6 3.3-3.3 5.2-8.3 5.5-15 .3-6.7.5-30.3.5-71v-75\nh399960zm0 0v40h399960v-40z'/></svg><svg x='50%' width='50%' viewBox='0 0\n 400000 522' preserveAspectRatio='xMaxYMin slice'>")+var.get('u').get('rightarrow'))
        PyJs_Object_777_ = Js({'bcancel':Js("<line x1='0' y1='0' x2='100%' y2='100%' stroke-width='0.046em'/>"),'cancel':Js("<line x1='0' y1='100%' x2='100%' y2='0' stroke-width='0.046em'/>"),'doubleleftarrow':((Js("><svg viewBox='0 0 400000 549'\npreserveAspectRatio='xMinYMin slice'>")+var.get('u').get('doubleleftarrow'))+Js('</svg>')),'doubleleftrightarrow':((((Js("><svg width='50.1%' viewBox='0 0 400000 549'\npreserveAspectRatio='xMinYMin slice'>")+var.get('u').get('doubleleftarrow'))+Js("</svg>\n<svg x='50%' width='50%' viewBox='0 0 400000 549' preserveAspectRatio='xMaxYMin\n slice'>"))+var.get('u').get('doublerightarrow'))+Js('</svg>')),'doublerightarrow':((Js("><svg viewBox='0 0 400000 549'\npreserveAspectRatio='xMaxYMin slice'>")+var.get('u').get('doublerightarrow'))+Js('</svg>')),'hookleftarrow':PyJs_LONG_778_(),'hookrightarrow':(PyJs_LONG_779_()+Js('</svg>')),'leftarrow':((Js("><svg viewBox='0 0 400000 522' preserveAspectRatio='xMinYMin\n slice'>")+var.get('u').get('leftarrow'))+Js('</svg>')),'leftharpoon':Js("><svg viewBox='0 0 400000 522' preserveAspectRatio='xMinYMin\n slice'><path d='M0 267c.7 5.3 3 10 7 14h399993v-40H93c3.3\n-3.3 10.2-9.5 20.5-18.5s17.8-15.8 22.5-20.5c50.7-52 88-110.3 112-175 4-11.3 5\n-18.3 3-21-1.3-4-7.3-6-18-6-8 0-13 .7-15 2s-4.7 6.7-8 16c-42 98.7-107.3 174.7\n-196 228-6.7 4.7-10.7 8-12 10-1.3 2-2 5.7-2 11zm100-26v40h399900v-40z'/></svg>"),'leftharpoondown':Js('><svg viewBox=\'0 0 400000 522\'\npreserveAspectRatio=\'xMinYMin slice\'><path d="M7 241c-4 4-6.333 8.667-7 14\n 0 5.333.667 9 2 11s5.333 5.333 12 10c90.667 54 156 130 196 228 3.333 10.667\n 6.333 16.333 9 17 2 .667 5 1 9 1h5c10.667 0 16.667-2 18-6 2-2.667 1-9.667-3-21\n -32-87.333-82.667-157.667-152-211l-3-3h399907v-40z\nM93 281 H400000 v-40L7 241z"/></svg>'),'leftrightarrow':((((Js("><svg width='50.1%' viewBox='0 0 400000 522'\npreserveAspectRatio='xMinYMin slice'>")+var.get('u').get('leftarrow'))+Js("</svg>\n<svg x='50%' width='50%' viewBox='0 0 400000 522' preserveAspectRatio='xMaxYMin\n slice'>"))+var.get('u').get('rightarrow'))+Js('</svg>')),'leftrightharpoons':Js("><svg width='50.1%' viewBox='0 0 400000 716'\npreserveAspectRatio='xMinYMin slice'><path d='M0 267c.7 5.3\n 3 10 7 14h399993v-40H93c3.3-3.3 10.2-9.5 20.5-18.5s17.8-15.8 22.5-20.5c50.7-52\n 88-110.3 112-175 4-11.3 5-18.3 3-21-1.3-4-7.3-6-18-6-8 0-13 .7-15 2s-4.7 6.7-8\n 16c-42 98.7-107.3 174.7-196 228-6.7 4.7-10.7 8-12 10-1.3 2-2 5.7-2 11zm100-26\nv40h399900v-40zM0 435v40h400000v-40zm0 0v40h400000v-40z'/></svg>\n<svg x='50%' width='50%' viewBox='0 0 400000 716' preserveAspectRatio='xMaxYMin\n slice'><path d='M399747 705c0 7.3 6.7 11 20 11 8 0 13-.8\n 15-2.5s4.7-6.8 8-15.5c40-94 99.3-166.3 178-217 13.3-8 20.3-12.3 21-13 5.3-3.3\n 8.5-5.8 9.5-7.5 1-1.7 1.5-5.2 1.5-10.5s-2.3-10.3-7-15H0v40h399908c-34 25.3\n-64.7 57-92 95-27.3 38-48.7 77.7-64 119-3.3 8.7-5 14-5 16zM0 435v40h399900v-40z\nm0-194v40h400000v-40zm0 0v40h400000v-40z'/></svg>"),'linesegment':Js("><svg width='50.1%' viewBox='0 0 400000 414'\npreserveAspectRatio='xMinYMin slice'><path d='M40 187V40H0\nv334h40V227h399960v-40zm0 0V40H0v334h40V227h399960v-40z'/></svg><svg x='50%'\nwidth='50%' viewBox='0 0 400000 414' preserveAspectRatio='xMaxYMin slice'>\n<path d='M0 187v40h399960v147h40V40h-40v147zm0\n 0v40h399960v147h40V40h-40v147z'/></svg>"),'longequal':Js(" viewBox='0 0 100 334' preserveAspectRatio='none'>\n<path d='M0 50h100v40H0zm0 194h100v40H0z'/>"),'mapsto':(PyJs_LONG_780_()+Js('</svg>')),'overbrace':Js("><svg width='25.5%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMinYMin slice'><path d='M6 548l-6-6\nv-35l6-11c56-104 135.3-181.3 238-232 57.3-28.7 117-45 179-50h399577v120H403\nc-43.3 7-81 15-113 26-100.7 33-179.7 91-237 174-2.7 5-6 9-10 13-.7 1-7.3 1-20 1\nH6z'/></svg><svg x='25%' width='50%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMidYMin slice'><path d='M200428 334\nc-100.7-8.3-195.3-44-280-108-55.3-42-101.7-93-139-153l-9-14c-2.7 4-5.7 8.7-9 14\n-53.3 86.7-123.7 153-211 199-66.7 36-137.3 56.3-212 62H0V214h199568c178.3-11.7\n 311.7-78.3 403-201 6-8 9.7-12 11-12 .7-.7 6.7-1 18-1s17.3.3 18 1c1.3 0 5 4 11\n 12 44.7 59.3 101.3 106.3 170 141s145.3 54.3 229 60h199572v120z'/></svg>\n<svg x='74.9%' width='24.1%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMaxYMin slice'><path d='M400000 542l\n-6 6h-17c-12.7 0-19.3-.3-20-1-4-4-7.3-8.3-10-13-35.3-51.3-80.8-93.8-136.5-127.5\ns-117.2-55.8-184.5-66.5c-.7 0-2-.3-4-1-18.7-2.7-76-4.3-172-5H0V214h399571l6 1\nc124.7 8 235 61.7 331 161 31.3 33.3 59.7 72.7 85 118l7 13v35z'/></svg>"),'overgroup':Js("><svg width='50.1%' viewBox='0 0 400000 342'\npreserveAspectRatio='xMinYMin slice'><path d='M400000 80\nH435C64 80 168.3 229.4 21 260c-5.9 1.2-18 0-18 0-2 0-3-1-3-3v-38C76 61 257 0\n 435 0h399565z'/></svg><svg x='50%' width='50%' viewBox='0 0 400000 342'\npreserveAspectRatio='xMaxYMin slice'><path d='M0 80h399565\nc371 0 266.7 149.4 414 180 5.9 1.2 18 0 18 0 2 0 3-1 3-3v-38\nc-76-158-257-219-435-219H0z'/></svg>"),'rightarrow':((Js("><svg viewBox='0 0 400000 522' preserveAspectRatio='xMaxYMin\n slice'>")+var.get('u').get('rightarrow'))+Js('</svg>')),'rightharpoon':Js("><svg viewBox='0 0 400000 522' preserveAspectRatio='xMaxYMin\n slice'><path d='M0 241v40h399993c4.7-4.7 7-9.3 7-14 0-9.3\n-3.7-15.3-11-18-92.7-56.7-159-133.7-199-231-3.3-9.3-6-14.7-8-16-2-1.3-7-2-15-2\n-10.7 0-16.7 2-18 6-2 2.7-1 9.7 3 21 15.3 42 36.7 81.8 64 119.5 27.3 37.7 58\n 69.2 92 94.5zm0 0v40h399900v-40z'/></svg>"),'rightharpoondown':Js("><svg viewBox='0 0 400000 522'\npreserveAspectRatio='xMaxYMin slice'><path d='M399747 511\nc0 7.3 6.7 11 20 11 8 0 13-.8 15-2.5s4.7-6.8 8-15.5c40-94 99.3-166.3 178-217\n 13.3-8 20.3-12.3 21-13 5.3-3.3 8.5-5.8 9.5-7.5 1-1.7 1.5-5.2 1.5-10.5s-2.3\n -10.3-7-15H0v40h399908c-34 25.3-64.7 57-92 95-27.3 38-48.7 77.7-64 119-3.3\n 8.7-5 14-5 16zM0 241v40h399900v-40z'/></svg>"),'rightleftharpoons':Js("><svg width='50%' viewBox='0 0 400000 716'\npreserveAspectRatio='xMinYMin slice'><path d='M7 435c-4 4\n-6.3 8.7-7 14 0 5.3.7 9 2 11s5.3 5.3 12 10c90.7 54 156 130 196 228 3.3 10.7 6.3\n 16.3 9 17 2 .7 5 1 9 1h5c10.7 0 16.7-2 18-6 2-2.7 1-9.7-3-21-32-87.3-82.7\n-157.7-152-211l-3-3h399907v-40H7zm93 0v40h399900v-40zM0 241v40h399900v-40z\nm0 0v40h399900v-40z'/></svg><svg x='50%' width='50%' viewBox='0 0 400000 716'\npreserveAspectRatio='xMaxYMin slice'><path d='M0 241v40\nh399993c4.7-4.7 7-9.3 7-14 0-9.3-3.7-15.3-11-18-92.7-56.7-159-133.7-199-231-3.3\n-9.3-6-14.7-8-16-2-1.3-7-2-15-2-10.7 0-16.7 2-18 6-2 2.7-1 9.7 3 21 15.3 42\n 36.7 81.8 64 119.5 27.3 37.7 58 69.2 92 94.5zm0 0v40h399900v-40z\n m100 194v40h399900v-40zm0 0v40h399900v-40z'/></svg>"),'tilde1':Js(" viewBox='0 0 600 260' preserveAspectRatio='none'>\n<path d='M200 55.538c-77 0-168 73.953-177 73.953-3 0-7\n-2.175-9-5.437L2 97c-1-2-2-4-2-6 0-4 2-7 5-9l20-12C116 12 171 0 207 0c86 0\n 114 68 191 68 78 0 168-68 177-68 4 0 7 2 9 5l12 19c1 2.175 2 4.35 2 6.525 0\n 4.35-2 7.613-5 9.788l-19 13.05c-92 63.077-116.937 75.308-183 76.128\n-68.267.847-113-73.952-191-73.952z'/>"),'tilde2':Js(" viewBox='0 0 1033 286' preserveAspectRatio='none'>\n<path d='M344 55.266c-142 0-300.638 81.316-311.5 86.418\n-8.01 3.762-22.5 10.91-23.5 5.562L1 120c-1-2-1-3-1-4 0-5 3-9 8-10l18.4-9C160.9\n 31.9 283 0 358 0c148 0 188 122 331 122s314-97 326-97c4 0 8 2 10 7l7 21.114\nc1 2.14 1 3.21 1 4.28 0 5.347-3 9.626-7 10.696l-22.3 12.622C852.6 158.372 751\n 181.476 676 181.476c-149 0-189-126.21-332-126.21z'/>"),'tilde3':Js(" viewBox='0 0 2339 306' preserveAspectRatio='none'>\n<path d='M786 59C457 59 32 175.242 13 175.242c-6 0-10-3.457\n-11-10.37L.15 138c-1-7 3-12 10-13l19.2-6.4C378.4 40.7 634.3 0 804.3 0c337 0\n 411.8 157 746.8 157 328 0 754-112 773-112 5 0 10 3 11 9l1 14.075c1 8.066-.697\n 16.595-6.697 17.492l-21.052 7.31c-367.9 98.146-609.15 122.696-778.15 122.696\n -338 0-409-156.573-744-156.573z'/>"),'tilde4':Js(" viewBox='0 0 2340 312' preserveAspectRatio='none'>\n<path d='M786 58C457 58 32 177.487 13 177.487c-6 0-10-3.345\n-11-10.035L.15 143c-1-7 3-12 10-13l22-6.7C381.2 35 637.15 0 807.15 0c337 0 409\n 177 744 177 328 0 754-127 773-127 5 0 10 3 11 9l1 14.794c1 7.805-3 13.38-9\n 14.495l-20.7 5.574c-366.85 99.79-607.3 139.372-776.3 139.372-338 0-409\n -175.236-744-175.236z'/>"),'tofrom':Js("><svg width='50.1%' viewBox='0 0 400000 528'\npreserveAspectRatio='xMinYMin slice'><path d='M0 147h400000\nv40H0zm0 214c68 40 115.7 95.7 143 167h22c15.3 0 23-.3 23-1 0-1.3-5.3-13.7-16-37\n-18-35.3-41.3-69-70-101l-7-8h399905v-40H95l7-8c28.7-32 52-65.7 70-101 10.7-23.3\n 16-35.7 16-37 0-.7-7.7-1-23-1h-22C115.7 265.3 68 321 0 361zm0-174v-40h399900\nv40zm100 154v40h399900v-40z'/></svg><svg x='50%' width='50%' viewBox='0 0\n 400000 528' preserveAspectRatio='xMaxYMin slice'><path\nd='M400000 167c-70.7-42-118-97.7-142-167h-23c-15.3 0-23 .3-23 1 0 1.3 5.3 13.7\n 16 37 18 35.3 41.3 69 70 101l7 8H0v40h399905l-7 8c-28.7 32-52 65.7-70 101-10.7\n 23.3-16 35.7-16 37 0 .7 7.7 1 23 1h23c24-69.3 71.3-125 142-167z\n M100 147v40h399900v-40zM0 341v40h399900v-40z'/></svg>"),'twoheadleftarrow':Js("><svg viewBox='0 0 400000 334'\npreserveAspectRatio='xMinYMin slice'><path d='M0 167c68 40\n 115.7 95.7 143 167h22c15.3 0 23-.3 23-1 0-1.3-5.3-13.7-16-37-18-35.3-41.3-69\n-70-101l-7-8h125l9 7c50.7 39.3 85 86 103 140h46c0-4.7-6.3-18.7-19-42-18-35.3\n-40-67.3-66-96l-9-9h399716v-40H284l9-9c26-28.7 48-60.7 66-96 12.7-23.333 19\n-37.333 19-42h-46c-18 54-52.3 100.7-103 140l-9 7H95l7-8c28.7-32 52-65.7 70-101\n 10.7-23.333 16-35.7 16-37 0-.7-7.7-1-23-1h-22C115.7 71.3 68 127 0 167z'/>\n</svg>"),'twoheadrightarrow':Js("><svg viewBox='0 0 400000 334'\npreserveAspectRatio='xMaxYMin slice'><path d='M400000 167\nc-68-40-115.7-95.7-143-167h-22c-15.3 0-23 .3-23 1 0 1.3 5.3 13.7 16 37 18 35.3\n 41.3 69 70 101l7 8h-125l-9-7c-50.7-39.3-85-86-103-140h-46c0 4.7 6.3 18.7 19 42\n 18 35.3 40 67.3 66 96l9 9H0v40h399716l-9 9c-26 28.7-48 60.7-66 96-12.7 23.333\n-19 37.333-19 42h46c18-54 52.3-100.7 103-140l9-7h125l-7 8c-28.7 32-52 65.7-70\n 101-10.7 23.333-16 35.7-16 37 0 .7 7.7 1 23 1h22c27.3-71.3 75-127 143-167z'/>\n</svg>"),'underbrace':Js("><svg width='25.1%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMinYMin slice'><path d='M0 6l6-6h17\nc12.688 0 19.313.3 20 1 4 4 7.313 8.3 10 13 35.313 51.3 80.813 93.8 136.5 127.5\n 55.688 33.7 117.188 55.8 184.5 66.5.688 0 2 .3 4 1 18.688 2.7 76 4.3 172 5\nh399450v120H429l-6-1c-124.688-8-235-61.7-331-161C60.687 138.7 32.312 99.3 7 54\nL0 41V6z'/></svg><svg x='25%' width='50%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMidYMin slice'><path d='M199572 214\nc100.7 8.3 195.3 44 280 108 55.3 42 101.7 93 139 153l9 14c2.7-4 5.7-8.7 9-14\n 53.3-86.7 123.7-153 211-199 66.7-36 137.3-56.3 212-62h199568v120H200432c-178.3\n 11.7-311.7 78.3-403 201-6 8-9.7 12-11 12-.7.7-6.7 1-18 1s-17.3-.3-18-1c-1.3 0\n-5-4-11-12-44.7-59.3-101.3-106.3-170-141s-145.3-54.3-229-60H0V214z'/></svg>\n<svg x='74.9%' width='25.1%' viewBox='0 0 400000 548'\npreserveAspectRatio='xMaxYMin slice'><path d='M399994 0l6 6\nv35l-6 11c-56 104-135.3 181.3-238 232-57.3 28.7-117 45-179 50H-300V214h399897\nc43.3-7 81-15 113-26 100.7-33 179.7-91 237-174 2.7-5 6-9 10-13 .7-1 7.3-1 20-1\nh17z'/></svg>"),'undergroup':Js("><svg width='50.1%' viewBox='0 0 400000 342'\npreserveAspectRatio='xMinYMin slice'><path d='M400000 262\nH435C64 262 168.3 112.6 21 82c-5.9-1.2-18 0-18 0-2 0-3 1-3 3v38c76 158 257 219\n 435 219h399565z'/></svg><svg x='50%' width='50%' viewBox='0 0 400000 342'\npreserveAspectRatio='xMaxYMin slice'><path d='M0 262h399565\nc371 0 266.7-149.4 414-180 5.9-1.2 18 0 18 0 2 0 3 1 3 3v38c-76 158-257\n 219-435 219H0z'/></svg>"),'widehat1':Js(" viewBox='0 0 1062 239' preserveAspectRatio='none'>\n<path d='M529 0h5l519 115c5 1 9 5 9 10 0 1-1 2-1 3l-4 22\nc-1 5-5 9-11 9h-2L532 67 19 159h-2c-5 0-9-4-11-9l-5-22c-1-6 2-12 8-13z'/>"),'widehat2':Js(" viewBox='0 0 2364 300' preserveAspectRatio='none'>\n<path d='M1181 0h2l1171 176c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 220h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'/>"),'widehat3':Js(" viewBox='0 0 2364 360' preserveAspectRatio='none'>\n<path d='M1181 0h2l1171 236c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 280h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'/>"),'widehat4':Js(" viewBox='0 0 2364 420' preserveAspectRatio='none'>\n<path d='M1181 0h2l1171 296c6 0 10 5 10 11l-2 23c-1 6-5 10\n-11 10h-1L1182 67 15 340h-1c-6 0-10-4-11-10l-2-23c-1-6 4-11 10-11z'/>"),'xcancel':Js("<line x1='0' y1='0' x2='100%' y2='100%' stroke-width='0.046em'/>\n<line x1='0' y1='100%' x2='100%' y2='0' stroke-width='0.046em'/>")})
        var.put('c', PyJs_Object_777_)
        @Js
        def PyJs_e_781_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_781_}, var)
            var.registers(['p', 'm', 'h', 'l', 'r', 'v', 'd', 'n', 'u', 's', 'f', 't'])
            var.put('n', var.get('t').get('value').get('label').callprop('substr', Js(1.0)))
            var.put('l', Js(0.0))
            var.put('s', Js(0.0))
            var.put('u', Js(''))
            var.put('f', Js(0.0))
            if var.get('i').callprop('contains', Js([Js('widehat'), Js('widetilde'), Js('undertilde')]), var.get('n')):
                var.put('h', var.get('t').get('value').get('value').get('length'))
                if (var.get('h')>Js(5.0)):
                    var.put('l', Js(0.312))
                    var.put('u', ((Js('widehat') if PyJsStrictEq(var.get('n'),Js('widehat')) else Js('tilde'))+Js('4')))
                else:
                    var.put('v', Js([Js(1.0), Js(1.0), Js(2.0), Js(2.0), Js(3.0), Js(3.0)]).get(var.get('h')))
                    if PyJsStrictEq(var.get('n'),Js('widehat')):
                        var.put('l', Js([Js(0.0), Js(0.24), Js(0.3), Js(0.3), Js(0.36), Js(0.36)]).get(var.get('h')))
                        var.put('u', (Js('widehat')+var.get('v')))
                    else:
                        var.put('l', Js([Js(0.0), Js(0.26), Js(0.3), Js(0.3), Js(0.34), Js(0.34)]).get(var.get('h')))
                        var.put('u', (Js('tilde')+var.get('v')))
            else:
                var.put('d', var.get('o').get(var.get('n')))
                var.put('l', var.get('d').get('0'))
                var.put('s', var.get('d').get('1'))
                var.put('u', var.get('d').get('2'))
                var.put('f', var.get('d').get('3'))
            var.put('p', var.get('a').callprop('makeSpan', Js([]), Js([]), var.get('r')))
            var.get('p').put('height', var.get('l'))
            var.get('p').put('depth', var.get('s'))
            var.put('m', (var.get('l')+var.get('s')))
            var.get('p').get('style').put('height', (var.get('m')+Js('em')))
            if (var.get('f')>Js(0.0)):
                var.get('p').get('style').put('minWidth', (var.get('f')+Js('em')))
            var.get('p').put('innerHTML', ((((Js("<svg width='100%' height='")+var.get('m'))+Js("em'"))+var.get('c').get(var.get('u')))+Js('</svg>')))
            return var.get('p')
        PyJs_e_781_._set_name('e')
        var.put('f', PyJs_e_781_)
        @Js
        def PyJs_e_782_(t, r, n, i, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'n':n, 'i':i, 'this':this, 'arguments':arguments, 'e':PyJs_e_782_}, var)
            var.registers(['i', 'r', 'l', 'n', 's', 't'])
            var.put('l', PyJsComma(Js(0.0), Js(None)))
            var.put('s', ((var.get('t').get('height')+var.get('t').get('depth'))+(Js(2.0)*var.get('n'))))
            if PyJsStrictEq(var.get('r'),Js('fbox')):
                var.put('l', var.get('a').callprop('makeSpan', Js([Js('stretchy'), var.get('r')]), Js([]), var.get('i')))
                if var.get('i').get('color'):
                    var.get('l').get('style').put('borderColor', var.get('i').callprop('getColor'))
            else:
                var.put('l', var.get('a').callprop('makeSpan', Js([]), Js([]), var.get('i')))
                var.get('l').put('innerHTML', ((((Js("<svg width='100%' height='")+var.get('s'))+Js("em'>"))+var.get('c').get(var.get('r')))+Js('</svg>')))
            var.get('l').put('height', var.get('s'))
            var.get('l').get('style').put('height', (var.get('s')+Js('em')))
            return var.get('l')
        PyJs_e_782_._set_name('e')
        var.put('h', PyJs_e_782_)
        PyJs_Object_783_ = Js({'encloseSpan':var.get('h'),'mathMLnode':var.get('s'),'svgSpan':var.get('f')})
        var.get('t').put('exports', PyJs_Object_783_)
    PyJs_anonymous_772_._set_name('anonymous')
    PyJs_Object_784_ = Js({'./buildCommon':Js(34.0),'./mathMLTree':Js(45.0),'./utils':Js(51.0)})
    @Js
    def PyJs_anonymous_785_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['B', 'R', 'q', 'E', 'r', 'o', 'y', 'T', 'N', 'i', 'h', 'v', 'w', 'x', 'e', 'a', 'A', 'S', 'O', '_', 'b', 'l', 'c', 'C', 'g', 'z', 'u', 'M', 'k', 't', 'p', 'm', 'd', 'n', 's', 'f'])
        @Js
        def PyJsHoisted_a_(e, r, a, n, i, l, this, arguments, var=var):
            var = Scope({'e':e, 'r':r, 'a':a, 'n':n, 'i':i, 'l':l, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r', 'l', 'n', 'e', 'a'])
            PyJs_Object_789_ = Js({'font':var.get('r'),'group':var.get('a'),'replace':var.get('n')})
            var.get('t').get('exports').get(var.get('e')).put(var.get('i'), PyJs_Object_789_)
            if var.get('l'):
                var.get('t').get('exports').get(var.get('e')).put(var.get('n'), var.get('t').get('exports').get(var.get('e')).get(var.get('i')))
        PyJsHoisted_a_.func_name = 'a'
        var.put('a', PyJsHoisted_a_)
        Js('use strict')
        PyJs_Object_787_ = Js({})
        PyJs_Object_788_ = Js({})
        PyJs_Object_786_ = Js({'math':PyJs_Object_787_,'text':PyJs_Object_788_})
        var.get('t').put('exports', PyJs_Object_786_)
        pass
        var.put('n', Js('math'))
        var.put('i', Js('text'))
        var.put('l', Js('main'))
        var.put('s', Js('ams'))
        var.put('o', Js('accent'))
        var.put('u', Js('bin'))
        var.put('c', Js('close'))
        var.put('f', Js('inner'))
        var.put('h', Js('mathord'))
        var.put('v', Js('op'))
        var.put('d', Js('open'))
        var.put('p', Js('punct'))
        var.put('m', Js('rel'))
        var.put('g', Js('spacing'))
        var.put('y', Js('textord'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≡'), Js('\\equiv'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≺'), Js('\\prec'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≻'), Js('\\succ'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∼'), Js('\\sim'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊥'), Js('\\perp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⪯'), Js('\\preceq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⪰'), Js('\\succeq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≃'), Js('\\simeq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∣'), Js('\\mid'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≪'), Js('\\ll'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≫'), Js('\\gg'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≍'), Js('\\asymp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∥'), Js('\\parallel'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⋈'), Js('\\bowtie'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⌣'), Js('\\smile'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊑'), Js('\\sqsubseteq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊒'), Js('\\sqsupseteq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≐'), Js('\\doteq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⌢'), Js('\\frown'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∋'), Js('\\ni'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∝'), Js('\\propto'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊢'), Js('\\vdash'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊣'), Js('\\dashv'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∋'), Js('\\owns'))
        var.get('a')(var.get('n'), var.get('l'), var.get('p'), Js('.'), Js('\\ldotp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('p'), Js('⋅'), Js('\\cdotp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('#'), Js('\\#'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('#'), Js('\\#'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('&'), Js('\\&'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('&'), Js('\\&'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('ℵ'), Js('\\aleph'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∀'), Js('\\forall'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('ℏ'), Js('\\hbar'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∃'), Js('\\exists'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∇'), Js('\\nabla'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♭'), Js('\\flat'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('ℓ'), Js('\\ell'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♮'), Js('\\natural'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♣'), Js('\\clubsuit'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('℘'), Js('\\wp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♯'), Js('\\sharp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♢'), Js('\\diamondsuit'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('ℜ'), Js('\\Re'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♡'), Js('\\heartsuit'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('ℑ'), Js('\\Im'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('♠'), Js('\\spadesuit'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('†'), Js('\\dag'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('†'), Js('\\dag'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('†'), Js('\\textdagger'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('‡'), Js('\\ddag'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('‡'), Js('\\ddag'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('†'), Js('\\textdaggerdbl'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('⎱'), Js('\\rmoustache'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('⎰'), Js('\\lmoustache'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('⟯'), Js('\\rgroup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('⟮'), Js('\\lgroup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∓'), Js('\\mp'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊖'), Js('\\ominus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊎'), Js('\\uplus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊓'), Js('\\sqcap'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∗'), Js('\\ast'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊔'), Js('\\sqcup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('◯'), Js('\\bigcirc'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∙'), Js('\\bullet'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('‡'), Js('\\ddagger'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('≀'), Js('\\wr'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⨿'), Js('\\amalg'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟵'), Js('\\longleftarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇐'), Js('\\Leftarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟸'), Js('\\Longleftarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟶'), Js('\\longrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇒'), Js('\\Rightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟹'), Js('\\Longrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↔'), Js('\\leftrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟷'), Js('\\longleftrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇔'), Js('\\Leftrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟺'), Js('\\Longleftrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↦'), Js('\\mapsto'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⟼'), Js('\\longmapsto'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↗'), Js('\\nearrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↩'), Js('\\hookleftarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↪'), Js('\\hookrightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↘'), Js('\\searrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↼'), Js('\\leftharpoonup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇀'), Js('\\rightharpoonup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↙'), Js('\\swarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↽'), Js('\\leftharpoondown'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇁'), Js('\\rightharpoondown'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↖'), Js('\\nwarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇌'), Js('\\rightleftharpoons'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≮'), Js('\\nless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue010'), Js('\\nleqslant'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue011'), Js('\\nleqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪇'), Js('\\lneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≨'), Js('\\lneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue00c'), Js('\\lvertneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋦'), Js('\\lnsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪉'), Js('\\lnapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊀'), Js('\\nprec'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋠'), Js('\\npreceq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋨'), Js('\\precnsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪹'), Js('\\precnapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≁'), Js('\\nsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue006'), Js('\\nshortmid'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∤'), Js('\\nmid'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊬'), Js('\\nvdash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊭'), Js('\\nvDash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋪'), Js('\\ntriangleleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋬'), Js('\\ntrianglelefteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊊'), Js('\\subsetneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue01a'), Js('\\varsubsetneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⫋'), Js('\\subsetneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue017'), Js('\\varsubsetneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≯'), Js('\\ngtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue00f'), Js('\\ngeqslant'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue00e'), Js('\\ngeqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪈'), Js('\\gneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≩'), Js('\\gneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue00d'), Js('\\gvertneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋧'), Js('\\gnsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪊'), Js('\\gnapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊁'), Js('\\nsucc'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋡'), Js('\\nsucceq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋩'), Js('\\succnsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪺'), Js('\\succnapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≆'), Js('\\ncong'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue007'), Js('\\nshortparallel'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∦'), Js('\\nparallel'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊯'), Js('\\nVDash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋫'), Js('\\ntriangleright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋭'), Js('\\ntrianglerighteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue018'), Js('\\nsupseteqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊋'), Js('\\supsetneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue01b'), Js('\\varsupsetneq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⫌'), Js('\\supsetneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue019'), Js('\\varsupsetneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊮'), Js('\\nVdash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪵'), Js('\\precneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪶'), Js('\\succneqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('\ue016'), Js('\\nsubseteqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊴'), Js('\\unlhd'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊵'), Js('\\unrhd'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↚'), Js('\\nleftarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↛'), Js('\\nrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇍'), Js('\\nLeftarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇏'), Js('\\nRightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↮'), Js('\\nleftrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇎'), Js('\\nLeftrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('△'), Js('\\vartriangle'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ℏ'), Js('\\hslash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('▽'), Js('\\triangledown'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('◊'), Js('\\lozenge'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('Ⓢ'), Js('\\circledS'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('®'), Js('\\circledR'))
        var.get('a')(var.get('i'), var.get('s'), var.get('y'), Js('®'), Js('\\circledR'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('∡'), Js('\\measuredangle'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('∄'), Js('\\nexists'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('℧'), Js('\\mho'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('Ⅎ'), Js('\\Finv'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('⅁'), Js('\\Game'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('k'), Js('\\Bbbk'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('‵'), Js('\\backprime'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('▲'), Js('\\blacktriangle'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('▼'), Js('\\blacktriangledown'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('■'), Js('\\blacksquare'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('⧫'), Js('\\blacklozenge'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('★'), Js('\\bigstar'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('∢'), Js('\\sphericalangle'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('∁'), Js('\\complement'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ð'), Js('\\eth'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('╱'), Js('\\diagup'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('╲'), Js('\\diagdown'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('□'), Js('\\square'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('□'), Js('\\Box'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('◊'), Js('\\Diamond'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('¥'), Js('\\yen'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('✓'), Js('\\checkmark'))
        var.get('a')(var.get('i'), var.get('s'), var.get('y'), Js('✓'), Js('\\checkmark'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ℶ'), Js('\\beth'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ℸ'), Js('\\daleth'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ℷ'), Js('\\gimel'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ϝ'), Js('\\digamma'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('ϰ'), Js('\\varkappa'))
        var.get('a')(var.get('n'), var.get('s'), var.get('d'), Js('┌'), Js('\\ulcorner'))
        var.get('a')(var.get('n'), var.get('s'), var.get('c'), Js('┐'), Js('\\urcorner'))
        var.get('a')(var.get('n'), var.get('s'), var.get('d'), Js('└'), Js('\\llcorner'))
        var.get('a')(var.get('n'), var.get('s'), var.get('c'), Js('┘'), Js('\\lrcorner'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≦'), Js('\\leqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⩽'), Js('\\leqslant'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪕'), Js('\\eqslantless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≲'), Js('\\lesssim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪅'), Js('\\lessapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≊'), Js('\\approxeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋖'), Js('\\lessdot'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋘'), Js('\\lll'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≶'), Js('\\lessgtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋚'), Js('\\lesseqgtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪋'), Js('\\lesseqqgtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≑'), Js('\\doteqdot'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≓'), Js('\\risingdotseq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≒'), Js('\\fallingdotseq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∽'), Js('\\backsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋍'), Js('\\backsimeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⫅'), Js('\\subseteqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋐'), Js('\\Subset'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊏'), Js('\\sqsubset'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≼'), Js('\\preccurlyeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋞'), Js('\\curlyeqprec'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≾'), Js('\\precsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪷'), Js('\\precapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊲'), Js('\\vartriangleleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊴'), Js('\\trianglelefteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊨'), Js('\\vDash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊪'), Js('\\Vvdash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⌣'), Js('\\smallsmile'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⌢'), Js('\\smallfrown'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≏'), Js('\\bumpeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≎'), Js('\\Bumpeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≧'), Js('\\geqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⩾'), Js('\\geqslant'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪖'), Js('\\eqslantgtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≳'), Js('\\gtrsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪆'), Js('\\gtrapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋗'), Js('\\gtrdot'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋙'), Js('\\ggg'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≷'), Js('\\gtrless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋛'), Js('\\gtreqless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪌'), Js('\\gtreqqless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≖'), Js('\\eqcirc'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≗'), Js('\\circeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≜'), Js('\\triangleq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∼'), Js('\\thicksim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≈'), Js('\\thickapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⫆'), Js('\\supseteqq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋑'), Js('\\Supset'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊐'), Js('\\sqsupset'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≽'), Js('\\succcurlyeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋟'), Js('\\curlyeqsucc'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≿'), Js('\\succsim'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⪸'), Js('\\succapprox'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊳'), Js('\\vartriangleright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊵'), Js('\\trianglerighteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊩'), Js('\\Vdash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∣'), Js('\\shortmid'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∥'), Js('\\shortparallel'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≬'), Js('\\between'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋔'), Js('\\pitchfork'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∝'), Js('\\varpropto'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('◀'), Js('\\blacktriangleleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∴'), Js('\\therefore'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∍'), Js('\\backepsilon'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('▶'), Js('\\blacktriangleright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('∵'), Js('\\because'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋘'), Js('\\llless'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⋙'), Js('\\gggtr'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊲'), Js('\\lhd'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊳'), Js('\\rhd'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≂'), Js('\\eqsim'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⋈'), Js('\\Join'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≑'), Js('\\Doteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('∔'), Js('\\dotplus'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('∖'), Js('\\smallsetminus'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋒'), Js('\\Cap'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋓'), Js('\\Cup'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⩞'), Js('\\doublebarwedge'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊟'), Js('\\boxminus'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊞'), Js('\\boxplus'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋇'), Js('\\divideontimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋉'), Js('\\ltimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋊'), Js('\\rtimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋋'), Js('\\leftthreetimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋌'), Js('\\rightthreetimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋏'), Js('\\curlywedge'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋎'), Js('\\curlyvee'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊝'), Js('\\circleddash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊛'), Js('\\circledast'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋅'), Js('\\centerdot'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊺'), Js('\\intercal'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋒'), Js('\\doublecap'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⋓'), Js('\\doublecup'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊠'), Js('\\boxtimes'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇢'), Js('\\dashrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇠'), Js('\\dashleftarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇇'), Js('\\leftleftarrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇆'), Js('\\leftrightarrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇚'), Js('\\Lleftarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↞'), Js('\\twoheadleftarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↢'), Js('\\leftarrowtail'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↫'), Js('\\looparrowleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇋'), Js('\\leftrightharpoons'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↶'), Js('\\curvearrowleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↺'), Js('\\circlearrowleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↰'), Js('\\Lsh'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇈'), Js('\\upuparrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↿'), Js('\\upharpoonleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇃'), Js('\\downharpoonleft'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊸'), Js('\\multimap'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↭'), Js('\\leftrightsquigarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇉'), Js('\\rightrightarrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇄'), Js('\\rightleftarrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↠'), Js('\\twoheadrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↣'), Js('\\rightarrowtail'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↬'), Js('\\looparrowright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↷'), Js('\\curvearrowright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↻'), Js('\\circlearrowright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↱'), Js('\\Rsh'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇊'), Js('\\downdownarrows'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↾'), Js('\\upharpoonright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇂'), Js('\\downharpoonright'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇝'), Js('\\rightsquigarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇝'), Js('\\leadsto'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⇛'), Js('\\Rrightarrow'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('↾'), Js('\\restriction'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('‘'), Js('`'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('$'), Js('\\$'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('$'), Js('\\$'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('$'), Js('\\textdollar'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('%'), Js('\\%'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('%'), Js('\\%'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('_'), Js('\\_'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('_'), Js('\\_'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('_'), Js('\\textunderscore'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∠'), Js('\\angle'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∞'), Js('\\infty'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('′'), Js('\\prime'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('△'), Js('\\triangle'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Γ'), Js('\\Gamma'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Δ'), Js('\\Delta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Θ'), Js('\\Theta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Λ'), Js('\\Lambda'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Ξ'), Js('\\Xi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Π'), Js('\\Pi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Σ'), Js('\\Sigma'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Υ'), Js('\\Upsilon'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Φ'), Js('\\Phi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Ψ'), Js('\\Psi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('Ω'), Js('\\Omega'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('¬'), Js('\\neg'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('¬'), Js('\\lnot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('⊤'), Js('\\top'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('⊥'), Js('\\bot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∅'), Js('\\emptyset'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('∅'), Js('\\varnothing'))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('α'), Js('\\alpha'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('β'), Js('\\beta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('γ'), Js('\\gamma'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('δ'), Js('\\delta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ϵ'), Js('\\epsilon'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ζ'), Js('\\zeta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('η'), Js('\\eta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('θ'), Js('\\theta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ι'), Js('\\iota'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('κ'), Js('\\kappa'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('λ'), Js('\\lambda'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('μ'), Js('\\mu'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ν'), Js('\\nu'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ξ'), Js('\\xi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ο'), Js('\\omicron'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('π'), Js('\\pi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ρ'), Js('\\rho'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('σ'), Js('\\sigma'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('τ'), Js('\\tau'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('υ'), Js('\\upsilon'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ϕ'), Js('\\phi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('χ'), Js('\\chi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ψ'), Js('\\psi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ω'), Js('\\omega'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ε'), Js('\\varepsilon'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ϑ'), Js('\\vartheta'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ϖ'), Js('\\varpi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ϱ'), Js('\\varrho'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ς'), Js('\\varsigma'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('φ'), Js('\\varphi'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∗'), Js('*'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('+'), Js('+'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('−'), Js('-'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⋅'), Js('\\cdot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∘'), Js('\\circ'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('÷'), Js('\\div'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('±'), Js('\\pm'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('×'), Js('\\times'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∩'), Js('\\cap'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∪'), Js('\\cup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∖'), Js('\\setminus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∧'), Js('\\land'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∨'), Js('\\lor'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∧'), Js('\\wedge'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('∨'), Js('\\vee'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('√'), Js('\\surd'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('('), Js('('))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('['), Js('['))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('⟨'), Js('\\langle'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('∣'), Js('\\lvert'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('∥'), Js('\\lVert'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js(')'), Js(')'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js(']'), Js(']'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('?'), Js('?'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('!'), Js('!'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('⟩'), Js('\\rangle'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('∣'), Js('\\rvert'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('∥'), Js('\\rVert'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('='), Js('='))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('<'), Js('<'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('>'), Js('>'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js(':'), Js(':'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≈'), Js('\\approx'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≅'), Js('\\cong'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≥'), Js('\\ge'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≥'), Js('\\geq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('←'), Js('\\gets'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('>'), Js('\\gt'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∈'), Js('\\in'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('∉'), Js('\\notin'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('̸'), Js('\\not'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊂'), Js('\\subset'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊃'), Js('\\supset'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊆'), Js('\\subseteq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊇'), Js('\\supseteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊈'), Js('\\nsubseteq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('⊉'), Js('\\nsupseteq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⊨'), Js('\\models'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('←'), Js('\\leftarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≤'), Js('\\le'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≤'), Js('\\leq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('<'), Js('\\lt'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≠'), Js('\\ne'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('≠'), Js('\\neq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('→'), Js('\\rightarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('→'), Js('\\to'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≱'), Js('\\ngeq'))
        var.get('a')(var.get('n'), var.get('s'), var.get('m'), Js('≰'), Js('\\nleq'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\!'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), Js('\xa0'), Js('\\ '))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), Js('\xa0'), Js('~'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\,'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\:'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\;'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\enspace'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\qquad'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), var.get(u"null"), Js('\\quad'))
        var.get('a')(var.get('n'), var.get('l'), var.get('g'), Js('\xa0'), Js('\\space'))
        var.get('a')(var.get('n'), var.get('l'), var.get('p'), Js(','), Js(','))
        var.get('a')(var.get('n'), var.get('l'), var.get('p'), Js(';'), Js(';'))
        var.get('a')(var.get('n'), var.get('l'), var.get('p'), Js(':'), Js('\\colon'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊼'), Js('\\barwedge'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊻'), Js('\\veebar'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊙'), Js('\\odot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊕'), Js('\\oplus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊗'), Js('\\otimes'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∂'), Js('\\partial'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⊘'), Js('\\oslash'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊚'), Js('\\circledcirc'))
        var.get('a')(var.get('n'), var.get('s'), var.get('u'), Js('⊡'), Js('\\boxdot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('△'), Js('\\bigtriangleup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('▽'), Js('\\bigtriangledown'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('†'), Js('\\dagger'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⋄'), Js('\\diamond'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('⋆'), Js('\\star'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('◃'), Js('\\triangleleft'))
        var.get('a')(var.get('n'), var.get('l'), var.get('u'), Js('▹'), Js('\\triangleright'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('{'), Js('\\{'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('{'), Js('\\{'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('{'), Js('\\textbraceleft'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('}'), Js('\\}'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('}'), Js('\\}'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('}'), Js('\\textbraceright'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('{'), Js('\\lbrace'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('}'), Js('\\rbrace'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('['), Js('\\lbrack'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js(']'), Js('\\rbrack'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('<'), Js('\\textless'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('>'), Js('\\textgreater'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('⌊'), Js('\\lfloor'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('⌋'), Js('\\rfloor'))
        var.get('a')(var.get('n'), var.get('l'), var.get('d'), Js('⌈'), Js('\\lceil'))
        var.get('a')(var.get('n'), var.get('l'), var.get('c'), Js('⌉'), Js('\\rceil'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('\\'), Js('\\backslash'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∣'), Js('|'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∣'), Js('\\vert'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('|'), Js('\\textbar'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∥'), Js('\\|'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('∥'), Js('\\Vert'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('∥'), Js('\\textbardbl'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↑'), Js('\\uparrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇑'), Js('\\Uparrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↓'), Js('\\downarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇓'), Js('\\Downarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('↕'), Js('\\updownarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('m'), Js('⇕'), Js('\\Updownarrow'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∐'), Js('\\coprod'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⋁'), Js('\\bigvee'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⋀'), Js('\\bigwedge'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⨄'), Js('\\biguplus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⋂'), Js('\\bigcap'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⋃'), Js('\\bigcup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∫'), Js('\\int'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∫'), Js('\\intop'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∬'), Js('\\iint'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∭'), Js('\\iiint'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∏'), Js('\\prod'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∑'), Js('\\sum'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⨂'), Js('\\bigotimes'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⨁'), Js('\\bigoplus'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⨀'), Js('\\bigodot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∮'), Js('\\oint'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('⨆'), Js('\\bigsqcup'))
        var.get('a')(var.get('n'), var.get('l'), var.get('v'), Js('∫'), Js('\\smallint'))
        var.get('a')(var.get('i'), var.get('l'), var.get('f'), Js('…'), Js('\\textellipsis'))
        var.get('a')(var.get('n'), var.get('l'), var.get('f'), Js('…'), Js('\\mathellipsis'))
        var.get('a')(var.get('i'), var.get('l'), var.get('f'), Js('…'), Js('\\ldots'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('f'), Js('…'), Js('\\ldots'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('f'), Js('⋯'), Js('\\cdots'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('f'), Js('⋱'), Js('\\ddots'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('⋮'), Js('\\vdots'), Js(True))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('´'), Js('\\acute'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('`'), Js('\\grave'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('¨'), Js('\\ddot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('~'), Js('\\tilde'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('¯'), Js('\\bar'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('˘'), Js('\\breve'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('ˇ'), Js('\\check'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('^'), Js('\\hat'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('⃗'), Js('\\vec'))
        var.get('a')(var.get('n'), var.get('l'), var.get('o'), Js('˙'), Js('\\dot'))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ı'), Js('\\imath'))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('ȷ'), Js('\\jmath'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('ˊ'), Js("\\'"))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('ˋ'), Js('\\`'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('ˆ'), Js('\\^'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('˜'), Js('\\~'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('ˉ'), Js('\\='))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('˘'), Js('\\u'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('˙'), Js('\\.'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('˚'), Js('\\r'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('ˇ'), Js('\\v'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('¨'), Js('\\"'))
        var.get('a')(var.get('i'), var.get('l'), var.get('o'), Js('̋'), Js('\\H'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('–'), Js('--'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('–'), Js('\\textendash'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('—'), Js('---'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('—'), Js('\\textemdash'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('‘'), Js('`'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('‘'), Js('\\textquoteleft'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('’'), Js("'"))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('’'), Js('\\textquoteright'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('“'), Js('``'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('“'), Js('\\textquotedblleft'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('”'), Js("''"))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('”'), Js('\\textquotedblright'))
        var.get('a')(var.get('n'), var.get('l'), var.get('y'), Js('°'), Js('\\degree'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('°'), Js('\\degree'))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('£'), Js('\\pounds'))
        var.get('a')(var.get('n'), var.get('l'), var.get('h'), Js('£'), Js('\\mathsterling'))
        var.get('a')(var.get('i'), var.get('l'), var.get('h'), Js('£'), Js('\\pounds'))
        var.get('a')(var.get('i'), var.get('l'), var.get('h'), Js('£'), Js('\\textsterling'))
        var.get('a')(var.get('n'), var.get('s'), var.get('y'), Js('✠'), Js('\\maltese'))
        var.get('a')(var.get('i'), var.get('s'), var.get('y'), Js('✠'), Js('\\maltese'))
        var.get('a')(var.get('i'), var.get('l'), var.get('g'), Js('\xa0'), Js('\\ '))
        var.get('a')(var.get('i'), var.get('l'), var.get('g'), Js('\xa0'), Js(' '))
        var.get('a')(var.get('i'), var.get('l'), var.get('g'), Js('\xa0'), Js('~'))
        var.put('x', Js('0123456789/@."'))
        #for JS loop
        var.put('w', Js(0.0))
        while (var.get('w')<var.get('x').get('length')):
            try:
                var.put('b', var.get('x').callprop('charAt', var.get('w')))
                var.get('a')(var.get('n'), var.get('l'), var.get('y'), var.get('b'), var.get('b'))
            finally:
                    (var.put('w',Js(var.get('w').to_number())+Js(1))-Js(1))
        var.put('k', Js('0123456789!@*()-=+[]<>|";:?/.,'))
        #for JS loop
        var.put('M', Js(0.0))
        while (var.get('M')<var.get('k').get('length')):
            try:
                var.put('z', var.get('k').callprop('charAt', var.get('M')))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('z'), var.get('z'))
            finally:
                    (var.put('M',Js(var.get('M').to_number())+Js(1))-Js(1))
        var.put('S', Js('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        #for JS loop
        var.put('A', Js(0.0))
        while (var.get('A')<var.get('S').get('length')):
            try:
                var.put('C', var.get('S').callprop('charAt', var.get('A')))
                var.get('a')(var.get('n'), var.get('l'), var.get('h'), var.get('C'), var.get('C'))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('C'), var.get('C'))
            finally:
                    (var.put('A',Js(var.get('A').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('T', Js(192.0))
        while (var.get('T')<=Js(214.0)):
            try:
                var.put('N', var.get('String').callprop('fromCharCode', var.get('T')))
                var.get('a')(var.get('n'), var.get('l'), var.get('h'), var.get('N'), var.get('N'))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('N'), var.get('N'))
            finally:
                    (var.put('T',Js(var.get('T').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('R', Js(216.0))
        while (var.get('R')<=Js(246.0)):
            try:
                var.put('q', var.get('String').callprop('fromCharCode', var.get('R')))
                var.get('a')(var.get('n'), var.get('l'), var.get('h'), var.get('q'), var.get('q'))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('q'), var.get('q'))
            finally:
                    (var.put('R',Js(var.get('R').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('_', Js(248.0))
        while (var.get('_')<=Js(255.0)):
            try:
                var.put('E', var.get('String').callprop('fromCharCode', var.get('_')))
                var.get('a')(var.get('n'), var.get('l'), var.get('h'), var.get('E'), var.get('E'))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('E'), var.get('E'))
            finally:
                    (var.put('_',Js(var.get('_').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('B', Js(1040.0))
        while (var.get('B')<=Js(1103.0)):
            try:
                var.put('O', var.get('String').callprop('fromCharCode', var.get('B')))
                var.get('a')(var.get('i'), var.get('l'), var.get('y'), var.get('O'), var.get('O'))
            finally:
                    (var.put('B',Js(var.get('B').to_number())+Js(1))-Js(1))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('–'), Js('–'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('—'), Js('—'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('‘'), Js('‘'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('’'), Js('’'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('“'), Js('“'))
        var.get('a')(var.get('i'), var.get('l'), var.get('y'), Js('”'), Js('”'))
    PyJs_anonymous_785_._set_name('anonymous')
    PyJs_Object_790_ = Js({})
    @Js
    def PyJs_anonymous_791_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'n', 'e', 'a', 't'])
        Js('use strict')
        var.put('a', JsRegExp('/[\\uAC00-\\uD7AF]/'))
        var.put('n', JsRegExp('/[\\u3000-\\u30FF\\u4E00-\\u9FAF\\uAC00-\\uD7AF\\uFF00-\\uFF60]/'))
        PyJs_Object_792_ = Js({'cjkRegex':var.get('n'),'hangulRegex':var.get('a')})
        var.get('t').put('exports', PyJs_Object_792_)
    PyJs_anonymous_791_._set_name('anonymous')
    PyJs_Object_793_ = Js({})
    @Js
    def PyJs_anonymous_794_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'l', 'r', 'o', 'n', 'u', 's', 'e', 'a', 't'])
        @Js
        def PyJsHoisted_i_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            PyJs_Object_795_ = Js({'default':var.get('e')})
            return (var.get('e') if (var.get('e') and var.get('e').get('__esModule')) else PyJs_Object_795_)
        PyJsHoisted_i_.func_name = 'i'
        var.put('i', PyJsHoisted_i_)
        Js('use strict')
        var.put('a', var.get('e')(Js('./ParseError')))
        var.put('n', var.get('i')(var.get('a')))
        pass
        PyJs_Object_796_ = Js({'pt':Js(1.0),'mm':(Js(7227.0)/Js(2540.0)),'cm':(Js(7227.0)/Js(254.0)),'in':Js(72.27),'bp':(Js(803.0)/Js(800.0)),'pc':Js(12.0),'dd':(Js(1238.0)/Js(1157.0)),'cc':(Js(14856.0)/Js(1157.0)),'nd':(Js(685.0)/Js(642.0)),'nc':(Js(1370.0)/Js(107.0)),'sp':(Js(1.0)/Js(65536.0)),'px':(Js(803.0)/Js(800.0))})
        var.put('l', PyJs_Object_796_)
        PyJs_Object_797_ = Js({'ex':Js(True),'em':Js(True),'mu':Js(True)})
        var.put('s', PyJs_Object_797_)
        @Js
        def PyJs_e_798_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_798_}, var)
            var.registers(['t'])
            if var.get('t').get('unit'):
                var.put('t', var.get('t').get('unit'))
            return ((var.get('l').contains(var.get('t')) or var.get('s').contains(var.get('t'))) or PyJsStrictEq(var.get('t'),Js('ex')))
        PyJs_e_798_._set_name('e')
        var.put('o', PyJs_e_798_)
        @Js
        def PyJs_e_799_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_799_}, var)
            var.registers(['r', 'a', 't', 'i'])
            var.put('a', PyJsComma(Js(0.0), Js(None)))
            if var.get('l').contains(var.get('t').get('unit')):
                var.put('a', ((var.get('l').get(var.get('t').get('unit'))/var.get('r').callprop('fontMetrics').get('ptPerEm'))/var.get('r').get('sizeMultiplier')))
            else:
                if PyJsStrictEq(var.get('t').get('unit'),Js('mu')):
                    var.put('a', var.get('r').callprop('fontMetrics').get('cssEmPerMu'))
                else:
                    var.put('i', PyJsComma(Js(0.0), Js(None)))
                    if var.get('r').get('style').callprop('isTight'):
                        var.put('i', var.get('r').callprop('havingStyle', var.get('r').get('style').callprop('text')))
                    else:
                        var.put('i', var.get('r'))
                    if PyJsStrictEq(var.get('t').get('unit'),Js('ex')):
                        var.put('a', var.get('i').callprop('fontMetrics').get('xHeight'))
                    else:
                        if PyJsStrictEq(var.get('t').get('unit'),Js('em')):
                            var.put('a', var.get('i').callprop('fontMetrics').get('quad'))
                        else:
                            PyJsTempException = JsToPyException(var.get('n').get('default').create(((Js("Invalid unit: '")+var.get('t').get('unit'))+Js("'"))))
                            raise PyJsTempException
                    if PyJsStrictNeq(var.get('i'),var.get('r')):
                        var.put('a', (var.get('i').get('sizeMultiplier')/var.get('r').get('sizeMultiplier')), '*')
            return (var.get('t').get('number')*var.get('a'))
        PyJs_e_799_._set_name('e')
        var.put('u', PyJs_e_799_)
        PyJs_Object_800_ = Js({'validUnit':var.get('o'),'calculateSize':var.get('u')})
        var.get('t').put('exports', PyJs_Object_800_)
    PyJs_anonymous_794_._set_name('anonymous')
    PyJs_Object_801_ = Js({'./ParseError':Js(29.0)})
    @Js
    def PyJs_anonymous_802_(e, t, r, this, arguments, var=var):
        var = Scope({'e':e, 't':t, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['p', 'i', 'h', 'l', 'r', 'v', 'c', 'o', 'd', 'n', 'u', 's', 'e', 'a', 'f', 't'])
        @Js
        def PyJsHoisted_f_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            return var.get('u').get(var.get('e'))
        PyJsHoisted_f_.func_name = 'f'
        var.put('f', PyJsHoisted_f_)
        @Js
        def PyJsHoisted_h_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            return (Js('')+var.get('e')).callprop('replace', var.get('c'), var.get('f'))
        PyJsHoisted_h_.func_name = 'h'
        var.put('h', PyJsHoisted_h_)
        @Js
        def PyJsHoisted_p_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            var.get('v')(var.get('e'), Js(''))
        PyJsHoisted_p_.func_name = 'p'
        var.put('p', PyJsHoisted_p_)
        Js('use strict')
        var.put('a', var.get('Array').get('prototype').get('indexOf'))
        @Js
        def PyJs_e_803_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_803_}, var)
            var.registers(['r', 't', 'n', 'i'])
            if (var.get('t')==var.get(u"null")):
                return (-Js(1.0))
            if (var.get('a') and PyJsStrictEq(var.get('t').get('indexOf'),var.get('a'))):
                return var.get('t').callprop('indexOf', var.get('r'))
            var.put('n', var.get('t').get('length'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('n')):
                try:
                    if PyJsStrictEq(var.get('t').get(var.get('i')),var.get('r')):
                        return var.get('i')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return (-Js(1.0))
        PyJs_e_803_._set_name('e')
        var.put('n', PyJs_e_803_)
        @Js
        def PyJs_e_804_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_804_}, var)
            var.registers(['r', 't'])
            return PyJsStrictNeq(var.get('n')(var.get('t'), var.get('r')),(-Js(1.0)))
        PyJs_e_804_._set_name('e')
        var.put('i', PyJs_e_804_)
        @Js
        def PyJs_e_805_(t, r, this, arguments, var=var):
            var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_805_}, var)
            var.registers(['r', 't'])
            return (var.get('r') if PyJsStrictEq(var.get('t'),var.get('undefined')) else var.get('t'))
        PyJs_e_805_._set_name('e')
        var.put('l', PyJs_e_805_)
        var.put('s', JsRegExp('/([A-Z])/g'))
        @Js
        def PyJs_e_806_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments, 'e':PyJs_e_806_}, var)
            var.registers(['t'])
            return var.get('t').callprop('replace', var.get('s'), Js('-$1')).callprop('toLowerCase')
        PyJs_e_806_._set_name('e')
        var.put('o', PyJs_e_806_)
        PyJs_Object_807_ = Js({'&':Js('&amp;'),'>':Js('&gt;'),'<':Js('&lt;'),'"':Js('&quot;'),"'":Js('&#x27;')})
        var.put('u', PyJs_Object_807_)
        var.put('c', JsRegExp('/[&><"\']/g'))
        pass
        pass
        var.put('v', PyJsComma(Js(0.0), Js(None)))
        if PyJsStrictNeq(var.get('document',throw=False).typeof(),Js('undefined')):
            var.put('d', var.get('document').callprop('createElement', Js('span')))
            if var.get('d').contains(Js('textContent')):
                @Js
                def PyJs_e_808_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_808_}, var)
                    var.registers(['r', 't'])
                    var.get('t').put('textContent', var.get('r'))
                PyJs_e_808_._set_name('e')
                var.put('v', PyJs_e_808_)
            else:
                @Js
                def PyJs_e_809_(t, r, this, arguments, var=var):
                    var = Scope({'t':t, 'r':r, 'this':this, 'arguments':arguments, 'e':PyJs_e_809_}, var)
                    var.registers(['r', 't'])
                    var.get('t').put('innerText', var.get('r'))
                PyJs_e_809_._set_name('e')
                var.put('v', PyJs_e_809_)
        pass
        PyJs_Object_810_ = Js({'contains':var.get('i'),'deflt':var.get('l'),'escape':var.get('h'),'hyphenate':var.get('o'),'indexOf':var.get('n'),'setTextContent':var.get('v'),'clearNode':var.get('p')})
        var.get('t').put('exports', PyJs_Object_810_)
    PyJs_anonymous_802_._set_name('anonymous')
    PyJs_Object_811_ = Js({})
    PyJs_Object_1_ = Js({'1':Js([PyJs_anonymous_2_, PyJs_Object_9_]),'2':Js([PyJs_anonymous_10_, PyJs_Object_12_]),'3':Js([PyJs_anonymous_13_, PyJs_Object_15_]),'4':Js([PyJs_anonymous_16_, PyJs_Object_18_]),'5':Js([PyJs_anonymous_19_, PyJs_Object_23_]),'6':Js([PyJs_anonymous_24_, PyJs_Object_27_]),'7':Js([PyJs_anonymous_28_, PyJs_Object_30_]),'8':Js([PyJs_anonymous_31_, PyJs_Object_33_]),'9':Js([PyJs_anonymous_34_, PyJs_Object_36_]),'10':Js([PyJs_anonymous_37_, PyJs_Object_39_]),'11':Js([PyJs_anonymous_40_, PyJs_Object_46_]),'12':Js([PyJs_anonymous_47_, PyJs_Object_52_]),'13':Js([PyJs_anonymous_53_, PyJs_Object_56_]),'14':Js([PyJs_anonymous_57_, PyJs_Object_65_]),'15':Js([PyJs_anonymous_66_, PyJs_Object_68_]),'16':Js([PyJs_anonymous_69_, PyJs_Object_70_]),'17':Js([PyJs_anonymous_71_, PyJs_Object_74_]),'18':Js([PyJs_anonymous_75_, PyJs_Object_79_]),'19':Js([PyJs_anonymous_80_, PyJs_Object_82_]),'20':Js([PyJs_anonymous_83_, PyJs_Object_85_]),'21':Js([PyJs_anonymous_86_, PyJs_Object_89_]),'22':Js([PyJs_anonymous_90_, PyJs_Object_92_]),'23':Js([PyJs_anonymous_93_, PyJs_Object_95_]),'24':Js([PyJs_anonymous_96_, PyJs_Object_97_]),'25':Js([PyJs_anonymous_98_, PyJs_Object_105_]),'26':Js([PyJs_anonymous_106_, PyJs_Object_114_]),'27':Js([PyJs_anonymous_115_, PyJs_Object_125_]),'28':Js([PyJs_anonymous_126_, PyJs_Object_162_]),'29':Js([PyJs_anonymous_163_, PyJs_Object_166_]),'30':Js([PyJs_anonymous_167_, PyJs_Object_171_]),'31':Js([PyJs_anonymous_172_, PyJs_Object_236_]),'32':Js([PyJs_anonymous_237_, PyJs_Object_242_]),'33':Js([PyJs_anonymous_243_, PyJs_Object_261_]),'34':Js([PyJs_anonymous_262_, PyJs_Object_298_]),'35':Js([PyJs_anonymous_299_, PyJs_Object_424_]),'36':Js([PyJs_anonymous_425_, PyJs_Object_476_]),'37':Js([PyJs_anonymous_477_, PyJs_Object_482_]),'38':Js([PyJs_anonymous_483_, PyJs_Object_521_]),'39':Js([PyJs_anonymous_522_, PyJs_Object_551_]),'40':Js([PyJs_anonymous_552_, PyJs_Object_583_]),'41':Js([PyJs_anonymous_584_, PyJs_Object_594_]),'42':Js([PyJs_anonymous_595_, PyJs_Object_613_]),'43':Js([PyJs_anonymous_614_, PyJs_Object_748_]),'44':Js([PyJs_anonymous_749_, PyJs_Object_750_]),'45':Js([PyJs_anonymous_751_, PyJs_Object_767_]),'46':Js([PyJs_anonymous_768_, PyJs_Object_771_]),'47':Js([PyJs_anonymous_772_, PyJs_Object_784_]),'48':Js([PyJs_anonymous_785_, PyJs_Object_790_]),'49':Js([PyJs_anonymous_791_, PyJs_Object_793_]),'50':Js([PyJs_anonymous_794_, PyJs_Object_801_]),'51':Js([PyJs_anonymous_802_, PyJs_Object_811_])})
    PyJs_Object_812_ = Js({})
    @Js
    def PyJs_e_813_(t, r, a, this, arguments, var=var):
        var = Scope({'t':t, 'r':r, 'a':a, 'this':this, 'arguments':arguments, 'e':PyJs_e_813_}, var)
        var.registers(['i', 'r', 'l', 'n', 'a', 't'])
        @Js
        def PyJsHoisted_n_(l, s, this, arguments, var=var):
            var = Scope({'l':l, 's':s, 'this':this, 'arguments':arguments}, var)
            var.registers(['l', 'c', 'o', 'u', 's'])
            if var.get('r').get(var.get('l')).neg():
                if var.get('t').get(var.get('l')).neg():
                    var.put('o', ((var.get('require',throw=False).typeof()==Js('function')) and var.get('require')))
                    if (var.get('s').neg() and var.get('o')):
                        return var.get('o')(var.get('l'), Js(0.0).neg())
                    if var.get('i'):
                        return var.get('i')(var.get('l'), Js(0.0).neg())
                    var.put('u', var.get('Error').create(((Js("Cannot find module '")+var.get('l'))+Js("'"))))
                    PyJsTempException = JsToPyException(PyJsComma(var.get('u').put('code', Js('MODULE_NOT_FOUND')),var.get('u')))
                    raise PyJsTempException
                PyJs_Object_815_ = Js({})
                PyJs_Object_814_ = Js({'exports':PyJs_Object_815_})
                var.put('c', var.get('r').put(var.get('l'), PyJs_Object_814_))
                @Js
                def PyJs_anonymous_816_(e, this, arguments, var=var):
                    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
                    var.registers(['e', 'r'])
                    var.put('r', var.get('t').get(var.get('l')).get('1').get(var.get('e')))
                    return var.get('n')((var.get('r') if var.get('r') else var.get('e')))
                PyJs_anonymous_816_._set_name('anonymous')
                var.get('t').get(var.get('l')).get('0').callprop('call', var.get('c').get('exports'), PyJs_anonymous_816_, var.get('c'), var.get('c').get('exports'), var.get('e'), var.get('t'), var.get('r'), var.get('a'))
            return var.get('r').get(var.get('l')).get('exports')
        PyJsHoisted_n_.func_name = 'n'
        var.put('n', PyJsHoisted_n_)
        pass
        var.put('i', ((var.get('require',throw=False).typeof()==Js('function')) and var.get('require')))
        #for JS loop
        var.put('l', Js(0.0))
        while (var.get('l')<var.get('a').get('length')):
            try:
                var.get('n')(var.get('a').get(var.get('l')))
            finally:
                    (var.put('l',Js(var.get('l').to_number())+Js(1))-Js(1))
        return var.get('n')
    PyJs_e_813_._set_name('e')
    return PyJs_e_813_(PyJs_Object_1_, PyJs_Object_812_, Js([Js(1.0)]))(Js(1.0))
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_anonymous_817_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 't'])
    if (PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')) and PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined'))):
        var.get('module').put('exports', var.get('e')())
    else:
        if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')):
            var.get('define')(Js([]), var.get('e'))
        else:
            pass
            if PyJsStrictNeq(var.get('window',throw=False).typeof(),Js('undefined')):
                var.put('t', var.get('window'))
            else:
                if PyJsStrictNeq(var.get('global',throw=False).typeof(),Js('undefined')):
                    var.put('t', var.get('global'))
                else:
                    if PyJsStrictNeq(var.get('self',throw=False).typeof(),Js('undefined')):
                        var.put('t', var.get('self'))
                    else:
                        var.put('t', var.get(u"this"))
            var.get('t').put('katex', var.get('e')())
PyJs_anonymous_817_._set_name('anonymous')
PyJs_anonymous_817_(PyJs_anonymous_0_)
pass


# Add lib to the module scope
katex = var.to_python()