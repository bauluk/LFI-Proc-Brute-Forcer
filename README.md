# LFI Proc Brute Forcer
This script will automatically brute force proc IDs. It requires a URL vulnerable to local file inclusion (LFI).

## Usage
```
python3 lfi-proc-brute-forcer.py -t <vulnerable_url> -i <iterations> [options]

Options:
-h, --help	 Show this menu.
-t, --target	 The destination URL to run this script against.
-i, --iterations The number of proc IDs to test for starting from zero.
-a, --all	 Test for all of the following proc types.
--cmdline	 Command line arguments.
--cpu		 Current and last cpu in which it was executed.
--cwd		 Link to the current working directory.
--environ	 Values of environment variables.
--exe		 Link to the executable of this process.
--fd		 Directory, which contains all file descriptors.
--maps		 Memory maps to executables and library files.
--mem		 Memory held by this process.
--root		 Link to the root directory of this process.
--stat		 Process status.
--statm		 Process memory status information.
--status	 Process status in human readable form.
```
