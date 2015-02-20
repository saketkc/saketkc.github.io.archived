---
layout: post
title: "Python silence traceback on Ctrl+c"
date: 2014-11-19 00:44:50 -0800
comments: true
categories: python, hacks
---
I came across this small little hack while 
writing my downloader for NCBI-SRA datasets(Should be on PyPI soon!)


{% codeblock lang:python %}
import signal
signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))
{% endcodeblock %}


### What did we just do?
using `signal.signal()` I set the `handler` to `sys.exit(0)` for `signal.SIGINT`
which is translated to a `KeyBoardInterrupt` exception(invoked on a `Ctrl+C` press)

Read more about the `signal` module [here](https://docs.python.org/2/library/signal.html).
