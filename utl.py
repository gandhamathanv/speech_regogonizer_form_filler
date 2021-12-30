import urllib.request
webUrl = urllib.request.urlopen('https://forms.gle/PQUkqKfvvPFZEhgdA')
data = webUrl.read()
print(data)
