import os
import sys
import shutil



def get_full_paths(paths):
	if isinstance(paths, list):
		return [get_full_path(path) for path in paths]
	elif isinstance(paths, str):
		return get_full_path(paths)
def get_full_path(path):
	return path if os.path.exists(path) \
		else os.path.join(os.getcwd(), path)



# code i found online to print a file tree 
# source: https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
from pathlib import Path
from itertools import islice
space  = '    '
branch = '│   '
tee    = '├── '
last   = '└── '
def tree(
	dir_path: Path,
	level: int=-1,
	limit_to_directories: bool=False,
	length_limit: int=1000):
	"""Given a directory Path object print a visual tree structure"""
	dir_path = Path(dir_path) # accept string coerceable to Path
	files = 0
	directories = 0
	def inner(dir_path: Path, prefix: str='', level=-1):
		nonlocal files, directories
		if not level: 
			return # 0, stop iterating
		if limit_to_directories:
			contents = [d for d in dir_path.iterdir() if d.is_dir()]
		else: 
			contents = list(dir_path.iterdir())
		pointers = [tee] * (len(contents) - 1) + [last]
		for pointer, path in zip(pointers, contents):
			if path.is_dir():
				yield prefix + pointer + path.name
				directories += 1
				extension = branch if pointer == tee else space 
				yield from inner(path, prefix=prefix+extension, level=level-1)
			elif not limit_to_directories:
				yield prefix + pointer + path.name
				files += 1
	print(dir_path.name)
	iterator = inner(dir_path, level=level)
	for line in islice(iterator, length_limit):
		print(line)
	if next(iterator, None):
		print(f'... length_limit, {length_limit}, reached, counted:')
	print(f'\n{directories} directories' + (f', {files} files' if files else ''))


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

	elif args[0] == 'mv':
		if len(args) == 3:
			filepath1 = get_full_path(args[1])
			filepath2 = get_full_path(args[2])
			# shutil.move() works for both files and directories
			# source: https://stackoverflow.com/questions/8858008/how-to-move-a-file
			shutil.move(filepath1, filepath2)
		else:
			print('invalid syntax. syntax must be: mv <src_dir> <dst_dir>')

	elif args[0] == 'touch':
		# create empty files if they don't exist
		# TODO handle filepath being given instead of using cwd
		filepaths = get_full_paths(args[1:])
		for filepath in filepaths:
			if not os.path.exists(filepath):
				open(filepath, 'w').close()

	elif args[0] == '_tree':

		args = args[1:]
		if len(args) == 0:
			dirpath = os.getcwd()
			tree(dirpath, limit_to_directories=False)
		elif len(args) == 1:
			dirpath = get_full_path(args[0])
			tree(dirpath, limit_to_directories=False)
		elif len(args) == 2:
			dirpath = os.getcwd()
			try:
				if args[0] != '-L':
					raise Exception()
				max_levels = int(args[1])
			except:
				print('Invalid arguments for tree')
				print('valid arguments: tree -L <max_level> <path>')
				print('    <max_level> - int    - optional, default value is infinit')
				print('    <path>      - string - optional, defaults to current directory')
				sys.exit()
			tree(dirpath, level=max_levels, limit_to_directories=False)
		elif len(args) == 3:
			dirpath = get_full_path(args[2])
			try:
				if args[0] != '-L':
					raise Exception()
				max_levels = int(args[1])
			except:
				print('Invalid arguments for tree')
				print('valid arguments: tree -L <max_level> <path>')
				print('    <max_level> - int    - optional, default value is infinit')
				print('    <path>      - string - optional, defaults to current directory')
				sys.exit()
			tree(dirpath, level=max_levels, limit_to_directories=False)
		# TODO: implement limit_to_directories=True
