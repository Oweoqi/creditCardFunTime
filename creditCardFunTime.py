#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# Created by Anthony Cozamanis
# twitter.com/Kurobeats

#!/usr/bin/env python

import os, fnmatch, re, sys
from baluhn import generate, verify

rootPath = sys.argv[1]
pattern = '*.*'
visa = re.compile(r'4[0-9]{12}(?:[0-9]{3})?')
mastercard = re.compile(r'5[1-5][0-9]{14}')
amex = re.compile(r'3[47][0-9]{13}')
diners = re.compile(r'3(?:0[0-5]|[68][0-9])[0-9]{11}')
discover = re.compile(r'6(?:011|5[0-9]{2})[0-9]{12}')
jcb = re.compile(r'(?:2131|1800|35[0-9]{3})[0-9]{11}')
 
for root, dirs, files in os.walk(rootPath):
	for filename in fnmatch.filter(files, pattern):
		cardNumbers = open((os.path.join(root, filename)), "r", errors='ignore', encoding='utf-8')
		for line in cardNumbers:
			line = line.rstrip()
			
			cardSearch = visa.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("Visa "+theCard)
			
			cardSearch = mastercard.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("Mastercard "+theCard)
				
			cardSearch = amex.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("American Express "+theCard)
				
			cardSearch = diners.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("Diners Club "+theCard)
				
			cardSearch = discover.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("Discover "+theCard)
			
			cardSearch = jcb.findall(line)
			for theCard in cardSearch:
				if verify(theCard):
					print("\n"+os.path.join(root, filename))
					print("JCB "+theCard)
