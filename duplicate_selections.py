import sublime
import sublime_plugin


class DuplicateSelectionsCommand(sublime_plugin.TextCommand):
    def duplicate_regions(self, edit, empty_region, notempty_region):
        notempty_content = self.view.substr(notempty_region)
        self.view.replace(edit, empty_region, notempty_content)

    def run(self, edit, **kwargs):
        empties = []
        notempties = []
        for region in self.view.sel():
            if region:
                notempties.append(region)
            else:
                empties.append(region)

        if not notempties:
            if not empties:
                return  # no cursors at all!?  weirdo.

            # gather all the lines
            lines = []
            for cursor in empties:
                line_region = self.view.full_line(cursor)
                line = self.view.substr(line_region)
                lines.append(line)

            # insert them
            self.view.sel().clear()
            lines.reverse()
            empties.reverse()
            last_row, _ = self.view.rowcol(len(self.view))
            for region_i, cursor in enumerate(empties):
                row, col = self.view.rowcol(cursor.a)
                line = lines[region_i]

                if row == last_row:
                    # if we're on the last line, things are hairy; we need to
                    # insert an extra newline somewhere, and account for that by
                    # moving col around.
                    if col == 0:
                        insert_point = cursor.a
                        line = line + "\n"
                    else:
                        insert_point = self.view.full_line(cursor).end()
                        col += 1
                        line = "\n" + line
                elif col == 0:
                    insert_point = cursor.a
                else:
                    insert_point = self.view.full_line(cursor).end()
                self.view.insert(edit, insert_point, line)
                insert_point += col
                self.view.sel().add(sublime.Region(insert_point, insert_point))
            return

        if not empties:
            sublime.status_message("No empty regions")
            return

        if len(notempties) > 1 and len(empties) != len(notempties):
            sublime.status_message("Number of empty regions (%i) does note equal number of non-empty regions (%i)" % (len(empties), len(notempties)))
            return

        for region_i, empty_region in enumerate(empties):
            if len(notempties) == 1:
                notempty_region = notempties[0]
            else:
                notempty_region = notempties[region_i]

            # adjust regions to the right of empty_region
            for fix_i, fix_region in enumerate(notempties):
                if fix_region.begin() >= empty_region.end():
                    notempties[fix_i] = sublime.Region(fix_region.a + len(notempty_region), fix_region.b + len(notempty_region))
            for fix_i, fix_region in enumerate(empties):
                if fix_region.begin() >= empty_region.end():
                    empties[fix_i] = sublime.Region(fix_region.a + len(notempty_region), fix_region.b + len(notempty_region))

            self.duplicate_regions(edit, empty_region, notempty_region)
        self.view.sel().clear()
        for region in empties:
            self.view.sel().add(region)
        self.view.show_at_center(empties[0])
