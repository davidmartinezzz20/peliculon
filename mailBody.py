from infoTransformer import d, filmDate, filmName, filmHref, filmImage

body_start = """
<!DOCTYPE html>
<html>
<head>
</head>
    <body>
        <h1 style="text-decoration: underline black">Las peli:</h1>
        <p></p>
"""
content = []
for i in d:
    x = """
    <img src="""+filmImage+"""/><br/>
    <a style="color: #000000">"""+filmName+"""</a><br/>
    <a style="color: #000000" href="""+filmHref+">Sinopsis</a><br/>""""
    <a style="color: #000000">Fecha de estreno: """+filmDate+"""</a><br/><br/>"""
    content.append(x)

body_end = """
    </body>
</html>
"""

mailBody = body_start + ''.join(content) + body_end

print(mailBody)