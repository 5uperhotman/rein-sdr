#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class diode_py_cc(gr.sync_block):
    """
    docstring for block diode_py_cc
    """
    def __init__(self, threshold):
	self.threshold = threshold
        gr.sync_block.__init__(self,
            name="diode_py_cc",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
	out[:]=in0
        # <+signal processing here+>
#	if in0.real > self.threshold:
#        	out[:] = self.threshold + in0.imag
#	else:
#		out[:] = in0.real + in0.imag
        return in0

