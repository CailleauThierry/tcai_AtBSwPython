04_09_2021
-------------------------------
I got lost for a while, switch to a previously commit point to see if it used to work better


Then I started watching this video:
https://www.youtube-nocookie.com/embed/G-7J9dU7QHo?autoplay=1&iv_load_policy=3&loop=1&modestbranding=1&playlist=G-7J9dU7QHo

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)
$ ls
00_core.ipynb       05_guess_the_number.ipynb  docker-compose.yml  index.ipynb  Makefile     Notes_Readme.md  settings.ini  tcai_AtBSwPython/
04_functions.ipynb  CONTRIBUTING.md            docs/               LICENSE      MANIFEST.in  README.md        setup.py

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)
$ nbdev_build_lib
Converted 00_core.ipynb.
Converted 04_functions.ipynb.
Converted 05_guess_the_number.ipynb.
Converted index.ipynb.



04_07_2021
-------------------------------
Trying to reproduce what I learn from following this YouTube Tutorial for nbdev...:

https://github.com/CailleauThierry/tcai_mages

... and trying to apply it to "Automate the Boring Stuff with Python" on Udemy

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)
$ nbdev_build_docs
converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\00_core.ipynb
An error occurred while executing the following cell:
------------------
from nbdev.showdoc import show_doc
from tcai_AtBSwPython.core import *
------------------

