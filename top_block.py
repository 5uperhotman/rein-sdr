#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 16 13:44:35 2019
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1e06
        self.slider_cutoff = slider_cutoff = samp_rate/8
        self.slider_trans = slider_trans = samp_rate/8
        self.slider_cutoff_high = slider_cutoff_high = slider_cutoff+2e03

        ##################################################
        # Blocks
        ##################################################
        self._slider_cutoff_range = Range(samp_rate/1000, samp_rate/2, 1, samp_rate/8, 200)
        self._slider_cutoff_win = RangeWidget(self._slider_cutoff_range, self.set_slider_cutoff, "slider_cutoff", "counter_slider", float)
        self.top_layout.addWidget(self._slider_cutoff_win)
        self._slider_trans_range = Range(samp_rate/1000, samp_rate/2, 1, samp_rate/8, 200)
        self._slider_trans_win = RangeWidget(self._slider_trans_range, self.set_slider_trans, "slider_trans", "counter_slider", float)
        self.top_layout.addWidget(self._slider_trans_win)
        self._slider_cutoff_high_range = Range(slider_cutoff, samp_rate/2, 1, slider_cutoff+2e03, 200)
        self._slider_cutoff_high_win = RangeWidget(self._slider_cutoff_high_range, self.set_slider_cutoff_high, "slider_cutoff_high", "counter_slider", float)
        self.top_layout.addWidget(self._slider_cutoff_high_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_HAMMING, #wintype
        	0, #fc
        	1e06, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.band_pass_filter_0 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate, slider_cutoff, slider_cutoff_high, slider_trans, firdes.WIN_HAMMING, 6.76))
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_slider_cutoff(self.samp_rate/8)
        self.set_slider_trans(self.samp_rate/8)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.slider_cutoff, self.slider_cutoff_high, self.slider_trans, firdes.WIN_HAMMING, 6.76))

    def get_slider_cutoff(self):
        return self.slider_cutoff

    def set_slider_cutoff(self, slider_cutoff):
        self.slider_cutoff = slider_cutoff
        self.set_slider_cutoff_high(self.slider_cutoff+2e03)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.slider_cutoff, self.slider_cutoff_high, self.slider_trans, firdes.WIN_HAMMING, 6.76))

    def get_slider_trans(self):
        return self.slider_trans

    def set_slider_trans(self, slider_trans):
        self.slider_trans = slider_trans
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.slider_cutoff, self.slider_cutoff_high, self.slider_trans, firdes.WIN_HAMMING, 6.76))

    def get_slider_cutoff_high(self):
        return self.slider_cutoff_high

    def set_slider_cutoff_high(self, slider_cutoff_high):
        self.slider_cutoff_high = slider_cutoff_high
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.slider_cutoff, self.slider_cutoff_high, self.slider_trans, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
