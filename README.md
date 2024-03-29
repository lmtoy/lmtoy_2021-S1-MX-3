# 2021-S1-MX-3

This project observed a series of EDGE galaxies looking for CO(1-0).

## OBSNUM

A total of 8 objects (so far)

More detailed descriptions are in the file **mk_runs.py**.

### Summary

As of June 16 2022 we have 130 obsnums in 8 galaxies. About 20 hours skytime was used.
RMS and peak are provisional pending QA on the pipeline.

     Galaxy           #obsnum  EXP RMS     Peak     map
                               mK  mK     K.km/s   size
     Arp91   NC5953/4    9/10  33  44  38 14     171 x 153  clear detection in both; (GBT and CARMA too)
     Arp143  NGC2444/5  12/12  29  36  32  4     180 x 215  clear detection (in main galaxy ; companion not) 
     NGC6786            10/10  32  38  32  5     180 x 200  both main and companion detected
     NGC5376            24/26  20  26  34  2.5   100 x 100  clear resolved detection, rot gal
     NGC5720            14/14  27  24  33  0.2   100 x 100  two peaks detected (DV~300 km/s  DR~40" PA~45) 7600-7950
     NGC2540             4/ 4  50  44  70  ?     100 x 100  weak in smooth cube  6160-6410
     NGC5473            31/32  18  23  29  ?     100 x 100  no detection
     NGC6173            15/22  26  30  41  ?     100 x 100  no detection

Each single RA-scan or DEC-scan map gives around 100mK noise if all beams work, exactly as the calculator predicts.
The "EXP" column is what the radiometer eq. would predict. Notable NGC2540 and NGC5720 perform a little better,
but QA is needed to verify.


## LMTOY Data Reduction

There are two ways to run the SLpipeline, using a different $WORK_LMT directory where the root
of the data processing occurs

1. Use the WORK_LMT that came with where **lmtoy** was installed. This will likely require
   write permission from the owner

   This is the way it runs on Unity.

2. Set WORK_LMT to a directory here in this directory,  something like

              WORK_LMT=`pwd`

   and no permissions in the $LMTOY tree are. Of course you still need to have LMTOY
   installed. The pipeline will then create all  data products in this local directory.

### Creating the run files

A master script **mk_runs** contains all the information on which obsnums are good,
which beams are good, etc.  You always will need to re-run this script to create the
SLpipeline *run* files. The script also uses the (optional) **OBSNUM.args** files, where
arguments specific to this obsnum can be stored. These files should be edited by
a user to create a new "final" dataset. Any optional post-processing after the
pipeline will not be described here (but is of course recommended?).

This command creates the run files (it uses the **mk_runs** scripts):

      make runs
	  
in this case just **2021-S1-MX-3.run1** and **2021-S1-MX-3.run2**


## Science:

### NGC6786

The neighbor LEDA 62867 was also detected, seemingly with about 1/10th of flux of NGC6786.
VLSR was seen around 7550, but catalog claims 7406. Thus we need to set the
baseline window (dv,dw) a bit odd. E.g. dv=350 dw=300 or a manual channel number,
or a fake restfreq?   Fixing the window changed the flux ratio to 1:4 !

NGC6786 is resolved, the kinematic PA is around 200-210. NED reports PA 20-40, INC 34-42.
Has a bar, and is CCW.  The bar is appears along the major axis.
LEDA 62867 might be more like 270, but not well resolved.


### Arp91, aka NC5953/4

We have CARMA and GBT data for this.

### Arp143, aka NGC 2444/5

Big HI tail (15 arcmin) to the north.
CO only in N2444 it seems.   Not in GBT sample

