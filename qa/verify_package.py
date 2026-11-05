#!/usr/bin/env python3
"""Public-artifact integrity test; does NOT validate native workbook or Power BI execution."""
from pathlib import Path
import re, sys, zipfile, struct
base = Path(__file__).resolve().parents[1]
readme = (base / 'README.md').read_text(encoding='utf-8')
refs = re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', readme) + re.findall(r'!\[[^\]]*\]\(([^)]+)\)', readme)
missing = [ref for ref in refs if not ref.startswith(('http://', 'https://', '#', 'mailto:')) and not (base / ref.split('#')[0]).is_file()]
required = ['README.md', 'DATA_SOURCE.md', 'NOTICE.md', 'docs/executive-case-study.pdf', 'assets/social-preview.png']
required += (['assets/dashboard-overview.png'] if 'food-beverage' in base.name else ['assets/executive-overview.jpg', 'assets/encounters-and-utilization.jpg', 'assets/financial-and-coverage.jpg', 'assets/patient-behavior.jpg'])
missing_required = [name for name in required if not (base / name).is_file()]
# Images: PNG dimensions from IHDR; no third-party dependencies.
preview = base / 'assets/social-preview.png'
valid_preview = bool(preview.exists() and preview.read_bytes()[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', preview.read_bytes()[16:24]) == (1280,640))
# PDF page count via PyMuPDF when installed; fall back to existence/size.
pdf = base / 'docs/executive-case-study.pdf'
valid_pdf = pdf.exists() and pdf.stat().st_size > 100000
pages = 0
try:
 import fitz
 with fitz.open(pdf) as doc:
  pages = len(doc)
 valid_pdf = valid_pdf and pages == (5 if 'food-beverage' in base.name else 15)
except ImportError:
 pass
checks = {
 'required_files': not missing_required,
 'local_readme_links': not missing,
 'portfolio_return_link': 'https://data.ianocamposystems.com' in readme,
 'source_limitations_disclosed': 'not' in readme.lower() and 'DATA_SOURCE.md' in readme,
 'social_preview_1280x640': valid_preview,
 'approved_pdf': valid_pdf,
 'no_stale_public_release_checklist': not (base/'RELEASE_CHECKLIST.md').exists()
}
for name,ok in checks.items():print(('PASS' if ok else 'FAIL')+'  '+name)
if missing_required:print('Missing assets:',missing_required)
if missing:print('Broken links:',missing)
sys.exit(0 if all(checks.values()) else 1)
