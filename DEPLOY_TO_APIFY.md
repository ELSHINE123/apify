# Deploying to Apify

## Prerequisites

1. **Node.js installed** (Apify CLI requires Node.js)
2. **Apify account** at https://apify.com (free account available)
3. **Apify CLI installed**

## Step 1: Install Apify CLI

```bash
npm install -g apify-cli
```

## Step 2: Authenticate with Apify

```bash
apify login
```

This will open your browser to authenticate. Log in with your Apify account.

If you don't have an account, create one at: https://apify.com/sign-up

## Step 3: Navigate to Project Directory

```bash
cd c:\Users\user\Desktop\create\ai-automation-nocode\google-maps-scraper
```

## Step 4: Push to Apify

```bash
apify push
```

This will:

1. Create a new Actor on Apify (or update existing)
2. Build the Docker image
3. Deploy the Actor
4. Provide you with a URL to your Actor

## Step 5: Run Your Actor

After pushing, you can run it in three ways:

### Option 1: Via Apify Console (easiest)

1. Go to https://console.apify.com
2. Find your Actor "google-maps-scraper"
3. Click "Run"
4. Configure input (search queries, filters)
5. Click "Start"
6. View results in the dataset

### Option 2: Via Apify CLI

```bash
apify call
```

### Option 3: Via API

```bash
curl -X POST https://api.apify.com/v2/acts/{YOUR_ACTOR_ID}/runs \
  -H "Authorization: Bearer YOUR_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "searchQueries": ["plumbers in New York"],
      "maxResultsPerQuery": 20,
      "filterNoWebsite": true
    }
  }'
```

## Understanding the Input Schema

When you run the Actor, you can customize:

**searchQueries** (required)

- Array of search terms
- Examples: `["plumbers in New York", "electricians in Los Angeles"]`

**maxResultsPerQuery**

- How many results per search (default: 20, max: 50)

**filterNoWebsite**

- Only return businesses without websites (default: true)
- Perfect for landing page targeting!

**minRating**

- Optional: filter by minimum rating (0-5)
- Example: 4.0 = 4+ stars only

**minReviewCount**

- Optional: filter by minimum review count
- Example: 5 = must have 5+ reviews

## Example: Run with Custom Input

Create `input.json`:

```json
{
  "searchQueries": [
    "plumbers in New York",
    "electricians in Boston",
    "hvac contractors in Chicago"
  ],
  "maxResultsPerQuery": 15,
  "filterNoWebsite": true,
  "minRating": 4.0,
  "minReviewCount": 5
}
```

Then run:

```bash
apify call --input-file input.json
```

## Troubleshooting

### "apify not found"

```bash
npm install -g apify-cli
```

### "Not authenticated"

```bash
apify login
```

### Build fails

- Make sure Docker is installed and running
- Check that all files are in the right place
- Look at build logs in Apify console

### Actor runs but gets no results

- Try simpler search queries
- Check internet connection in Actor logs
- Increase `maxResultsPerQuery`

## After Deployment

Once deployed:

1. **Share your Actor**: Get the public URL from Apify console
2. **Integrate with workflows**: Use Apify API in your automation
3. **Schedule runs**: Set up automated scraping on a schedule
4. **Monitor**: View logs, performance, and results

## Next Steps

1. Install CLI and authenticate
2. Run `apify push`
3. Go to https://console.apify.com
4. Find your Actor and test it
5. Share with your team or integrate with your workflows

## Resources

- Apify Console: https://console.apify.com
- Apify Docs: https://docs.apify.com
- Actor Examples: https://apify.com/store
