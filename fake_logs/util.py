import os
import glob
import sys
import getopt
from weighted_choice import WeightedChoice


def append_line_number_to_file(path_name):
	def write_to_file(file_name):
		lines = []
		with open(file_name, "r", encoding='utf-8') as f:
			for i, line in enumerate(f):
				lines.append(line[:-1] + " " + str(i + 1) + "\n")
		with open(file_name, "w", encoding='utf-8') as f:
			for line in lines:
				f.write(line)

	if os.path.isfile(path_name):
		write_to_file(path_name)
	else:
		files = glob.glob(path_name + '/**/*.txt', recursive=True)
		for file in files:
			if os.path.isfile(file):
				write_to_file(file)


def append_debug_level_to_file(path_name):
	"""
	Add debug level and Tag to the front of each line
	"""
	def write_to_file(file_name):
		lines = []
		base_name = os.path.basename(file_name)
		with open(file_name, "r", encoding='utf-8') as f:
			for i, line in enumerate(f):
				debug_level = WeightedChoice(["V", "D", "I", "W", "E", "F"], [0.5, 0.35, 0.06, 0.04, 0.02, 0.03])
				lines.append(f'{debug_level.run()} {base_name}: {line}')
		with open(file_name, "w", encoding='utf-8') as f:
			for line in lines:
				f.write(line)

	if os.path.isfile(path_name):
		write_to_file(path_name)
	else:
		files = glob.glob(path_name + '/**/*.txt', recursive=True)
		for file in files:
			if os.path.isfile(file):
				write_to_file(file)


def main(argv):
	in_folder = ''
	out_folder = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["in_folder=", "out_folder="])
	except getopt.GetoptError:
		print('test.py -i <in_folder>')
		print('Not supported: test.py -i <in_folder> -o <out_folder>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <in_folder>')
			print('Not supported: test.py -i <in_folder> -o <out_folder>')
			sys.exit()
		elif opt in ("-i", "--in_folder"):
			in_folder = arg
		elif opt in ("-o", "--out_folder"):
			print('Not supported yet for out_folder')
			out_folder = arg

	append_line_number_to_file(in_folder)
	append_debug_level_to_file(in_folder)


if __name__ == "__main__":
	main(sys.argv[1:])

