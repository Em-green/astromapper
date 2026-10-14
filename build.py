"""Regenerate the buildless HTML from the React source and CSS (Python 3 only)."""
from pathlib import Path
root = Path(__file__).resolve().parent
source = (root / 'AstroApp.jsx').read_text(encoding='utf-8')
source = source.replace('import React, { useState, useMemo } from "react";', 'const { useState, useMemo } = React;').replace('export default function App()', 'function App()')
css = (root / 'styles.css').read_text(encoding='utf-8')
page = '''<!doctype html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0E1029">
<title>AstroMapper — 星から探す、あなたの居場所</title>
<meta name="description" content="出生データから、恋愛・仕事・居心地など7つのテーマで土地との相性を楽しむ無料アストロカートグラフィーツール。出生時間がだいたいでも入力できます。">
<style>''' + css + '''</style>
</head>
<body>
<div id="root"><p style="padding:32px">AstroMapperを読み込み中…</p></div>
<noscript>このツールにはJavaScriptが必要です。ブラウザの設定で有効にしてください。</noscript>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.3.1/umd/react.production.min.js" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.3.1/umd/react-dom.production.min.js" crossorigin="anonymous"></script>
<script>
if (typeof React === 'undefined' || typeof ReactDOM === 'undefined') {
  document.getElementById('root').textContent = '読み込みに失敗しました。インターネット接続を確認して、ページを再読み込みしてください。';
} else {
''' + source + '''
ReactDOM.createRoot(document.getElementById('root')).render(React.createElement(App));
}
</script>
</body>
</html>
'''
(root / 'index.html').write_text(page, encoding='utf-8')
print('Generated index.html')
