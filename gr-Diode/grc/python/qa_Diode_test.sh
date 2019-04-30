#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/kasutaja/rein-sdr/gr-Diode/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/kasutaja/rein-sdr/gr-Diode/grc/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/kasutaja/rein-sdr/gr-Diode/grc/swig:$PYTHONPATH
/usr/bin/python2 /home/kasutaja/rein-sdr/gr-Diode/python/qa_Diode.py 
