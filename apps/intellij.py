from talon import Context, actions, ui, Module, app, clip
from typing import List, Union

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()
mod.apps.intellij = "app.name: IntelliJ IDEA"

ctx.matches = r"""
app: intellij
"""


@ctx.action_class("win")
class win_actions:
    def filename():
        title = actions.win.title()
        # this doesn't seem to be necessary on VSCode for Mac
        # if title == "":
        #    title = ui.active_window().doc

        if is_mac:
            result = title.split(" - ")[1].split(" ")[0]
        else:
            result = title.split(" - ")[0]

        if "." in result:
            return result

        return ""

    def file_ext():
        return actions.win.filename().split(".")[-1]
