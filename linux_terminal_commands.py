import os
import sys
import shutil



def get_full_paths(paths):
	if isinstance(paths, list):
		return [get_full_path(path) for path in paths]
	elif isinstance(paths, str):
		return get_full_path(paths)
def get_full_path(path):
	return path if os.path.isdir(path) \
		else os.path.join(os.getcwd(), path)

if __name__ == '__main__':

	args = sys.argv[1:]

	if args[0] == 'rm':

		# delete director recursively
		if args[1] == '-rf':
			# recursively remove directory
			# source: https://stackoverflow.com/questions/13118029/deleting-folders-in-python-recursively
			dirpaths = get_full_paths(args[2:])
			for dirpath in dirpaths:
				if os.path.isdir(dirpath):
					shutil.rmtree(dirpath)

		# delete file(s)
		else:
			filepaths = get_full_paths(args[1:])
			for filepath in filepaths:
				if os.path.isfile(filepath):
					os.remove(filepath)
				else:
					print('%s is a directory' % filepath)

	elif args[0] == 'touch':
		# create empty files if they don't exist
		# TODO handle filepath being given instead of using cwd
		filepaths = get_full_paths(args[1:])
		for filepath in filepaths:
			if not os.path.exists(filepath):
				open(filepath, 'w').close()

	elif args[0] == 'mv':
		if len(args) == 3:
			filepath1 = get_full_path(args[1])
			filepath2 = get_full_path(args[2])
			# shutil.move() works for both files and directories
			# source: https://stackoverflow.com/questions/8858008/how-to-move-a-file
			shutil.move(filepath1, filepath2)
		else:
			print('invalid syntax. syntax must be: mv <src_dir> <dst_dir>')
