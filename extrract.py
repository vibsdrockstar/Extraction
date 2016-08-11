#We need the urllib to get the site
import urllib2

#Then a request is created
request = urllib2.Request(url)
#Set the url:
url= "http://updates.collegespace.in/"

#Now a handle can be created which can be read out later
handle = urllib2.urlopen(request)

#Read content
content = handle.read()

#Conversion of text to an array
splitted_page = content.split("<td headers=\" files_downloads_h\">",1);

splitted_page = splitted_page[1].split("</td>",1)

print ("Downloads:") + splitted_page[0]
