from infoTransformer import mailContent

body_start = """
<!DOCTYPE html>
<html>
<head>
<style>

    .box {

    background-color: lightgrey;

    width: 300px;

    border: 10px solid black;

    padding: 50px;

    margin: 20px;

    }

</style>
</head>
    <body>
        <h1 style="text-decoration: underline black">Las peli:</h1>
        <p></p>
"""

body_end = """
    </body>
</html>
"""

mailBody = body_start + ''.join(mailContent) + body_end

print(mailBody)