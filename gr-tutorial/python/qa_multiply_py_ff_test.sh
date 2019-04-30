#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/kasutaja/gr-tutorial/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/kasutaja/gr-tutorial/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/kasutaja/gr-tutorial/swig:$PYTHONPATH
/usr/bin/python2 /home/kasutaja/gr-tutorial/python/qa_multiply_py_ff.py 
