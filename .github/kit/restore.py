"""Puts the realluked account kit back into index.html (and kit.js back) if a rebuild dropped them."""
import pathlib, shutil, sys
root = pathlib.Path(__file__).resolve().parents[2]
html_path, kit_path = root / 'index.html', root / 'kit.js'
backup_kit, lines = root / '.github/kit/kit.js', (root / '.github/kit/kit-lines.html').read_text()
changed = []
if not kit_path.exists():
    shutil.copyfile(backup_kit, kit_path); changed.append('kit.js')
html = html_path.read_text()
if 'src="kit.js"' not in html:
    if '</body>' not in html: sys.exit('index.html has no </body>')
    html_path.write_text(html.replace('</body>', lines + '</body>', 1)); changed.append('index.html')
print('restored: ' + ', '.join(changed) if changed else 'kit already present')
pathlib.Path('restored.txt').write_text(' '.join(changed))
