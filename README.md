DuplicateSelections for Sublime Text 2
======================================

If you have an equal number of empty selections (cursors) and selections, this
command will place each selection at the corresponding cursor location.

Installation
------------

### Sublime Text 2

1. Using Package Control, install "DuplicateSelections"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

### Sublime Text 3

1. Open the Sublime Text 2 Packages folder
2. clone this repo, but use the `st3` branch

       git clone -b st3 git@github.com:colinta/SublimeDuplicateSelections

Commands
--------

`duplicate_selections`: For each empty cursor, copies a non-empty region into that cursor.