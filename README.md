DuplicateSelections
===================

I wrote and use this plugin as an alternative to copy and pasting.

First, you can use this command to duplicate the current line (or lines).

Another common use case is when you need to copy some small bit of text, like a variable or method name.

Select the text to copy, then `cmd+click` to place an empty cursor, then run this command to insert the selected text at the cursor position.

This can be extended to multiple selections: if you have an equal number of selections and cursors, this command will place each selection at the corresponding cursor location.

Or, you can select some text and place *multiple* empty cursors, and the selection will be inserted at all the cursor locations.

###### Example:
<video src="https://github.com/colinta/SublimeDuplicateSelections/raw/master/example.mp4">[Example.mp4](https://github.com/colinta/SublimeDuplicateSelections/raw/master/example.mp4)</video>

Installation
------------

Using Package Control, install "DuplicateSelections" or clone this repo in your packages folder.

I recommended you add key bindings for the commands. I've included my preferred bindings below.
Copy them to your key bindings file (⌘⇧,).

Commands
--------

`duplicate_selections`: See description above

Key Bindings
------------

Copy these to your user key bindings file.

<!-- keybindings start -->
    { "keys": ["ctrl+d"], "command": "duplicate_selections" },
<!-- keybindings stop -->
