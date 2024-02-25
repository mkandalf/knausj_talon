import io
import subprocess
from typing import Union
from contextlib import redirect_stdout
from talon import Context, Module, actions, app, speech_system
from talon.grammar import Phrase

mod = Module()

VSCODE_PATH = "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"

@mod.action_class
class Actions:
    def talon_edit_phrase(phrase: Union[str, Phrase]):
        """Edits file for phrase"""
        actions.user.talon_edit_file(speech_system._sim(str(phrase)).split('\n')[1].split(': ')[1].strip())

    def talon_edit_file(file_name: str):
        """Edits file"""
        command = [VSCODE_PATH, file_name]
        subprocess.run(command)

    def talon_edit_file_at(file_name: str, line_number: int):
        """Edits file and line number"""
        command = [VSCODE_PATH, "-g", f"{file_name}:{line_number}"]
        subprocess.run(command)
