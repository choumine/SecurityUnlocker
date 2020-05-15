<!-- index.tpl（文件名） -->
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>SecrecyAutoUnlocker</title>
  </head>
  <body>
  <h1>SecrecyAutoUnlocker</h1>
  <form method = 'post' action = './'>
  IMEI:<br />
  <input type = 'text' name = 'imei'><br />
  时戳:<br />
  <input type = 'text' name = 'timestamp'><br />
  <br />
  <button>提交</button>
  </form>
  　<br />
  <form action = './view'>
    <button>查看</button>
  </form>
  </body>
</html>