# Each

A small tool for iterating over files.

Peter Swire, swirepe.com

## What does it do?

It allows you to specify a name for a file as you iterate through them.  Think of it as a foreach loop.

## What do you use it for?

For those times when you have a command that can't take in a glob.  It can run commands in series or parallel.

    each markdownFile in *.md :: convertToHTML markdownFile
    each experiment in *.settings ++ runBigExperiment experiment


## Help

	 each: an iterator for files
	 Peter Swire - swirepe.com
	     
	 General syntax:
	    each <name> in <list> :: <command>
	        assign, one by one, the values in <list> to <name>
	        The values of <name> are replaced in <command>
	    ::
	        Run in series.
	    ++
	        Run in parallel, each in its own process.
	        Only one of :: or ++ is used by this program.  
	        Any after the first are assumed to be arguments for an external command
	       
	 Example usage:
	    With an implied variable $
	       each *.zip :: unzip $
	     
	    With a named variable
	        each picture in *.jpg :: do_something picture
	     
	    With more than one type of file
	        each picture in *.jpg *.png :: do_something picture
	    
	    With things run in parallel instead of series
	        each picture in *.jpg *.png ++ do_something picture