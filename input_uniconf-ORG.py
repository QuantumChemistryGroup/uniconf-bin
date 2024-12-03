#!/usr/bin/python
import sys, string, os, glob
from math import *

# a few special functions
def IsFloat(s):
        try: 
                float(s)
                return True
        except ValueError:
                return False

def IsInt(s):
        try: 
                int(s)
                return True
        except ValueError:
                return False

# script to prepare the input file for the uniconf conformer generator

# reading the file with the charges

mol=[]
try:
	f = open(sys.argv[1], "r")
except Exception as e:
	print ("The error occured is: ", e)
	sys.exit(0)

for line in f:
	d = str.split(line)
	if len(d) == 5 and IsFloat(d[1]) == True and IsFloat(d[2]) == True and IsFloat(d[3]) == True and IsFloat(d[4]) == True:
		mol.append((d[0], d[1], d[2], d[3], d[4]))
f.close()

# parameters 
bonds = []

if os.path.isfile(sys.argv[1][0:-4]+'.ROT') == True:
	print ('bonds are here')
	f = open(sys.argv[1][0:-4]+'.ROT', 'r')
	for line in f:
		d = str.split(line)
		if len(d) == 5 and IsInt(d[0]) == True and IsInt(d[1]) == True and IsInt(d[2]) == True and IsInt(d[3]) == True and IsInt(d[4]) == True:
			for i in range(len(d)):
				d[i] = int(d[i])
			bonds.append(d)	
	f.close()	

# writing the uniconf input

f = open(sys.argv[1][0:-4]+'-uni.inp', 'w')
f.write('$BOND\n')
for i in range(len(bonds)):
	f.write('%5i %5i %5i %5i %5i\n' % (bonds[i][0], bonds[i][1], bonds[i][2], bonds[i][3], bonds[i][4]) )
f.write('$END\n')
f.write('$ALGO\n')
f.write('''ALGO=CONF CONNECT=WRITE DIST=1.5 
STRATEGY=1 CLUSTERPROPERTY=IXX
MK=150000 ITER1=3000 KMEANS=5000  MAXCONF=150000 
ITER2=33000 KMEANS1=30 MAXCONFPRINT=55000 
''')
f.write('$END\n')
f.write('$MOLECULE\n')
for i in range(len(mol)):
	f.write('%3s %12s %12s %12s\n' % (mol[i][0], mol[i][1], mol[i][2], mol[i][3]))
f.write('$END\n')
f.write('$CHARGE\n')
for i in range(len(mol)):
	f.write('%12s \n' % mol[i][4])
f.write('$END\n')
f.close()
