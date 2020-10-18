#trt
**translate your text on terminal**

'trt' is a CLI script that you can use to translate text on terminal.
Just set two _'language options'_ and enter your text and trt will get your translated text from "translate.google.com".

Example:

`$ trt -en -fr "I am a programmer"`

output:

`Je suis un programmeur`


There are three ways that you can enter your text.
1. By entering as an argument (like the example above).
2. By entering input mode (when you enter no arguments you will enter input mode).
3. By entering option '-c', this will get the text from your clipboard.

......


**NOTE:**

For using option '-c' you have to install a copy/paste mechanism such as 'xclip' or 'xsel'.

For further information check this link out.

https://pyperclip.readthedocs.io/en/latest/#not-implemented-error