# Copy-Paste Commands for GitHub to Apify

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Name: `google-maps-scraper`
3. Click Create
4. Copy the HTTPS URL shown (looks like: `https://github.com/YOUR_USERNAME/google-maps-scraper.git`)

---

## Step 2: Push to GitHub (Copy-Paste All Commands)

**In PowerShell:**

```powershell
# Navigate to project
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

# Configure git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Initialize repository
git init

# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: Google Maps scraper for Apify"

# Add remote - REPLACE YOUR_USERNAME!
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

**When prompted**: Log in with your GitHub account

---

## Step 3: Connect to Apify

1. Go to: https://console.apify.com
2. Click **Actors** (left sidebar)
3. Click **Create Actor**
4. Click **"From Git repository"**
5. Paste your GitHub URL:
   ```
   https://github.com/YOUR_USERNAME/google-maps-scraper.git
   ```
6. Click **Create**
7. Wait 2-5 minutes for build
8. Click **Run** to test

---

## Step 4: Update in Future

```powershell
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

git add .
git commit -m "Describe your changes here"
git push origin main
```

Apify automatically rebuilds!

---

## ✨ That's It!

Your Actor is now:

- On GitHub (version controlled)
- On Apify (running in cloud)
- Auto-updating (push = auto-deploy)

---

## Common Mistakes to Avoid

❌ Don't forget to replace `YOUR_USERNAME` with your actual GitHub username
❌ Don't use SSH URL - use HTTPS URL
❌ Don't skip `git push` - Apify only sees what's on GitHub
✅ Do commit your changes before pushing
✅ Do wait for Apify build to complete
✅ Do test your Actor after deployment

---

## Verify Success

### After git push:

- Check: https://github.com/YOUR_USERNAME/google-maps-scraper
- You should see all your files there

### After connecting to Apify:

- Check: https://console.apify.com
- You should see "google-maps-scraper" in your Actors list
- Build status should show "Success"

### After running Actor:

- Check the **Dataset** tab
- You should see business data extracted

If all three ✅, you're done!

---

## Quick Reference URLs

- **Create GitHub Repo**: https://github.com/new
- **My GitHub Repos**: https://github.com/YOUR_USERNAME?tab=repositories
- **Apify Console**: https://console.apify.com
- **Apify Docs**: https://docs.apify.com
- **Git Help**: https://git-scm.com

---

Questions? See the full guides:

- `GITHUB_TO_APIFY.md` - Complete walkthrough
- `GITHUB_APIFY_CHECKLIST.md` - Step-by-step checklist
