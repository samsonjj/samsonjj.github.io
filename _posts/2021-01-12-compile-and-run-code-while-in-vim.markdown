---
layout: post
title: Compile and Run Code While In Vim
---

This is an incredibly useful shortcut I have found that makes my vim workflow fast. I'm using this workflow while doing the Rust Book examples.

My workflow:
1) Edit code
2) Compile & run code
3) Repeat

This shortcut makes step 2 very fast. We just set up a vim macro to do the compiling and running for us.

1) Start recording a macro by pressing `q` and then `r`. This will allow us to press `@r` in the future to run the macro that we record. Feel free to bind the macro to another letter besides `r`.
2) Enter command mode by pressing `:`.
3) We will execute a few terminal commands from the vim prompt, by prefixing them with `!`. This will run the commands outside vim, in the shell. First, we want to clear terminal, so we will execute a 'clear' command. Then we want to compile the code. Lastly we will run it. This can be accomplished all on the same line with `:w | clear && cargo run`. I left out that we want to save the file first, before compiling. Rust is nice and does the compiling and running of the code in one
command, 'cargo run'.
4) You will likely need to press a key to come back into vim. Then press `q` to stop recording the macro.

All done! Now you can use `@r` (or a different key than r if you changed the binding) to run your macro.
