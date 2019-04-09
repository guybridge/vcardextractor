#!/usr/bin/python3
# Author: Guy Bridge
# Description: multi vCard to single vCard converter

import sys

# the multi vCard file
CONTACTS_FILE = "contacts.vcf"

VCARD_ENTRY_START = "BEGIN:VCARD"
VCARD_ENTRY_END = "END:VCARD"
VCARD_NUM = 1

# open the file
try:
	fh = open(CONTACTS_FILE, "r")
except FileNotFoundError:
	print("\nUnable to find VCF file to open, please specify in variable\n")
	sys.exit(1)
	

fh_open = False

# create a file handle to store the single vCard
vcard = open("vCard-" + str(VCARD_NUM) + ".vcf", "w")

# Loop through the file
for line in fh:

	# Check if we are at the start
	if VCARD_ENTRY_START in line or fh_open == True:
		fh_open = True
		print("Found the start of a vCard!")
		vcard.write(line)
		
	if VCARD_ENTRY_END in line:
		print("Found the end of a vCard!");
		fh_open = False
		#Close the handle
		vcard.close();
		# increment to the next
		VCARD_NUM += 1
		# open a new handle
		vcard = open("vcards/" + "vCard" + str(VCARD_NUM) + ".vcf", "w")
	
fh.close()



