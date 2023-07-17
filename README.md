# nuitka_test_python37
Test environment with nuitka and python37

## debian buster python-3.7.X

- [dockerfile_buster_python372](./dockerfile_buster_python372): Debian buster with python-3.7.2 installation
- [dockerfile_buster_python373](./dockerfile_buster_python373): Debian buster with python-3.7.3 installation
- [dockerfile_buster_python374](./dockerfile_buster_python374): Debian buster with python-3.7.4 installation
- [dockerfile_buster_python376](./dockerfile_buster_python376): Debian buster with python-3.7.6 installation
- [dockerfile_buster_python378](./dockerfile_buster_python378): Debian buster with python-3.7.8 installation
- [dockerfile_buster_python3713](./dockerfile_buster_python3713): Debian buster with python-3.7.13 installation

Build command:
```console
docker built -f dockerfile_buster_python37X -t buster:python-3.7.X .
```

## test package compilation

This dockerfile is based on previous debian buster python-3.7.X.

It composes of 2 stages:
- first stage compile the source code with nuitka in a specific python3.7 version,
- second stage install the package (containing the `.so`) in another python3.7 version.

Build command:
```console
docker built -f dockerfile_test -t test .
```

Run command:
```console
docker run -it --entrypoint bash test
```

Debug commands:
```console
root@xxxxxxxxxxxx:/opt# python3 -m mypackage.demo
Segmentation fault (core dumped)
root@xxxxxxxxxxxx:/opt# gdb
GNU gdb (Debian 8.2.1-2+b3) 8.2.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) file python3
Reading symbols from python3...done.
(gdb) run /usr/local/lib/python3.7/site-packages/mypackage/demo/__main__.py
Starting program: /usr/local/bin/python3 /usr/local/lib/python3.7/site-packages/mypackage/demo/__main__.py
warning: Error disabling address space randomization: Operation not permitted
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
Nuitka_SetModule (module=<optimized out>, module_name=<optimized out>) at /usr/local/lib/python3.7/site-packages/nuitka/build/include/nuitka/importing.h:85
85      /usr/local/lib/python3.7/site-packages/nuitka/build/include/nuitka/importing.h: No such file or directory.
(gdb) bt
#0  Nuitka_SetModule (module=<optimized out>, module_name=<optimized out>) at /usr/local/lib/python3.7/site-packages/nuitka/build/include/nuitka/importing.h:85
#1  Nuitka_SetModuleString (module=<optimized out>, module_name=<optimized out>) at /usr/local/lib/python3.7/site-packages/nuitka/build/include/nuitka/importing.h:91
#2  PyInit_app () at module.app.c:843
#3  0x0000557c299a2f0d in _PyImport_LoadDynamicModuleWithSpec (spec=spec@entry=0x7f995fb1bd68, fp=fp@entry=0x0) at ./Python/importdl.c:159
#4  0x0000557c299a1193 in _imp_create_dynamic_impl (module=<optimized out>, file=<optimized out>, spec=0x7f995fb1bd68) at Python/import.c:2158
#5  _imp_create_dynamic (module=<optimized out>, args=<optimized out>, nargs=<optimized out>) at Python/clinic/import.c.h:289
#6  0x0000557c298dd301 in _PyMethodDef_RawFastCallDict (method=0x557c29b31660 <imp_methods+320>, self=0x7f995fc36778, args=0x7f995fb49098, nargs=1,
    kwargs=<optimized out>) at Objects/call.c:530
#7  0x0000557c298dd62e in _PyCFunction_FastCallDict (kwargs=<optimized out>, nargs=<optimized out>, args=<optimized out>, func=0x7f995fc3cd80) at Objects/call.c:582
#8  PyCFunction_Call (kwargs=<optimized out>, args=<optimized out>, func=0x7f995fc3cd80) at Objects/call.c:787
#9  PyCFunction_Call (func=0x7f995fc3cd80, args=<optimized out>, kwargs=<optimized out>) at Objects/call.c:778
#10 0x0000557c298c8880 in do_call_core (kwdict=0x7f995fbbd318, callargs=0x7f995fb49080, func=0x7f995fc3cd80) at Python/ceval.c:4641
#11 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3191
#12 0x0000557c299864f2 in PyEval_EvalFrameEx (throwflag=0, f=0x7f995fc45240) at Python/ceval.c:547
#13 _PyEval_EvalCodeWithName (_co=0x7f995fc5bdb0, globals=<optimized out>, locals=locals@entry=0x0, args=<optimized out>, argcount=2, kwnames=0x0,
    kwargs=0x7f995fae8908, kwcount=0, kwstep=1, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x7f995fc20b70, qualname=0x7f995fc20b70) at Python/ceval.c:3930
#14 0x0000557c298dc6f3 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=<optimized out>, nargs=<optimized out>, kwnames=<optimized out>)
    at Objects/call.c:433
#15 0x0000557c298c8c60 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>) at Python/ceval.c:4616
#16 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3093
#17 0x0000557c298c0653 in function_code_fastcall (co=<optimized out>, args=<optimized out>, nargs=2, globals=<optimized out>) at Objects/call.c:283
#18 0x0000557c298dc817 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=<optimized out>, nargs=<optimized out>, kwnames=<optimized out>)
    at Objects/call.c:415
#19 0x0000557c298c93d5 in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>) at Python/ceval.c:4616
#20 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3110
#21 0x0000557c298c0653 in function_code_fastcall (co=<optimized out>, args=<optimized out>, nargs=1, globals=<optimized out>) at Objects/call.c:283
#22 0x0000557c298dc817 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=<optimized out>, nargs=<optimized out>, kwnames=<optimized out>)
    at Objects/call.c:415
#23 0x0000557c298c83ef in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>) at Python/ceval.c:4616
#24 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3124
#25 0x0000557c298c0653 in function_code_fastcall (co=<optimized out>, args=<optimized out>, nargs=1, globals=<optimized out>) at Objects/call.c:283
#26 0x0000557c298dc817 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=<optimized out>, nargs=<optimized out>, kwnames=<optimized out>)
    at Objects/call.c:415
--Type <RET> for more, q to quit, c to continue without paging--
#27 0x0000557c298c83ef in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>) at Python/ceval.c:4616
#28 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3124
#29 0x0000557c298c0653 in function_code_fastcall (co=<optimized out>, args=<optimized out>, nargs=2, globals=<optimized out>) at Objects/call.c:283
#30 0x0000557c298dc817 in _PyFunction_FastCallKeywords (func=<optimized out>, stack=<optimized out>, nargs=<optimized out>, kwnames=<optimized out>)
    at Objects/call.c:415
#31 0x0000557c298c83ef in call_function (kwnames=0x0, oparg=<optimized out>, pp_stack=<synthetic pointer>) at Python/ceval.c:4616
#32 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:3124
#33 0x0000557c298c0653 in function_code_fastcall (co=co@entry=0x7f995fc35300, args=<optimized out>, args@entry=0x7ffc067f9e00, nargs=nargs@entry=2,
    globals=globals@entry=0x7f995fc2fbd0) at Objects/call.c:283
#34 0x0000557c298dc652 in _PyFunction_FastCallDict (func=0x7f995fc40d90, args=0x7ffc067f9e00, nargs=2, kwargs=0x0) at Objects/call.c:322
#35 0x0000557c298dde90 in object_vacall (callable=callable@entry=0x7f995fc40d90, vargs=vargs@entry=0x7ffc067f9e78) at Objects/call.c:1198
#36 0x0000557c298de0e5 in _PyObject_CallMethodIdObjArgs (obj=<optimized out>, name=name@entry=0x557c29b312e0 <PyId__find_and_load.15874>) at Objects/call.c:1248
#37 0x0000557c2999ef90 in import_find_and_load (abs_name=abs_name@entry=0x7f995fa5d8e8) at Python/import.c:1646
#38 0x0000557c299a2110 in PyImport_ImportModuleLevelObject (name=name@entry=0x7f995fa5d8e8, globals=<optimized out>, locals=<optimized out>,
    fromlist=fromlist@entry=0x7f995fc2d198, level=0) at Python/import.c:1754
#39 0x0000557c298c9fc3 in import_name (level=0x557c29b79220 <small_ints+160>, fromlist=0x7f995fc2d198, name=0x7f995fa5d8e8, f=0x7f995fc339f8) at Python/ceval.c:4770
#40 _PyEval_EvalFrameDefault (f=<optimized out>, throwflag=<optimized out>) at Python/ceval.c:2600
#41 0x0000557c299864f2 in PyEval_EvalFrameEx (throwflag=0, f=0x7f995fc339f8) at Python/ceval.c:547
#42 _PyEval_EvalCodeWithName (_co=_co@entry=0x7f995fbbf660, globals=globals@entry=0x0, locals=locals@entry=0x7f995fb870d8, args=args@entry=0x0,
    argcount=argcount@entry=0, kwnames=kwnames@entry=0x0, kwargs=0x0, kwcount=0, kwstep=2, defs=0x0, defcount=0, kwdefs=0x0, closure=0x0, name=0x0, qualname=0x0)
    at Python/ceval.c:3930
#43 0x0000557c29986753 in PyEval_EvalCodeEx (closure=0x0, kwdefs=0x0, defcount=0, defs=0x0, kwcount=0, kws=0x0, argcount=0, args=0x0,
    locals=locals@entry=0x7f995fb870d8, globals=globals@entry=0x0, _co=_co@entry=0x7f995fbbf660) at Python/ceval.c:3959
#44 PyEval_EvalCode (co=co@entry=0x7f995fbbf660, globals=globals@entry=0x7f995fb870d8, locals=locals@entry=0x7f995fb870d8) at Python/ceval.c:524
#45 0x0000557c299b86a2 in run_mod (arena=0x7f995fc810a8, flags=0x7ffc067fa2ac, locals=0x7f995fb870d8, globals=0x7f995fb870d8, filename=0x7f995fac07b0,
    mod=0x557c2a532158) at Python/pythonrun.c:1035
#46 PyRun_FileExFlags (fp=<optimized out>, filename_str=<optimized out>, start=<optimized out>, globals=0x7f995fb870d8, locals=0x7f995fb870d8, closeit=1,
    flags=0x7ffc067fa2ac) at Python/pythonrun.c:988
#47 0x0000557c299b882d in PyRun_SimpleFileExFlags (fp=fp@entry=0x557c2a535e90, filename=<optimized out>, closeit=closeit@entry=1, flags=flags@entry=0x7ffc067fa2ac)
    at Python/pythonrun.c:429
#48 0x0000557c299b8ce3 in PyRun_AnyFileExFlags (fp=fp@entry=0x557c2a535e90, filename=<optimized out>, closeit=closeit@entry=1, flags=flags@entry=0x7ffc067fa2ac)
    at Python/pythonrun.c:84
#49 0x0000557c298d0ecb in pymain_run_file (p_cf=0x7ffc067fa2ac, filename=<optimized out>, fp=0x557c2a535e90) at Modules/main.c:427
--Type <RET> for more, q to quit, c to continue without paging--
#50 pymain_run_filename (cf=0x7ffc067fa2ac, pymain=0x7ffc067fa380) at Modules/main.c:1627
#51 pymain_run_python (pymain=0x7ffc067fa380) at Modules/main.c:2877
#52 pymain_main (pymain=pymain@entry=0x7ffc067fa380) at Modules/main.c:3038
#53 0x0000557c298d10f9 in _Py_UnixMain (argc=<optimized out>, argv=<optimized out>) at Modules/main.c:3073
#54 0x00007f995fce809b in __libc_start_main (main=0x557c298c05e0 <main>, argc=2, argv=0x7ffc067fa4c8, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7ffc067fa4b8) at ../csu/libc-start.c:308
#55 0x0000557c298cadba in _start () at Objects/call.c:28
```