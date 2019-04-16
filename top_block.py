#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 16 13:26:01 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tap4 = tap4 = 1
        self.tap3 = tap3 = 1
        self.tap2 = tap2 = 1
        self.tap1 = tap1 = 1
        self.tap0 = tap0 = 1
        self.samp_rate = samp_rate = 1e06

        ##################################################
        # Blocks
        ##################################################
        _tap4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap4_sizer,
        	value=self.tap4,
        	callback=self.set_tap4,
        	label='tap4',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap4_sizer,
        	value=self.tap4,
        	callback=self.set_tap4,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap4_sizer)
        _tap3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap3_sizer,
        	value=self.tap3,
        	callback=self.set_tap3,
        	label='tap3',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap3_sizer,
        	value=self.tap3,
        	callback=self.set_tap3,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap3_sizer)
        _tap2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap2_sizer,
        	value=self.tap2,
        	callback=self.set_tap2,
        	label='tap2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap2_sizer,
        	value=self.tap2,
        	callback=self.set_tap2,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap2_sizer)
        _tap1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap1_sizer,
        	value=self.tap1,
        	callback=self.set_tap1,
        	label='tap1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap1_sizer,
        	value=self.tap1,
        	callback=self.set_tap1,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap1_sizer)
        _tap0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tap0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tap0_sizer,
        	value=self.tap0,
        	callback=self.set_tap0,
        	label='tap0',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tap0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tap0_sizer,
        	value=self.tap0,
        	callback=self.set_tap0,
        	minimum=-1,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tap0_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vff((tap3, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((tap1, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((tap4, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((tap2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((tap0, ))
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, 3)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_float*1, 4)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def get_tap4(self):
        return self.tap4

    def set_tap4(self, tap4):
        self.tap4 = tap4
        self._tap4_slider.set_value(self.tap4)
        self._tap4_text_box.set_value(self.tap4)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.tap4, ))

    def get_tap3(self):
        return self.tap3

    def set_tap3(self, tap3):
        self.tap3 = tap3
        self._tap3_slider.set_value(self.tap3)
        self._tap3_text_box.set_value(self.tap3)
        self.blocks_multiply_const_vxx_0_1_0.set_k((self.tap3, ))

    def get_tap2(self):
        return self.tap2

    def set_tap2(self, tap2):
        self.tap2 = tap2
        self._tap2_slider.set_value(self.tap2)
        self._tap2_text_box.set_value(self.tap2)
        self.blocks_multiply_const_vxx_0_0.set_k((self.tap2, ))

    def get_tap1(self):
        return self.tap1

    def set_tap1(self, tap1):
        self.tap1 = tap1
        self._tap1_slider.set_value(self.tap1)
        self._tap1_text_box.set_value(self.tap1)
        self.blocks_multiply_const_vxx_0_1.set_k((self.tap1, ))

    def get_tap0(self):
        return self.tap0

    def set_tap0(self, tap0):
        self.tap0 = tap0
        self._tap0_slider.set_value(self.tap0)
        self._tap0_text_box.set_value(self.tap0)
        self.blocks_multiply_const_vxx_0.set_k((self.tap0, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
