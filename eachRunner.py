import subprocess
import time
import sys

def makeRunner(series):
	if series:
		return lambda x: subprocess.call(x)
	else:
		return lambda x: subprocess.Popen(x)


def replaceWithVar(var, subst, cmd):
	newcmd = cmd[:]

	indices = [i for (i,x) in enumerate(cmd) if x == var]
	for i in indices:
		newcmd[i] = subst

	return newcmd


def runEach(parsedTuple):
	verbose, series, var, files, cmd = parsedTuple
	run = makeRunner(series)

	if verbose:
		s = " parallel."
		if series:
			s = " series."
		print "[EACH] running ", len(files), "commands in" + s


	# store those processes
	ps = []
	for f in files:
		fcmd = replaceWithVar(var, f, cmd)

		if verbose:
			print "[EACH] Running command:", " ".join(fcmd)

		p = run(fcmd)
		ps.append(p)



	if verbose:
		"[EACH] Successfully started ", len(files), "commands."

	# now leave
	if series:
		status = sum(ps)
		if verbose:
			print "[EACH] Exiting with status", status
		sys.exit(status)
	else:
		waitToFinish(ps)


def waitToFinish(ps):
	# if all of them have completed, stop running
	while True:
		time.sleep(0.1)
		for p in ps:
			p.poll()
			
		if not any([p.returncode == None for p in ps]):
			sys.exit(0)