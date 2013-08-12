DuplicateSelections
===================

If you have an equal number of empty selections (cursors) and selections, this
command will place each selection at the corresponding cursor location.

Installation
------------

1. Using Package Control, install "DuplicateSelections"

Or:

1. Open the Sublime Text Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
    - Windows: %APPDATA%/Sublime Text 3/Packages/
    - Linux: ~/.Sublime Text 3/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

### Sublime Text 2

1. Open the Sublime Text 2 Packages folder
2. clone this repo, but use the `st2` branch

       git clone -b st2 git@github.com:colinta/SublimeDuplicateSelections

Commands
--------

`duplicate_selections`: For each empty cursor, copies a non-empty region into that cursor.