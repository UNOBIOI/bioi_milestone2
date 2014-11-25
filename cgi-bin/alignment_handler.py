#!/usr/bin/python 

#Import modules for CGI handling
import cgi, cgitb
 

#Import functions of other programs
import tools.seq_apps as sa
import tools.blast_run as br

#Import Biopython modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
seq = form.getvalue('seq')
option = form.getvalue('dropdown')
fastafile = form.getvalue('fastafile')
length = str(len(seq))

# need to make calls to functions in seq_apps.py
#messenger_rna = Seq(seq, IUPAC.unambiguous_dna)

#blast_output = str(br.runBlast(seq))
#blast_output = str(blast_output)
headings, lengths, e_vals = br.runBlast(seq)

print 'Content-type:text/html\r\n\r\n'
print '<html>'
print '<head>'
print '<style>'
print '    #header {'
print '        background-color:black;'
print '        color:white;'
print '        text-align:center;'
print '        padding:5px;'
print '    }'
print '    #nav {'
print '        width:35%;'
print '        float:left;'
print '        padding:5px;'
print '    }'
print '    #section {'
print '        width:350px;'
print '        float:left;'
print '        padding:10px;'
print '    }'
print '    #footer {'
print '        background-color:black;'
print '        color:white;'
print '        clear:both;'
print '        text-align:center;'
print '        padding:5px;'
print '    }'
print '</style>'
print '    <title>Bioinformatics Tool Wrapper</title>'
print '</head>'
print '<body background="../images/images2.jpg" bgpropeties="fixed">'
print '<div id="header">'
print ' <h1>Alignment Tool</h1>'
print '</div>'
print '<div id = "results">'
print ' <h2>Length of sequence: %s </h2>' % length
print ' <h2>BLAST Results: </h2>'
n = 0
for head in headings:
    h = str(headings[n])
    l = str(lengths[n])
    e = str(e_vals[n])
    print '<p>'
    print 'Sequence: %s ' % h
    print '<br>Length: %s ' % l
    print '<br>E value: %s ' % e
    print '</p>'
    n = n + 1
print '</div>'
print '<div id="footer">'
print '    @Tool Wrapper'
print '</div>'
print '</body>'
print '</html>'
