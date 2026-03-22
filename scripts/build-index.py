#!/usr/bin/env python3
"""
Build the SEO-enhanced index.html from Lovable's build + pre-rendered content.

Usage:
  python3 scripts/build-index.py \
    --js assets/index-XXXX.js \
    --css assets/index-XXXX.css \
    --root-content root-content.html \
    --seo-head scripts/seo-head.html \
    --output index.html
"""
import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--js', required=True, help='Path to JS bundle (e.g. assets/index-XXX.js)')
    parser.add_argument('--css', required=True, help='Path to CSS bundle (e.g. assets/index-XXX.css)')
    parser.add_argument('--root-content', required=True, help='Path to pre-rendered root content HTML')
    parser.add_argument('--seo-head', default='scripts/seo-head.html', help='Path to SEO head template')
    parser.add_argument('--output', default='index.html', help='Output file path')
    args = parser.parse_args()

    with open(args.seo_head, 'r') as f:
        seo_head = f.read()

    with open(args.root_content, 'r') as f:
        root_content = f.read()

    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

{seo_head}

    <!-- Lovable React App -->
    <link rel="stylesheet" crossorigin href="/{args.css}">
    <script type="module" crossorigin src="/{args.js}"></script>
  </head>

  <body>
    <!-- GTM noscript -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX" height="0" width="0" style="display:none;visibility:hidden" title="GTM"></iframe></noscript>

    <!-- React root: pre-rendered for SEO, React hydrates over it -->
    <div id="root">
{root_content}
    </div>
  </body>
</html>"""

    with open(args.output, 'w') as f:
        f.write(html)

    print(f"Built {args.output} ({len(html)} bytes)")
    print(f"  JS:  /{args.js}")
    print(f"  CSS: /{args.css}")
    print(f"  Root content: {len(root_content)} chars")

if __name__ == '__main__':
    main()
