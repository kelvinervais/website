# Kelvin Ervais — personal site

Static single page, served by GitHub Pages at https://kelvinervais.github.io/website

- `index.html` — the whole site (hand-written CSS, no build step)
- `Golf/rounds.json` — golf scores the chart reads, generated from an 18Birdies export
- `Golf/build_rounds.py` — regenerates `rounds.json`; strips account details from the raw export

To refresh golf data: export from 18Birdies, then

```
python3 Golf/build_rounds.py ~/Downloads/18Birdies_archive.json
```

Never commit the raw export; it contains a phone number and email.
