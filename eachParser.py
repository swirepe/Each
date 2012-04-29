from glob import glob

def parse(args):
	if not ("::" in args or "++" in args):
		raise ValueError("Expectd :: or ++")

	verbose = False
	if args[0] in ["-v", "--verbose"] :
		verbose = True
		args = args[1:]

	series = args[getOpIndex(args)] == "::"

	var = "$"
	if "in" in args:
		var = args[0]
	
	files = getFiles(args)

	cmd = getCmd(args)

	return verbose, series, var, files, cmd


def getOpIndex(args):
	# if they are both in there, pick the first
	if "::" in args:
		if "++" in args:
			return min([args.index("::"), args.index("++")])

		return args.index("::")

	return args.index("++")


def getFiles(args):
	if "in" in args:
		in_index = args.index("in")
	else:
		in_index = 0


	op_index = getOpIndex(args)

	flist = []
	for f in args[in_index+1:op_index]:
		flist.extend(glob(f))

	return flist

def getCmd(args):
	op_index = getOpIndex(args)
	return args[op_index+1:]

