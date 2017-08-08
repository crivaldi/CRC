#!/usr/bin/python
###This program is written in partial fulfillment of HW8 for Bioinformatics Spring 2016 - inst by Sheri Sanders
###This program is written in python to trim adapters from sequences
###To run this program: ./Trimmer2.py
###input file and amount of bases to trim from beginning - allows for multiple file input and custom file output
###Author: Chissa Rivaldi

###IMPORT LIBRARIES####
import sys;

###DEFINE FUNCTIONS###
def load_seq():
	infile = raw_input("Which file would you like to trim?");
	trim = int(raw_input("How much would you like to trim off?"));
	seq_dict = {}
	my_in_file = open(infile, 'r')
	line = my_in_file.readline();
	while line !="":
		name = line			 #saves current line as name
		seq = my_in_file.readline(); 	#defines seq as next line
		seq_dict[name] = seq[trim:];	#line that saves seq[int(trim)] in seq_dict[name]
		line = my_in_file.readline();
	my_in_file.close();
	return(seq_dict);

def print_seq(fasta_dict):
	output = raw_input("What would you like to save the output as?")
	my_out_file = open(output, 'w')
	for name in fasta_dict:
		my_out_file.write(name + fasta_dict[name]); #writes name and seq to outfile
	my_out_file.close();



###MAIN###
print "Welcome to Trimmer!"


my_seq = load_seq();   ##load first file

more = raw_input("Would you like to load more (Y/N?)");
while more == "Y":
	more_seq = load_seq();
	my_seq.update(more_seq);  #.update to stick dictionaries together
	more = raw_input("Would you like to load more (Y/N)?");
if more != "N" and more != "Y":
	print "You did not enter Y or N - defaulting to N."


print_seq(my_seq);

