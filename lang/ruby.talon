mode: user.ruby
mode: command 
and code.language: ruby
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic
settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"
state return: "return "
signature:
    insert("sig {}")
    key(left)
binding pry:
    insert("require 'pry'; binding.pry")
type hash:
    insert("T::Hash[]")
    key(left)
type array:
    insert("T::Array[]")
    key(left)
blocker:
    key(escape)
    key(shift-a)
    insert(" do\n")
