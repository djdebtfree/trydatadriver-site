# Data Driver — Static Marketing Site

Static HTML/CSS/JS site for [trydatadriver.com](https://trydatadriver.com), hosted on Netlify.

## Quick Start

No build step required. Open `index.html` in a browser or deploy to Netlify.

## How to Update Content

1. Edit `index.html` directly — all copy, sections, and structured data are in one file
2. CSS is in `css/styles.css`
3. JS is in `js/main.js` (scroll animations, FAQ accordion, mobile nav)
4. Push to `main` branch — Netlify auto-deploys

## How to Add GTM / Pixel IDs

All tracking runs through Google Tag Manager. No hardcoded pixel scripts.

1. Open `index.html`
2. Find `GTM-XXXXXXX` (appears twice — `<head>` script and `<noscript>` iframe)
3. Replace with your GTM container ID (e.g., `GTM-ABC1234`)
4. Inside GTM, add these tags:
   - **Google Analytics 4**: GA4 Configuration tag with your Measurement ID (G-XXXXXXX)
   - **Facebook/Meta Pixel**: Custom HTML tag with your Pixel base code
   - **Any other pixels**: Add via GTM, not hardcoded

## How to Trigger a New Deploy

- **Auto-deploy**: Push to `main` branch on GitHub
- **Manual deploy**: Go to Netlify dashboard → Deploys → "Trigger deploy"
- **CLI**: `netlify deploy --prod` (requires `npm i -g netlify-cli && netlify login`)

## DNS Instructions — Point trydatadriver.com to Netlify

### Option A: Netlify DNS (recommended)

1. In Netlify dashboard → Domain settings → Add custom domain → `trydatadriver.com`
2. Netlify will prompt you to use Netlify DNS
3. Update your domain registrar's nameservers to:
   ```
   dns1.p06.nsone.net
   dns2.p06.nsone.net
   dns3.p06.nsone.net
   dns4.p06.nsone.net
   ```
   (Exact nameservers shown in Netlify dashboard)
4. Wait for DNS propagation (up to 48 hours, usually < 1 hour)
5. Netlify auto-provisions SSL via Let's Encrypt

### Option B: External DNS (keep existing DNS provider)

1. In Netlify dashboard → Domain settings → Add custom domain → `trydatadriver.com`
2. Add these DNS records at your registrar:

   | Type  | Name | Value                          |
   |-------|------|--------------------------------|
   | A     | @    | 75.2.60.5                      |
   | CNAME | www  | your-site-name.netlify.app     |

3. Enable "HTTPS" in Netlify domain settings after DNS propagates
4. Netlify auto-provisions SSL via Let's Encrypt

### Verify

```bash
# Check DNS propagation
dig trydatadriver.com +short

# Check HTTPS
curl -I https://trydatadriver.com
```

## File Structure

```
├── index.html          # Full page with SEO, AEO, structured data
├── css/styles.css      # All styles
├── js/main.js          # Scroll animations, FAQ, mobile nav
├── images/
│   ├── logo.jpeg       # Brand logo
│   └── og-image.jpg    # Open Graph share image (replace with actual)
├── robots.txt          # Allow all crawlers
├── sitemap.xml         # XML sitemap
├── netlify.toml        # Netlify build config, headers, redirects
├── _redirects          # Netlify redirect rules
└── README.md           # This file
```

## SEO Checklist

- [x] Unique `<title>` and `<meta description>`
- [x] Open Graph and Twitter Card meta tags
- [x] Canonical URL
- [x] robots.txt allowing all crawlers
- [x] XML sitemap at /sitemap.xml
- [x] JSON-LD: Organization, Product, FAQPage, HowTo, Speakable
- [x] Semantic HTML (header, main, nav, footer, article, section)
- [x] Alt text on all images
- [x] Internal anchor linking (#how-it-works, #platform, #pricing, #faq)

## AEO Checklist

- [x] FAQ schema markup (8 questions)
- [x] HowTo schema (3-step setup)
- [x] Speakable schema on key content

## Performance

- [x] No framework — zero JS overhead
- [x] Lazy loading on images and video
- [x] Preconnect to Google Fonts and GTM
- [x] CSS/JS cacheable with immutable headers
- [x] Single HTTP request for CSS, single for JS
