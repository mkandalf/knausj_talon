os: mac
app: iterm2
-
tag(): terminal
# todo: filemanager support
tag(): user.file_manager
tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.tabs
tag(): user.tmux

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
