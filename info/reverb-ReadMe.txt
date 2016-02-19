============================================================================
REVERB
============================================================================

http://reverb.cs.washington.edu/README.html
http://ai.cs.washington.edu/www/media/papers/reverb.pdf

******************
EXECUTION
******************
Jednotlive: java -Xmx8g -jar reverb-latest.jar vzor.TXT -t > vystup_vzor
Davkove: dir /s /b /a:-D "Reverb_data\*.text" | java -Xmx8g -jar reverb-latest.jar -f > vystup
dir /s /b /a:-D "Reverb_data\*.text" | java -Xmx8g -jar reverb-latest.jar -f -t -a > vystup
FOR %c in (C:\Reverb\Reverb_data\*.text) DO  echo %c | java -Xmx8g -jar reverb-latest.jar -f
************ 
dir /s /b /a:-D "Reverb_data\*.text" > reverb-todo.list
FOR /F "usebackq tokens=1,2* delims=," %G IN ("reverb-todo.list") DO java -Xmx8g -jar reverb-latest.jar %G > %G.ptxt -> ulozeni vysledku 
FOR /F "usebackq tokens=1,2* delims=," %G IN ("reverb-todo.list") DO java -Xmx8g -jar reverb-latest.jar -a %G > %G.ptxta -> ulozeni vysledku ArgLearner

************
HELP
************
usage: CommandLineReVerb [OPTIONS] [FILES]
 -a,--argLearner        Use ArgLearner to identify extraction arguments
                        (experimental, slower but more accurate). If you
                        use this setting, the minFreq, noConstraints,
                        keepOverlap, and allowUnary values will be
                        ignored.
 -f,--files             Read file list from standard input
 -h,--help              Print help and exit
 -K,--keepOverlap       Do not merge overlapping relations (Default is to
                        merge.)
 -m,--minFreq <arg>     Each relation must have at a minimum this many
                        number of distinct arguments in a large corpus.
 -N,--noConstraints     Do not enforce the syntactic and lexical
                        constraints that are part of ReVerb.
 -p,--filter-pronouns   Filter out arguments that contain a pronoun
 -q,--quiet             Quiet mode (don't print messages to standard
                        error)
 -s,--strip-html        Strip HTML before extracting
 -t,--timing            Provide detailed timing information
 -U,--allowUnary        Allow relations with a single argument to be
                        output. (Default setting is to disallow unary
                        relations.)

Output Columns:
    1. filename
    2. sentence number
    3. arg1
    4. rel
    5. arg2
    6. arg1 start
    7. arg1 end
    8. rel start
    9. rel end
    10. arg2 start
    11. arg2 end
    12. conf
    13. sentence words
    14. sentence pos tags
    15. sentence chunk tags
    16. arg1 normalized
    17. rel normalized
    18. arg2 normalized