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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from diode_py_cc import diode_py_cc
import numpy as np

class qa_diode_py_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data
	src_data = ((0.1+12j), (0.3+5j), (1+5j), (0.8+3j))
	#src_data = (0.1)#, 0.3, 1, 0.8)
	expected_result = ((0.1+12j), (0.3+5j), (0.7+5j), (0.7+3j))
	#expected_result = (0.1)#, 0.3, 0.7, 0.7)
	src = blocks.vector_source_c(src_data)
	thre = diode_py_cc(0.7)
	snk = blocks.vector_sink_c()
	self.tb.connect(src, thre)
	self.tb.connect(thre, snk)
	self.tb.run
	result_data = snk.data()
	self.assertComplexTuplesAlmostEqual(expected_result, result_data, 2)



if __name__ == '__main__':
    gr_unittest.run(qa_diode_py_cc, "qa_diode_py_cc.xml")
