import sys
from eachParser import parse
from eachRunner import runEach

if __name__ == "__main__":
	args = sys.argv[1:]

	if len(args) <= 0:
		print "each: an iterator for files"
		print "Peter Swire - swirepe.com"
		print "    "
		print "General syntax:"
		print "   each <name> in <list>\tassign, one by one, the values in <list> to <name>"
		print "   ::\tThe command to run with in iteration.  It is run in series."
		print "   ++\tThe command to run with in iteration.  It is run in parallel."
		print "     \tOnly one of :: or ++ is used by this program."  
		print "     \tAny after the first are assumed to be arguments for an external command"
		print "      "
		print "Example usage:"
		print "   With an implied variable $"
		print "      each *.zip :: unzip $"
		print "    "
		print "   With a named variable"
		print "       each picture in *.jpg :: do_something picture"
		print "    "
		print "   With more than one type of file"
		print "       each picture in *.jpg *.png :: do_something picture"
		print "   "
		print "   With things run in parallel instead of series"
		print "       each picture in *.jpg *.png ++ do_something picture"
		sys.exit(0)


	parsedTuple = parse(args)
	runEach(parsedTuple)