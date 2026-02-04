# Push to GitHub & Deploy to Apify

## Step-by-Step Guide

### Prerequisites

- GitHub account (https://github.com/sign-up)
- Git installed ✅ (we verified this)

---

## Phase 1: Create GitHub Repository

### 1.1 Create Repo on GitHub

1. Go to https://github.com/new
2. **Repository name**: `google-maps-scraper`
3. **Description**: Google Maps Business Scraper for Apify
4. Choose **Public** or **Private**
5. **Don't** check "Initialize this repository with a README"
6. Click **Create repository**

### 1.2 Copy Your Repository URL

After creating, GitHub shows you the URL. It looks like:

```
https://github.com/YOUR_USERNAME/google-maps-scraper.git
```

Save this - you'll need it!

---

## Phase 2: Push Code to GitHub

### 2.1 Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2.2 Initialize Repository Locally

```bash
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

git init
```

### 2.3 Add All Files

```bash
git add .
```

### 2.4 Create Initial Commit

```bash
git commit -m "Initial commit: Google Maps scraper for Apify"
```

### 2.5 Add Remote (Replace YOUR_USERNAME!)

```bash
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git
```

### 2.6 Set Default Branch to main

```bash
git branch -M main
```

### 2.7 Push to GitHub

```bash
git push -u origin main
```

You may be asked to authenticate. GitHub will open a browser for you to authorize.

### 2.8 Verify on GitHub

Go to https://github.com/YOUR_USERNAME/google-maps-scraper

You should see all your files!

---

## Phase 3: Connect GitHub to Apify

### 3.1 Go to Apify Console

Navigate to https://console.apify.com

### 3.2 Create New Actor

1. Click **Actors** (left sidebar)
2. Click **Create Actor** button
3. Click **"From Git repository"** option

### 3.3 Configure Actor

1. **Git URL**: Paste your GitHub URL
   ```
   https://github.com/YOUR_USERNAME/google-maps-scraper.git
   ```
2. Click **Create**
3. Apify will automatically:
   - Detect `.actor/actor.json`
   - Build Docker container
   - Deploy your Actor

### 3.4 Test Your Actor

1. Go to your Actor page
2. Click **Run**
3. Configure search queries
4. Click **Start**
5. View results in **Dataset** tab

---

## Phase 4: Update Workflow

Once connected, updating is super simple:

### Update Your Code

```bash
# Make changes to your Python files
# Then:

git add .
git commit -m "Description of changes"
git push origin main
```

### Apify Auto-Updates

- Apify watches your GitHub repository
- When you push, Apify automatically:
  1. Pulls the new code
  2. Rebuilds the Docker image
  3. Deploys the new version
  4. Your Actor is immediately updated!

---

## Quick Reference

### Initial Setup (One Time)

```bash
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git init
git add .
git commit -m "Initial commit: Google Maps scraper"

git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git
git branch -M main
git push -u origin main
```

### Future Updates

```bash
git add .
git commit -m "Your change description"
git push origin main
```

---

## File Structure (What Gets Pushed)

✅ **Pushed to GitHub:**

- `scraper_simple.py` - Main scraper code
- `main.py` - Apify entry point
- `requirements.txt` - Dependencies
- `Dockerfile` - Container configuration
- `.actor/` folder - Apify configuration
- All other source files

❌ **NOT Pushed (in .gitignore):**

- `output/` folder
- `__pycache__/`
- `.env` files
- Virtual environments

---

## Troubleshooting

### "fatal: not a git repository"

```bash
git init
```

### "Permission denied (publickey)"

You need to set up SSH keys. Easier alternative: Use HTTPS and authenticate in browser.

### "Git not found"

Install Git from https://git-scm.com/download/win

### Apify not detecting actor.json

- Make sure `.actor/actor.json` exists
- Commit and push the `.actor` folder
- Wait a moment, then refresh Apify console

---

## Next Steps

1. **Create GitHub repo** at https://github.com/new
2. **Run Phase 2 commands** above (push to GitHub)
3. **Connect to Apify** (Phase 3)
4. **Test your Actor** from Apify console
5. **Make changes** and push - Apify updates automatically!

---

## Resources

- GitHub Help: https://docs.github.com
- Git Guide: https://git-scm.com/doc
- Apify Docs: https://docs.apify.com
- Apify GitHub Integration: https://docs.apify.com/platform/actors/development/git-integration
