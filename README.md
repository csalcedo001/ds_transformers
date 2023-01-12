# Data structures and Transformers

Test transformer models in their capacity to learn data structures


## Overview

What are the limitations of transformer models in learning patterns from sequential data? Large language models (LLM) have shown remarkable results in learning patterns from natural language for expressive and realistic text generation. What if we now change the setup and test the capacity of transformers to learn the functions executed by data structures? Take a _stack_ as an example. We can perform a series of operations such as push or pop that modify the internal state of the stack. If we provide a transformer with the sequence of operations and arguments given to the stack in order as tokens, will it be able to learn the underlying mechanism that makes the data structure work the way it works?

input: \<PUSH\> <1> \<PUSH\> <5> \<POP\> \<PUSH\> <7> \<POP\> \<POP\>

output: <5> <7> <1>
