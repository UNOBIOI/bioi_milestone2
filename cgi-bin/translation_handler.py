#!/usr/bin/python 

#Import modules for CGI handling
import cgi, cgitb
 

#Import functions of other programs
import tools.seq_apps as sa

#Import Biopython modules
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
seq = form.getvalue('seq')
option = form.getvalue('dropdown')
fileitem = form['fastafile'].value
length = str(len(seq))

# read file
fp = open('userinput.txt', 'wb')
fp.write(fileitem)
fp.close()

# need to make calls to functions in seq_apps.py
#messenger_rna = Seq(seq, IUPAC.unambiguous_dna)
trans = sa.translation(seq)
rev = sa.reverseComp(seq)


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
print ' <h1>Translation and Reverse Composition Tool</h1>'
print '</div>'
print '<div id = "results">'
print ' <h2>Translation of sequence: %s </h2>' % trans
print ' <h2>Reverse of complement of sequence: %s </h2>' % rev
print ' <h2>Length of sequence: %s </h2>' % length
print '</div>'
print '<div id="footer">'
print '    @Tool Wrapper'
print '</div>'
print '</body>'
print '</html>'