←[1;31m---------------------------------------------------------------------------←[0m
←[1;31mModuleNotFoundError←[0m                       Traceback (most recent call last)
←[1;32m<ipython-input-1-c545cbfc6508>←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      1←[0m ←[1;32mfrom←[0m ←[0mnbdev←[0m←[1;33m.←[0m←[0mshowdoc←[0m ←[1;32mimport←[0m ←[0mshow_doc←[0m←[1;33m←[0m←[1;33m←[0m←[0m       
←[1;32m----> 2←[1;33m ←[1;32mfrom←[0m ←[0mtcai_AtBSwPython←[0m←[1;33m.←[0m←[0mcore←[0m ←[1;32mimport←[0m ←[1;33m*←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;31mModuleNotFoundError←[0m: No module named 'tcai_AtBSwPython'
ModuleNotFoundError: No module named 'tcai_AtBSwPython'

converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\04_functions.ipynb
An error occurred while executing the following cell:
------------------
from nbdev.showdoc import show_doc
from tcai_AtBSwPython.core import *
------------------

←[1;31m---------------------------------------------------------------------------←[0m
←[1;31mModuleNotFoundError←[0m                       Traceback (most recent call last)
←[1;32m<ipython-input-1-c545cbfc6508>←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      1←[0m ←[1;32mfrom←[0m ←[0mnbdev←[0m←[1;33m.←[0m←[0mshowdoc←[0m ←[1;32mimport←[0m ←[0mshow_doc←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 2←[1;33m ←[1;32mfrom←[0m ←[0mtcai_AtBSwPython←[0m←[1;33m.←[0m←[0mcore←[0m ←[1;32mimport←[0m ←[1;33m*←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;31mModuleNotFoundError←[0m: No module named 'tcai_AtBSwPython'
ModuleNotFoundError: No module named 'tcai_AtBSwPython'

converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\05_guess_the_number.ipynb
An error occurred while executing the following cell:
------------------
from nbdev.showdoc import show_doc
from tcai_AtBSwPython.core import *
------------------

←[1;31m---------------------------------------------------------------------------←[0m
←[1;31mModuleNotFoundError←[0m                       Traceback (most recent call last)
←[1;32m<ipython-input-1-c545cbfc6508>←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      1←[0m ←[1;32mfrom←[0m ←[0mnbdev←[0m←[1;33m.←[0m←[0mshowdoc←[0m ←[1;32mimport←[0m ←[0mshow_doc←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 2←[1;33m ←[1;32mfrom←[0m ←[0mtcai_AtBSwPython←[0m←[1;33m.←[0m←[0mcore←[0m ←[1;32mimport←[0m ←[1;33m*←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;31mModuleNotFoundError←[0m: No module named 'tcai_AtBSwPython'
ModuleNotFoundError: No module named 'tcai_AtBSwPython'

converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\index.ipynb
Conversion failed on the following:
00_core.ipynb
04_functions.ipynb
05_guess_the_number.ipynb
Traceback (most recent call last):
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\tcailleau\AppData\Local\Programs\Python\Python39\Scripts\nbdev_build_docs.exe\__main__.py", line 7, in <module>
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\fastcore\script.py", line 105, in _f
    tfunc(**merge(args, args_from_prog(func, xtra)))
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 665, in nbdev_build_docs
    if fname is None: make_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 730, in make_sidebar
    create_default_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 722, in create_default_sidebar
    dic = {Config().lib_name: _create_default_sidebar()}
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in _create_default_sidebar
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in <listcomp>
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 704, in _get_title
    with open(fname, 'r') as f: code = f.read()
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\tcailleau\\Documents\\Python\\tcai_AtBSwPython\\docs\\core.html'

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)
$ nbdev_build_lib
Converted 00_core.ipynb.
Converted 04_functions.ipynb.
Converted 05_guess_the_number.ipynb.
Converted index.ipynb.

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)
$ nbdev_build_docs
converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\00_core.ipynb
converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\04_functions.ipynb
An error occurred while executing the following cell:
------------------
from nbdev.showdoc import show_doc
from tcai_AtBSwPython.functions import *
------------------

←[1;31m---------------------------------------------------------------------------←[0m
←[1;31mZeroDivisionError←[0m                         Traceback (most recent call last)
←[1;32m<ipython-input-1-d61a94cea746>←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      1←[0m ←[1;32mfrom←[0m ←[0mnbdev←[0m←[1;33m.←[0m←[0mshowdoc←[0m ←[1;32mimport←[0m ←[0mshow_doc←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 2←[1;33m ←[1;32mfrom←[0m ←[0mtcai_AtBSwPython←[0m←[1;33m.←[0m←[0mfunctions←[0m ←[1;32mimport←[0m ←[1;33m*←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;32m~\Documents\Python\tcai_AtBSwPython\tcai_AtBSwPython\functions.py←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      4←[0m ←[1;33m←[0m←[0m
←[0;32m      5←[0m ←[1;31m# Cell←[0m←[1;33m←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 6←[1;33m ←[1;36m5←[0m←[1;33m/←[0m←[1;36m0←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;31mZeroDivisionError←[0m: division by zero
ZeroDivisionError: division by zero

converting: C:\Users\tcailleau\Documents\Python\tcai_AtBSwPython\05_guess_the_number.ipynb
An error occurred while executing the following cell:
------------------
from nbdev.showdoc import show_doc
from tcai_AtBSwPython.guess_the_number import *
------------------

←[1;31m---------------------------------------------------------------------------←[0m
←[1;31mStdinNotImplementedError←[0m                  Traceback (most recent call last)
←[1;32m<ipython-input-1-19e069bf1df9>←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      1←[0m ←[1;32mfrom←[0m ←[0mnbdev←[0m←[1;33m.←[0m←[0mshowdoc←[0m ←[1;32mimport←[0m ←[0mshow_doc←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 2←[1;33m ←[1;32mfrom←[0m ←[0mtcai_AtBSwPython←[0m←[1;33m.←[0m←[0mguess_the_number←[0m ←[1;32mimport←[0m ←[1;33m*←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m
←[1;32m~\Documents\Python\tcai_AtBSwPython\tcai_AtBSwPython\guess_the_number.py←[0m in ←[0;36m<module>←[1;34m←[0m
←[0;32m      7←[0m ←[1;32mimport←[0m ←[0mrandom←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0;32m      8←[0m ←[0mprint←[0m←[1;33m(←[0m←[1;34m'Hello. What is your name?'←[0m←[1;33m)←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m----> 9←[1;33m ←[0mname←[0m ←[1;33m=←[0m ←[0minput←[0m←[1;33m(←[0m←[1;33m)←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0m←[0;32m     10←[0m ←[0msecretNumber←[0m ←[1;33m=←[0m ←[0mrandom←[0m←[1;33m.←[0m←[0mrandint←[0m←[1;33m(←[0m←[1;36m1←[0m←[1;33m,←[0m ←[1;36m20←[0m←[1;33m)←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0;32m     11←[0m ←[0mprint←[0m←[1;33m(←[0m←[1;34m'Well, '←[0m ←[1;33m+←[0m ←[0mname←[0m ←[1;33m+←[0m ←[1;34m'I am thinking of a number between 1 and 20.'←[0m←[1;33m)←[0m←[1;33m←[0m←[1;33m←[0m←[0m

←[1;32m~\AppData\Roaming\Python\Python39\site-packages\ipykernel\kernelbase.py←[0m in ←[0;36mraw_input←[1;34m(self, prompt)←[0m
←[0;32m    843←[0m         """
←[0;32m    844←[0m         ←[1;32mif←[0m ←[1;32mnot←[0m ←[0mself←[0m←[1;33m.←[0m←[0m_allow_stdin←[0m←[1;33m:←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[1;32m--> 845←[1;33m             raise StdinNotImplementedError(
←[0m←[0;32m    846←[0m                 ←[1;34m"raw_input was called, but this frontend does not support input requests."←[0m←[1;33m←[0m←[1;33m←[0m←[0m
←[0;32m    847←[0m             )

←[1;31mStdinNotImplementedError←[0m: raw_input was called, but this frontend does not support input requests.
StdinNotImplementedError: raw_input was called, but this frontend does not support input requests.

Conversion failed on the following:
04_functions.ipynb
05_guess_the_number.ipynb
Traceback (most recent call last):
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\tcailleau\AppData\Local\Programs\Python\Python39\Scripts\nbdev_build_docs.exe\__main__.py", line 7, in <module>
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\fastcore\script.py", line 105, in _f
    tfunc(**merge(args, args_from_prog(func, xtra)))
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 665, in nbdev_build_docs
    if fname is None: make_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 730, in make_sidebar
    create_default_sidebar()
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 722, in create_default_sidebar
    dic = {Config().lib_name: _create_default_sidebar()}
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in _create_default_sidebar
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 714, in <listcomp>
    titles = [_get_title(f) for f in fnames if f.stem!='index']
  File "c:\users\tcailleau\appdata\local\programs\python\python39\lib\site-packages\nbdev\export2html.py", line 704, in _get_title
    with open(fname, 'r') as f: code = f.read()
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\tcailleau\\Documents\\Python\\tcai_AtBSwPython\\docs\\functions.html'

tcailleau@TCAILLEAU-02 MINGW64 ~/Documents/Python/tcai_AtBSwPython (master)


**Searching for:** *"raw_input was called, but this frontend does not support input requests."* and found: https://github.com/ipython/ipython/issues/11361