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
from diode1_py_cc import diode1_py_cc

class qa_diode1_py_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        self.tb.run ()
        # check data
	src_data = (0+2j, 1+5j, -2+3j, 5.5+12j, -0.5+22j)
	expected_result = (0+2j, 0.7+5j, -2+3j, 0.7+12j, -0.5+22j)
#	src_data = (0, 1, -2, 5.5, -0.5)
#	expected_result = (0, 0.7, -2, 0.7, -0.5)
	src = blocks.vector_source_c (src_data)
	mult = diode1_py_cc (0.7)
	snk = blocks.vector_sink_c ()
	self.tb.connect (src, mult)
	self.tb.connect (mult, snk)
	self.tb.run ()
	result_data = snk.data ()
	self.assertComplexTuplesAlmostEqual (src_data, result_data, 4)



if __name__ == '__main__':
    gr_unittest.run(qa_diode1_py_cc, "qa_diode1_py_cc.xml")
