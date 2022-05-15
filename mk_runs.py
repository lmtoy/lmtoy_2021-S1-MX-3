#! /usr/bin/env python
#
#   script generator for project="2021-S1-MX-3"
#
#

import os
import sys

project="2021-S1-MX-3"

#        obsnums per source
on = {}
on['Arp91']   = [97559, 97560, 97562, 97563, 97905, 97906, 97907, 97908, 97912, 97913]
on['Arp143']  = [97955, 97956, 97960, 97961, 97965, 97966, 99440, 99441, 99477, 99478, 99480, 99481]
on['NGC6786'] = [98082, 98083, 98138, 98139, 98768, 98769, 98773, 98774, 98778, 98779]
on['NGC5376'] = [99286, 99288, 99290, 99291, 99295, 99296, 99300, 99301, 99303, 99304, 99306, 99307,
                 99319, 99320, 99322, 99323, 99341, 99342, 99492, 99493, 99495, 99496, 99498, 99499, 99537, 99538]
on['NGC5720'] = [99546, 99547, 99549, 99550, 99552, 99553]

#        common parameters per source on the first dryrun
pars1 = {}
pars1['Arp91']   = "dv=350 dw=300"
pars1['Arp143']  = "dv=350 dw=300"
pars1['NGC6786'] = "dv=350 dw=300"
pars1['NGC5376'] = "dv=350 dw=300"
pars1['NGC5720'] = "dv=350 dw=300"

#        common parameters per source on subsequent runs
pars2 = {}
pars2['Arp91']   = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['Arp143']  = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC6786'] = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC5376'] = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"
pars2['NGC5720'] = "pix_list=1,2,3,4,6,7,8,9,10,11,12,13,14,15"


# below here no need to change code
# ========================================================================

#        helper function for populating obsnum dependant argument
def getargs(obsnum):
    """ search for <obsnum>.args
    """
    f = "%d.args" % obsnum
    if os.path.exists(f):
        lines = open(f).readlines()
        args = ""
        for line in lines:
            if line[0] == '#': continue
            args = args + line.strip() + " "
        return args
    else:
        return ""

#        specific parameters per obsnum will be in files <obsnum>.args
pars3 = {}
for s in on.keys():
    for o in on[s]:
        pars3[o] = getargs(o)


run1  = '%s.run1'  % project
run1a = '%s.run1a' % project
run2  = '%s.run2' % project
run2a = '%s.run2a' % project

fp1 = open(run1,  "w")
fp2 = open(run1a, "w")
fp3 = open(run2,  "w")
fp4 = open(run2a, "w")

n1 = 0
for s in on.keys():
    for o in on[s]:
        cmd1 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 restart=1 " % (o,s,pars1[s])
        cmd2 = "SLpipeline.sh obsnum=%d _s=%s %s admit=0 tap=1 %s" % (o,s,pars2[s], pars3[o])
        fp1.write("%s\n" % cmd1)
        fp2.write("%s\n" % cmd2)
        n1 = n1 + 1

n2 = 0        
for s in on.keys():
    obsnums = ""
    for o in on[s]:
        if obsnums == "":
            obsnums = "%d" % o
        else:
            obsnums = obsnums + ",%d" % o
    print('%s[%d] :' % (s,len(on[s])), obsnums)
    cmd3 = "SLpipeline.sh _s=%s admit=0 restart=1 obsnums=%s" % (s, obsnums)
    cmd4 = "SLpipeline.sh _s=%s admit=1 srdp=1  obsnums=%s" % (s, obsnums)
    fp3.write("%s\n" % cmd3)
    fp4.write("%s\n" % cmd4)
    n2 = n2 + 1

print("A proper re-run of %s should be in the following order:" % project)
print(run1)
print(run2)
print(run1a)
print(run2a)
print("Where there are %d single obsnum runs, and %d combination obsnums" % (n1,n2))
