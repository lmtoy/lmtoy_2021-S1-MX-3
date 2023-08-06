#! /usr/bin/env python
#
#   script generator for project="2021-S1-MX-3"
#

import os
import sys

from lmtoy import runs

project="2021-S1-MX-3"

#        obsnums per source (make it negative for not adding to the final combinations)
on = {}
on['Arp91']   = [97559, 97560, 97562, 97563,-97905, 97906, 97907, 97908, 97912, 97913]
on['Arp143']  = [97955, 97956, 97960, 97961, 97965, 97966, 99440, 99441, 99477, 99478, 99480, 99481]
on['NGC6786'] = [98082, 98083, 98138, 98139, 98768, 98769, 98773, 98774, 98778, 98779]
on['NGC5376'] = [99286, 99288, 99290, 99291, 99295, 99296, 99300, 99301, 99303, 99304, 99306, 99307,
                 99319, 99320, 99322, 99323, 99341, 99342, 99492, 99493, 99495, 99496,-99498,-99499, 99537, 99538]

on['NGC5720'] = [99546, 99547, 99549, 99550, 99552, 99553, 99727, 99728, 99754, 99755, 99757, 99758,     # 17-may
                 100603, 100604]                                                                         # 1-jun
on['NGC2540'] = [99662, 99663, 99667, 99668]                                                             # 17-may
on['NGC5473'] = [100216, 100217, 100219, 100220, 100222, 100223, 100225, 100226,                    # 24-may
                 100606, 100607,                                                                    # 1-jun
                 100678, 100679, 100683, 100684, 100688, 100689, 100718,-100719, 100723, 100724,    # 7-jun
                 100821, 100822, 100826, 100827, 100831, 100832, 100857, 100858, 100862, 100863,    # 8-jun
                 100867, 100868]

on['NGC6173'] = [ 100979, 100980, 100982, 100983, 100985, 100986, 100988,-100989,-100993,-100994,-100996,
                 -100997, 100999, 101000, 101002, 101003, 101007, 101008, 101010, 101011,-101013,-101014]   # 15-jun


#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['Arp91']   = "dv=250 dw=400 extent=240 edge=1"
pars1['Arp143']  = "dv=250 dw=450 extent=240"         # has small birdie
pars1['NGC6786'] = "dv=350 dw=300 extent=240"         # vlsr is off, need bigger dv
pars1['NGC5376'] = "dv=250 dw=400 extent=240"
pars1['NGC5720'] = "dv=300 dw=350 extent=240"
pars1['NGC2540'] = "dv=300 dw=350 extent=240"
pars1['NGC5473'] = "dv=300 dw=350 extent=240"
pars1['NGC6173'] = "dv=300 dw=350 extent=240"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['Arp91']   = "pix_list=-0,5"
pars2['Arp143']  = "pix_list=-0,5"
pars2['NGC6786'] = "pix_list=-0"
pars2['NGC5376'] = "pix_list=-0,5,14,15"
pars2['NGC5720'] = "pix_list=-0,5"
pars2['NGC2540'] = "pix_list=-0,5"
pars2['NGC5473'] = "pix_list=-0,5"
pars2['NGC6173'] = "pix_list=-0,5"



runs.mk_runs(project, on, pars1, pars2, sys.argv)

