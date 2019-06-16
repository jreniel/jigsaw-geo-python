#!/usr/bin/env python

import jigsawpy

from tests.case_1_ import case_1_
from tests.case_2_ import case_2_
from tests.case_3_ import case_3_
from tests.case_4_ import case_4_
from tests.case_5_ import case_5_

import argparse

def example(IDnumber=1,savefigs=False):

#--------------- don't disp. to screen, write to png backend

    if savefigs: plt.switch_backend("Agg")

#--------------- delegate to the individual example cases...
    
    if   (IDnumber == +1):
        case_1_(savefigs)

    elif (IDnumber == +2):
        case_2_(savefigs)

    elif (IDnumber == +3):
        case_3_(savefigs)

    elif (IDnumber == +4):
        case_4_(savefigs)

    elif (IDnumber == +5):
        case_5_(savefigs)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("--IDnumber", dest="IDnumber", action="store_true",
                        help="Run EXAMPLE(IDNUMBER).")

    parser.add_argument("--savefigs", dest="savefigs", action="store_true",
                        help="Set this flag to save figures to file rather" 
                             "than loading graphics.")
    
    args = parser.parse_args()

    example(IDnumber = args.IDnumber,
            savefigs = args.savefigs)



