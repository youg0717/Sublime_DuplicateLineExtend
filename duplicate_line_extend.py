import sublime, sublime_plugin

class DuplicateLineExtendCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            line_contents = self.view.substr(line) + '\n'
            self.view.insert(edit, line.begin(), line_contents)
