#!/usr/bin/python 

#Import modules for CGI handling
import cgi, cgitb
 

#Import functions of other programs
import tools.seq_apps as sa
import tools.gcContent as gcCont

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
a_comp, g_comp, c_comp, t_comp = sa.composition(seq)
gc = gcCont.get_gcCont(seq)


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
print ' <h2>A: %s</h2>' % a_comp
print ' <h2>G: %s</h2>' % g_comp
print ' <h2>C: %s</h2>' % c_comp
print ' <h2>T: %s</h2>' % t_comp
print ' <h2>GC Content: %s</h2>' % gc
print '</div>'
print '<div id="footer">'
print '    @Tool Wrapper'
print '</div>'
print '</body>'
print '</html>'
