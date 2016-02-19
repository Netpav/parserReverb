
echo %time%
:: Testovani dat

set LF=^


for /f eol^=^%LF%%LF%^ delims^= %%A IN (vzorek_10.txt) do (
    echo %%A | java -jar reverb-latest.jar -t >> out_reverb_lines.log
)

