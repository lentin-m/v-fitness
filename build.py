# Baut index.html aus der Artifact-Datei (winter-bulk-tracker.html)
import sys,re,hashlib
src=sys.argv[1] if len(sys.argv)>1 else '../winter-bulk-tracker.html'
s=open(src,encoding='utf8').read()
cut=s.find('<style>');head_extra=s[:cut];body=s[cut:]
head_extra=re.sub(r'<meta name="claude:[^>]*>\n?','',head_extra)
ver=hashlib.sha1(s.encode()).hexdigest()[:8]
html=f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#000000">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="V Fitness">
<meta name="robots" content="noindex,nofollow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-180.png">
{head_extra}</head>
<body style="background:#000">
{body}
<script>if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("sw.js?v={ver}").catch(()=>{{}}));</script>
</body>
</html>
'''
open('index.html','w',encoding='utf8').write(html)
sw=open('sw.template.js',encoding='utf8').read().replace('__VER__',ver)
open('sw.js','w',encoding='utf8').write(sw)
print('ok',ver,len(html))
