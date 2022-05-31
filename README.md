# sagasu

Running this script on a Linux machine will let you search recursively through any directory available from your current directory position for a regular expression. If there is a hit, the file name and the corresponding lines, containing the requested phrase, will be printed out.

## Example

Executing the following lines
```sh
cd ~/Documents

sagasu 'yellow'
```

will search in any file that can be found from the _Documents_ directory for a line that contains the word *_yellow_*.
The output should be something like this:
```sh
src/File.cs:

Console.WriteLine('yellow blue red');
```


