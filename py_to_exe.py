#file: py_to_exe.py
import distutils
import py2exe
distutils.core.setup(windows=["sql2excel.py"])