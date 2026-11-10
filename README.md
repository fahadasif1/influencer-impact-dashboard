# Influencer Reach & Impact Dashboard

Static dashboard (no server, no database). It reads three CSV files in `data/`:

| File | What it holds |
|---|---|
| `data/influencers.csv` | One row per influencer: name, channel, handle, followers, reported video count |
| `data/videos.csv` | One row per video: `slug`, influencer, platform, link, post id, caption |
| `data/history.csv` | One row per video **per check**: date plus views, likes, comments, shares, saves. Leave unknown values blank (shown as N/A, never 0) |

## Updating
1. Add a row to `videos.csv` for a new video (unique `slug`, e.g. `tiktok-<id>`).
2. Add a row to `history.csv` each time you check it (same `slug`, new `collected_at` date). Two or more rows give a growth chart.
3. Edit on GitHub (pencil icon) and commit. The site updates in about a minute.
4. Run `python3 scripts/make_embedded.py` if you want `data/embedded.js` refreshed for opening `index.html` straight from a file.

## Rules
- Views are platform play counts and are not added up as an audience. Unique reach stays blank unless a creator shares their analytics.
- Engagement rate = (likes + comments + shares) / views.
- Do not commit phone numbers, commenter names or any personal contact data. This repo is public.
- No payment, cost or ROI data belongs here.

Open `index.html` (dashboard) or `video.html?id=<slug>` (single video).
