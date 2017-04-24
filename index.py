#-*-coding: utf-8-*-
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<html>"
print "<header>"
print '<meta charset="utf-8">'
print '<style>'
print 'body{font-family: "PT Mono"}'
print '</style>'
print '<body>'
import csv

fcsv = open(u'C:\\Users\\andreev_af\\Documents\\_РИО\\калькуляция\\ТаблицаКалькуляция.txt')

s = csv.reader(fcsv, delimiter='\t', quotechar="'")

n = s.next()
n = s.next()
n = s.next()
print n[0]
for i in n:
	print '<br />', i