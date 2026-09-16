# Kelvin Ervais — personal site

Static single page, served by GitHub Pages at https://kelvinervais.github.io/website

- `index.html` — the whole site. Navigation is a baseball diamond: each base is a section, a runner moves around the basepaths as you scroll, and a small diamond stays pinned once the big one scrolls away.
- `Golf/rounds.json` — golf rounds the chart reads, generated from an 18Birdies export
- `Golf/build_rounds.py` — regenerates `rounds.json` and strips account details from the raw export

To refresh golf data: export from 18Birdies, save it as `Golf/18Birdies_archive.json` (gitignored), then

```
python3 Golf/build_rounds.py Golf/18Birdies_archive.json
```

Never commit the raw export; it contains a phone number and email.
