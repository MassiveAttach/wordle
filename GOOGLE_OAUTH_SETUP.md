# Google OAuth Setup Guide

This guide will help you set up Google OAuth authentication for the Wordle web application.

## Step 1: Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Create Project" or select an existing project
3. Give your project a name (e.g., "Wordle Game")
4. Click "Create"

## Step 2: Enable Google+ API

1. In the Google Cloud Console, go to "APIs & Services" > "Library"
2. Search for "Google+ API" 
3. Click on it and press "Enable"
4. Also search for "People API" and enable it (for user profile information)

## Step 3: Create OAuth 2.0 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen first:
   - Choose "External" user type
   - Fill in the required fields:
     - App name: "Wordle by Pavlo"
     - User support email: your email
     - Developer contact information: your email
   - Add scopes: `../auth/userinfo.email`, `../auth/userinfo.profile`
   - Add test users if needed (your email and friends' emails)

4. Create OAuth client ID:
   - Application type: "Web application"
   - Name: "Wordle Web App"
   - Authorized JavaScript origins:
     - `http://localhost:8000` (for local development)
     - `https://your-ngrok-url.ngrok-free.app` (replace with your ngrok URL)
   - Authorized redirect URIs:
     - `http://localhost:8000/auth/callback`
     - `https://your-ngrok-url.ngrok-free.app/auth/callback`

5. Click "Create"
6. Copy the Client ID and Client Secret

## Step 4: Update Environment Variables

1. Open the `.env` file in your project directory
2. Replace the placeholder values with your actual credentials:

```env
# Google OAuth Configuration
GOOGLE_CLIENT_ID=your_actual_client_id_here
GOOGLE_CLIENT_SECRET=your_actual_client_secret_here

# Flask Configuration
FLASK_SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///wordle.db
```

## Step 5: Important Notes

### For Local Development:
- Use `http://localhost:8000` as your base URL
- Make sure to add this to your OAuth authorized origins

### For Public Access (ngrok):
- Get your ngrok URL by running: `ngrok http 8000`
- Add the ngrok URL to your OAuth authorized origins
- Update the redirect URI to use the ngrok URL
- **Important**: ngrok free URLs change every time you restart the tunnel

### Security Considerations:
- Keep your `.env` file secure and never commit it to version control
- The `.env` file is already in `.gitignore`
- For production deployment, use environment variables instead of the `.env` file

## Step 6: Testing the Setup

1. Start your Flask application:
   ```bash
   python app_with_auth.py
   ```

2. Or use the batch file:
   ```bash
   start_server_multi_user.bat
   ```

3. Navigate to your application URL
4. You should see a login page with a "Login with Google" button
5. Click the button to test the OAuth flow

## Troubleshooting

### Common Issues:

1. **"redirect_uri_mismatch" error**:
   - Check that your redirect URI in Google Console matches exactly
   - Make sure you're using the correct protocol (http vs https)

2. **"invalid_client" error**:
   - Verify your Client ID and Client Secret are correct
   - Check that the OAuth client is enabled

3. **"access_denied" error**:
   - Make sure your app is not in testing mode with restricted users
   - Add your email to test users if the app is in testing mode

4. **App shows "This app isn't verified"**:
   - This is normal for development
   - Click "Advanced" > "Go to [Your App Name] (unsafe)" to continue
   - For production, you'll need to verify your app with Google

### Getting Help:
- Check the Google Cloud Console error logs
- Review the Flask application logs for detailed error messages
- Make sure all required APIs are enabled in Google Cloud Console

## Production Deployment

For production deployment:
1. Use a proper domain name instead of ngrok
2. Set up SSL/HTTPS
3. Verify your app with Google to remove the "unverified app" warning
4. Use environment variables instead of `.env` file
5. Consider using a production database (PostgreSQL, MySQL) instead of SQLite
