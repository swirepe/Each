# Each

A small tool for iterating over files.

Peter Swire, swirepe.com

## What does it do?

It allows you to specify a name for a file as you iterate through them.  Think of it as a foreach loop.

## What do you use it for?

For those times when you have a command that can't take in a glob.  It can run commands in series or parallel.

    each markdownFile in *.md :: convertToHTML markdownFile
    each experiment in *.settings ++ runBigExperiment experiment


## Why not use what is build into cmd?

For example, %F is the current file.  You can do something like

    for %F in (*.txt) do some_command %F


The `each` command lets you do that in parallel, if you so choose.  If you don't have access to xargs or gnu parallel, perhaps you have access to this?

Update: I just learned about [forfiles.](http://blog.ringerc.id.au/2011/12/windows-command-line-survival-findfiles.html)  That may work for you, too.


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