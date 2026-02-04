# GitHub to Apify - Quick Checklist

## ✅ Pre-Flight Checklist

- [ ] GitHub account created at https://github.com/sign-up
- [ ] Git installed and working (`git --version` shows version)
- [ ] Code is ready in `c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper`

---

## 📋 Part 1: Create GitHub Repository (5 minutes)

- [ ] Go to https://github.com/new
- [ ] Repository name: `google-maps-scraper`
- [ ] Description: `Google Maps Business Scraper for Apify`
- [ ] Choose **Public** or **Private**
- [ ] Click **Create Repository**
- [ ] Copy the HTTPS URL

Example URL:

```
https://github.com/YOUR_USERNAME/google-maps-scraper.git
```

---

## 📋 Part 2: Push Code to GitHub (5 minutes)

Run these commands in PowerShell:

```powershell
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

# First time only:
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Initialize and commit
git init
git add .
git commit -m "Initial commit: Google Maps scraper for Apify"

# Replace YOUR_USERNAME with your actual GitHub username!
git remote add origin https://github.com/YOUR_USERNAME/google-maps-scraper.git
git branch -M main
git push -u origin main
```

**GitHub will ask you to log in - that's normal!**

- [ ] All commands ran successfully
- [ ] No errors in terminal
- [ ] Check GitHub - you should see your files there

---

## 📋 Part 3: Connect to Apify (5 minutes)

- [ ] Go to https://console.apify.com
- [ ] Click **Actors** in left sidebar
- [ ] Click **Create Actor** button
- [ ] Click **"From Git repository"** option
- [ ] Paste your GitHub URL
  ```
  https://github.com/YOUR_USERNAME/google-maps-scraper.git
  ```
- [ ] Click **Create**
- [ ] Wait for build to complete (takes 2-5 minutes)

---

## 🧪 Part 4: Test Your Actor (5 minutes)

- [ ] Navigate to your Actor page
- [ ] Click **Run** button
- [ ] Enter search queries (or use defaults):
  ```
  ["plumbers in New York"]
  ```
- [ ] Click **Start**
- [ ] Wait for execution to complete
- [ ] View results in **Dataset** tab

---

## 🎉 Success!

If you see businesses in the Dataset, you're done!

### Your Actor is now:

✅ Stored on GitHub (version controlled)
✅ Deployed on Apify (running in the cloud)
✅ Auto-updating (push to GitHub → Apify rebuilds)

---

## 🔄 Future Updates

Every time you want to update:

```powershell
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper

git add .
git commit -m "Your change description"
git push origin main
```

**Apify automatically rebuilds when you push!**

---

## ❓ Need Help?

- **Git Issues**: https://git-scm.com/doc
- **GitHub Issues**: https://docs.github.com
- **Apify Issues**: https://docs.apify.com

---

## 📝 Important Notes

1. **Replace YOUR_USERNAME** in all URLs with your actual GitHub username
2. **Public vs Private**:
   - Public = Anyone can see your code
   - Private = Only you can see it
3. **Apify Access**: Free Apify account required (https://apify.com/sign-up)

---

Ready to start? Begin with **Part 1** above! 🚀
