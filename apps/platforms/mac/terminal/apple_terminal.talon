app: apple_terminal
-
# makes the commands in generic_terminal available
tag(): terminal

# activates the implementation of the commands/functions in generic_terminal
tag(): user.generic_unix_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application
tag(): user.git
tag(): user.anaconda
tag(): user.kubectl

# TODO: explain
tag(): user.tabs
tag(): user.file_manager
tag(): user.tmux

suspend:
    key(ctrl-z)
resume:
    insert("fg")
    key(enter)

run vim: "vim\n"
run tea mux:
    insert("tmux")
    key(enter)
grep: "grep "
git grep: "git grep "
ls: "ls\n"
clear way left:
    key(ctrl-u)

clear way right:
    key(ctrl-k)

clear word left:
    key(ctrl-w)

clear word right:
    key(ctrl-k)

go way left:
    key(ctrl-a)
    key(a)
